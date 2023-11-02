import sys

class MinHeap:

      FRONT = 1
      max_size = 0
      size = 0
      Heap = []

      def __init__(self, max_size):
            self.max_size = max_size
            self.Heap = [0 for i in range(max_size)] 
            self.Heap[0] = 1

      def parent(self, pos):
            return pos//2
      
      def left(self, pos):
            return pos * 2
      
      def right(self, pos):
            return pos * 2 + 1
      
      def isLeaf(self,pos):
            if(self.left(pos) > self.size):
                  return True
            return False

      def insert(self, value):
            
            self.size += 1
            self.Heap[self.size] = value
            current = self.size
            while(self.Heap[current] < self.Heap[self.parent(current)]):
                  self.swap(current, self.parent(current))
                  current = self.parent(current)

      def remove(self):

            popped = self.Heap[self.FRONT]
            self.Heap[self.FRONT] = self.Heap[self.size]
            self.size -= 1
            self.MinHeapify(self.FRONT) 
            return popped

      def swap(self, pos1, pos2):
            self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1]


      def MinHeapify(self, current):
            
            if(not self.isLeaf(current)):

                  if(self.Heap[current] > self.Heap[self.right(current)] or
                     self.Heap[current] > self.Heap[self.left(current)] ):

                        if(self.Heap[current] > self.Heap[self.left(current)]):
                              self.swap(current, self.left(current))
                              self.MinHeapify(self.left(current))
                        else:
                              self.swap(current, self.right(current))
                              self.MinHeapify(self.right(current))
                  
      def Print(self):
            for i in range(1, self.size + 1):
                  print(f"{self.Heap[i]} " , sep=' ', end='')
            print()

if(__name__ == "__main__"):
      mH = MinHeap(20)
      while(True):
            user = input("Enter a value:")
            if(user == "r"):
                  mH.Print()
                  mH.remove()
            elif (user == "q"):
                  break
            elif(user == "e"):
                  mH.Print()
            else: 
                  mH.insert(int(user))
                  print(f"Size: {mH.size}")
                  mH.Print()
