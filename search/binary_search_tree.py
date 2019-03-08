class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    pass    

  def breadth_first_for_each(self, cb):
      q = [self]
      while len(q) > 0:
        print('array', q)
          # print('len', len(q))
          # print(f'q zero: {q[0].value}')
        if q[0].left != None:
           print('left', q[0].left.value)
           q.append(q[0].left)
          # print('left ', q[0].left.value )
        if q[0].right != None:
           print('right', q[0].right.value)
           q.append(q[0].right)
          # print('right ', q[0].right.value )
        cb(q[0].value)
        # print('len before', len(q))
        q.pop(0)
        # print('len after', len(q))

# what I want to know is if there are children. I want to know if there is a left child or a right child. then I want to add any children to the array.


          # if this returns false then I know we have no children on this node
          # if it returns true we have two children
          # if parent.left and parent.right == None:
          #     return
          # elif 

      # if parent.left == None:
      #     print('no left')
      # elif parent.right == None:
      #     print('no right')
      # else:



      # if parent.left == None:
      #     print('no left child')
      # else:
      #     print('left child => ', parent.left.value)

      # if parent.right == None:
      #   print('no right child')
      # else:
      #   print('right child => ', parent.right.value)




      # first add the parent.
      # check if there is a left child.
      # if so, add it to the queue.
      #     if there isn't a left child
      #         return
      # check if there is a right child 
      # if there is add it to the queue.
      #     if there isn't a right child return

      



      # we need a queue.

      # Then we need to add the root.
      # Look at the root. Add it's children to the queue
      # Call the callback on the root.
      # Then pop the root from the queue
      # then repeat with the children.
      # don't need recursion. because we have to go through the entire tree
      # We have to be careful of NoneType problems.
      # This is a binary search tree, not a heap.
      # So we have to find a way to check for children.





  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

bst = BinarySearchTree(5)
bst.insert(3)
bst.insert(4)
bst.insert(10)
bst.insert(9)
bst.insert(11)
bst.breadth_first_for_each(lambda x: x + 1)
