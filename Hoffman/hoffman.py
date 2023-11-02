import pickle

class node: 

      def __init__(self, sym, value, left=None, right=None):
            self.value = value 
            self.sym = sym
            self.left = left
            self.right = right
            self.huff = ''
      
      def __lt__(self, other):
            if(type(other) == int):
                  return False
            return self.value < other.value
      
      def __str__(self):
            return f"'{self.sym}': {self.value}"

class save_node:

      def __init__(self, node):
            if(len(node.sym) == 1):
                  self.sym = node.sym
                  self.left = None
                  self.right = None
            else:             
                  self.left = save_node(node.left)
                  self.right = save_node(node.right)
      


def save(node):

      save_tree = save_node(node)

      pickle.dump(save_tree, open("./HoffTree", "wb"))
      
def getEncoding(node, encoding=''): 
      lst=[]
      print(node)
      encoding = encoding + str(node.huff)
      if(node.left):
            lst.append(getEncoding(node.left, encoding))
      if(node.right):
            lst.append(getEncoding(node.right, encoding))
      
      if(not node.right and not node.left):
            return (node.sym, encoding)
      
      return lst

def getPrefix(node, char, encoding=''):
      encoding = encoding + str(node.huff)
      if(node.left or  node.right):
            if(node.left.sym.find(char) != -1):
                  return getPrefix(node.left, char, encoding)
            elif(node.right.sym.find(char) != -1):
                  return getPrefix(node.right, char, encoding)
      else:
            return encoding

def decode(node, bit_string):
      current = node
      string = '' 
      while(len(bit_string)>0):
            
            if(current.left or current.right):

                  if(bit_string[0] == '0'):
                        current = current.left
                        bit_string = bit_string[1::]
                  elif(bit_string[0] == '1'):
                        current = current.right
                        bit_string = bit_string[1::]
                  else:
                        bit_string = bit_string[1::]
            else:
                  string += current.sym
                  current = node
      
      return string

