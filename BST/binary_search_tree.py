# Binary Search Tree Theory 12/10/25

"""
BST is prefered over BTree for faster search O(H) as compared to O(N)
If the tree is skewed (like a linked list), the height = H
If the tree is balanced, height = O(log n) (Bcz n is divided into 2 equal parts)
"""

# <-------------------------- Build BST ---------------------------------------> 

# Class/ structure to hold 3 vars val, left and right binded to one entity node
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):      # 3. create new node, return type is of TreeNode
    if root is None:
        return TreeNode(val)
    if root.val > val:
        root.left = insert(root.left, val)      # 4. if val is smaller insert in left side and r.l will store instance/ obj. of the subtree/ tree node that will be returned
    else:        # root.val < val
        root.right = insert(root.right, val)

    return root

# <-------------------------- Print Inorder ---------------------------------------> 

def inorder(root):      # 7. this prints the BST as expected in increasing sorted seq.
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

# <-------------------------- search in BST ---------------------------------------> 

def search(root, key):
    if root is None:        # nothing matched we reached end so ret False
        return False
    elif root.val > key:
        return search(root.left, key)
    elif root.val == key:
        return True
    else:
        return search(root.right, key)
    
# <-------------------------- Delete a node in BST ---------------------------------------> 

def inorderSuccessor(self, root) -> Optional[TreeNode]:     # TC O(H) for finding null single sided call only
        while root.left is not None:
            root = root.left
        return root

def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:     # TC, SC O(H) for finding and deleting
    if root is None:
        return None
    # searching for the node to be deleted

    if root.val > key:      # search in left half root is > key
        root.left = self.deleteNode(root.left, key)
    elif root.val < key:      # search in right half key > root
        root.right = self.deleteNode(root.right, key)

    else:       # key found
        # case 1 no child
        if root.left is None and root.right is None:
            return None
        # case 2 single child
        elif root.left is None:
            return root.right       # to the parent
        elif root.right is None:
            return root.left       

        # case 3, 2 child

        # 1. find inorder successor in right subtree of the root to be deleted
        inorder_successor = self.inorderSuccessor(root.right)
        # 2. update root val with IS val
        root.val = inorder_successor.val
        # 3. delete the IS, same as case 1 or 2
        root.right = self.deleteNode(root.right, inorder_successor.val)     # r.r is from where it has to begin search and is.val is which val it has to delete, TC O(H), SC O(H) for finding and deleting 

    return root # at last


"""
12/10/25

TC -- O(H) {to find the root to be deleted} + [O(H) + O(H) {for case 3 only for finding IS, then delete}]
SC -- O(H) {call stack space}
"""
    

# <-------------------------- Main fn. ---------------------------------------------->

if __name__ == "__main__":			# main fn. execution will start here
# <-------------------------- Build BST ---------------------------------------> 
    values = [5, 1, 3, 4, 2, 7]     # 1. values from which nodes will be constructed
    # root = TreeNode()               
    root = None     # 2. initializing root as None
    for value in values:        # 5. build BST, TC O(N*H), SC O(N) + O(H)
        root = insert(root, value)
    
# <-------------------------- Print Inorder ---------------------------------------> 
    inorder(root)       # DFS TC O(N), SC O(H) stack space
    print()

# <-------------------------- search in BST ---------------------------------------> 

    if search(root, 8):
        print("Found")
    else:
        print("Not Found")

    