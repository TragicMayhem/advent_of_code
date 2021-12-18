

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    # def toTree(self):
    #     for i, elem in enumerate(self.data):
    #         if not isinstance(elem, int):
    #             if i == 0:
    #                 self.left = Node(elem)
    #                 self.left.toTree()
    #             else:
    #                 self.right =  Node(elem)
    #                 self.right.toTree()
    #         else:
    #             if i == 0:
    #                 self.left = Node(elem)
    #             else:
    #                 self.right =  Node(elem)

    
    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def is_leaf(self):
        check = self.left is None and self.right is None
        return check

    def _split(self):
        """Split big number (>=10) into child numbers
            So a leaf node becomes parent, creating two leaf nodes that total the parent
            without using math module now removed (floor(v/2), ceil(v/2))"""
        
        # if self.data > 10: # how to check this or do you call when you know?  error handing!
        big_number=self.data
        ln = big_number // 2
        rn = big_number - ln
    
        self.data=None # need to check what use this for
        self.left=Node(ln)
        self.right=Node(rn)
        print("split", self.data, self.left,self.right)


    def try_and_split(self):
        print("try_and-split", self.data)
        if self.is_leaf():
            if self.data >= 10:
                print("val is leaf and over 10")
                self._split()
                return True
            else:
                return False
        else:
            return self.left.try_and_split() or self.right.try_and_split()


    def __repr__(self):
        """Leaf nodes are represented by their contents
        Other nodes are represented by their children (recursively)"""
        return f"[{self.left}, {self.right}]" if self.data is None else f"{self.data}"

      
    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
      
    
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res





def toTreeFromList(data):
    '''
    takes in list (length of 2) which can be int or nested lists
    for each element, recursively call with new element to build out the tree of nodes
    '''
    root = Node(data)

    for i, elem in enumerate(data):

        if not isinstance(elem, int):
        # Means its a list so create a new tree
            if i == 0:
                root.left = toTreeFromList(elem)
            else:
                root.right = toTreeFromList(elem)
        else:
            # if it is an integer then just make a node (leaf)
            if i == 0:
                root.left = Node(elem)
            else:
                root.right =  Node(elem)
    
    return root


test_list = [[1, 2], [[1, 2], 3], [9, [8, 7]], [[1, 9], [8, 5]], [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9]]
test_list2 = [[1, 2], [[1, 12], 3], [9, [8, 7]], [[1, 19], [8, 15]], [[[[1, 2], [13, 4]], [[5, 6], [7, 8]]], 9]]

print()
print("TEST",test_list)
root = toTreeFromList(test_list)
root.PrintTree()
print(root.depth())
print()

print(test_list)
print(root)

print()
print(root.try_and_split())
print(root)

print("TEST2")
print(test_list2)
root = toTreeFromList(test_list2)
print(root.depth())
root.PrintTree()
print(root)
print(root.try_and_split())
print(root)
print()


# l1 = [1,2]
# l2 = [1,[3,4]]
# l3 = [[3,4],1]

# print()
# print("L1",l1)
# root = toTreeFromList(l1)
# root.PrintTree()
# print(root.depth())

# print()
# print("L2",l2)
# root = toTreeFromList(l2)
# root.PrintTree()
# print(root.depth())

# print()
# print("L3",l3)
# root = toTreeFromList(l3)
# root.PrintTree()
# print(root.depth())


# root = Node([1,2])
# root.toTree()
# root.PrintTree()
# print(root.inorderTraversal(root)) 

# print()
# root = Node([1,[3,4]])
# root.toTree()
# root.PrintTree()
# print(root.inorderTraversal(root)) 

# print()
# root = Node([[3,4],6])
# root.toTree()
# root.PrintTree()
# print(root.inorderTraversal(root)) 

# print()
# root = Node([1,[[5,6],4]])
# root.toTree()
# root.PrintTree()

# # Use the insert method to add nodes
# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)
# root.PrintTree()

# print(root.inorderTraversal(root)) 
# print(root.PreorderTraversal(root))
# print(root.PostorderTraversal(root))