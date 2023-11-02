import pickle
from hoffman import decode

def getBits(byte):
      string = ''
      while(byte > 0):
            string = string + str(byte%2)
            byte = byte//2
      for i in range(8-len(string)):
            string += '0'
      
      return string[::-1]

tree = pickle.load(open("./HoffTree", "rb"))


with open("./test.bin", "rb") as bin:
      
      buffer = bin.readlines()
      bit_string = ''
      for line in buffer:
            for byte in line:
                  for bit in getBits(byte):
                        bit_string += bit
      string = decode(tree, bit_string)
      print(string)