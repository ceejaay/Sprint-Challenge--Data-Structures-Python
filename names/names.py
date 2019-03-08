# This takes 15 seconds on a 2012 macbook air.
import time

# How to optimize this code:
#     I'm not sure a heap would work. Because these names don't seem to be organized 
# A heap would still have to go through every item in the list
# We could add them to a heap and organize them.
# That would take more time. But it would be easier to search for them
# Put one list in a heap. Check the other list against the heap.

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      if value < self.value:
          if self.left == None:
              self.left = BinarySearchTree(value)
          else:
              self.left.insert(value)
      else:
          if self.right == None:
              self.right = BinarySearchTree(value)
          else:
              self.right.insert(value)


  def contains(self, target):
      if target == self.value:
          return True
      elif target < self.value:
          if self.left == None:
              return False
          else:
              return self.left.contains(target)
      elif target > self.value:
          if self.right == None:
              return False
          else:
              return self.right.contains(target)






start_time = time.time()


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# print(names_1)

tree = BinarySearchTree(names_1[0])
# print(tree.value)

for i in range(1, len(names_1)):
    tree.insert(names_1[i])

duplicates = []

for item in names_2:
    if tree.contains(item):
        duplicates.append(item)



# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# print(duplicates_1 == duplicates)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

