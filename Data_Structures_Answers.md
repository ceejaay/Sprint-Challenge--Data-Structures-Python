Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
NA

2. What is the space complexity of your `depth_first_for_each` function?
NA

3. What is the runtime complexity of your `breadth_first_for_each` method?
The runtime complexity for the breadth first search on the binary search tree is O(n)
The search is touching every item in the tree.

4. What is the space complexity of your `breadth_first_for_each` method?
The space complexity for the breadth first search in the binary search tree is O(1 + 2)
The method I've written requires a list. At most that list gets 3 items.
The breadth first algorithm looks at a parent. It adds the two children of itself.
Then it runs the callback on the item at the zero index of the list.
After that, it removes that item.
Leaving only two items remaning. The next item adds it's children. 
So at any given time, the maximum size of the array is 3.
We drop the + 2 and the space complexity is O(1)


5. What is the runtime complexity of the provided code in `names.py`?
The runtime complexity of the provided code in names.py is O(n^2).
For each item in Names_1, the inner loop runs 10,000 times. Thus 10,000 * 10,000.

6. What is the space complexity of the provided code in `names.py`?
The space complexity of the code provided in names.py is O(n^2).
It creates one array for each list of names.

7. What is the runtime complexity of your optimized code in `names.py`?
The runtime complexity of the optimized code is as follows.
First the algorithm sorts the names in list. This runtime complexity is O(log n)
Next the algorithm goes through each name in names_2. The runtime for this is O(n). It has to check each name against the binary search tree.

Therfore, the runtime for the total algorithm is O(n log n).

8. What is the space complexity of your optimized code in `names.py`?
The space complexity for this solution is O(n^3).
Each list is put into an array. This O(n^2)
The space complexity for a Binary Search Tree is O(n).
We combine these for O(n^3)

