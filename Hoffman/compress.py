from hoffman import node, getEncoding, getPrefix, save

filename = input("Enter a file to compress.")

def toBits(byte):
    val = 0
    for i, bit in enumerate(byte[::-1]):
        val += int(bit) * 2**i

    return val


freq = dict()
data = None
sc = 0    
with open(filename, "r") as file:
    data = file.readlines()
    for line in data:
        for word in line:
            for sym in word:
                sc += 1
                if sym in freq.keys():
                    freq[sym] += 1 
                else: 
                    freq[sym] = 1
    

for key in freq.keys():
    freq[key] = round(freq[key] / sc, 3)

lst = sorted(freq.items(),key=lambda x: x[1])

nodes = list()
for tuple in lst:
    nodes.append(node(tuple[0], tuple[1]))

while(len(nodes) > 1):

    nodes = sorted(nodes, key=lambda x:x.value)
    left = nodes[0]
    right = nodes[1]

    nodes.remove(left)
    nodes.remove(right)

    left.huff = 0
    right.huff = 1

    newNode = node(left.sym+right.sym, left.value+right.value, left=left, right=right)
    nodes.append(newNode)

print(getEncoding(nodes[0]))

with open(f"{filename}.bin", "wb") as huf:
    for line in data:
        buffer = ''
        for sym in line:
            buffer += getPrefix(nodes[0],sym)
        
        bits = list()
        for i in range(0, len(buffer), 8):
        
            bits.append(toBits(buffer[i:i+8:]))
        
        huf.write(bytearray(bits)) 

save(nodes[0])