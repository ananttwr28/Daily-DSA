# Binary Tree Theory 22/9/25

# Build tree given pre order sequence

from collections import deque           # deque is implemented using DLL in py


# <-------------------------- Build Tree from Preorder Seq. ---------------------------------------> 

# 1. tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Binary Tree Class for building whole tree from list of elements/nodes
class BinaryTree:
    def __init__(self):
        self.idx = -1		# 7. index to iterate the whole list and create tree, using self to set the idx of that object initialised and making sure we are using that only
    def build_tree(self, nodes):			# 3. fn. to build tree takes list of nodes and returns root
        self.idx += 1		# 8. increment each time fn. is called
    
        if nodes[self.idx] == -1:		# 9. return none for -1
            return None
        new_node = TreeNode(nodes[self.idx])             # 10. create new nodes for rest of elts.
        new_node.left = self.build_tree(nodes)
        new_node.right = self.build_tree(nodes)
        
        return new_node
    
# <----------------------------------------------------------------------------------->


# <---------------------- preorder traversal ------------------------------------------->
# preorder traversal/ print node -> go left -> right

def preorder(root):     # TC O(N), SC O(H) 
    if root is None:
        print(-1, end=" ")         # print(-1, " ") print in another line, end by default is newline, here telling that keep space after every print. sep=" " by default to separate multi args on same line.
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
    
# <----------------------------------------------------------------------------------->


# <------------------------- level order traversal ------------------------------------------>

def levelorder(root):           # TC O(N) visiting each node at max once, SC O(M) Max number of nodes at a level < N
    if root is None:
        return
    q = deque()      # dequeue for storing node data for level order, and popleft is O(1) TC
    q.append(root)          # adding root (and direct reference/ obj not the val as printing val.val will give error) first and None to print newline after 1 level is finsihed
    q.append(None)
    
    while q:
        curr = q.popleft()

        if curr is None:        # if the curr is None, print new line and if it was last item, then break dont push anything else push new None in the Queue
            print()

            if not q:
                break
            else:
                q.append(None)
        else:
            print(curr.val, end=" ")       # print curr elt. and before moving to it's adjacent add its childrens in the Q.

            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)

# <----------------------------------------------------------------------------------->
		
if __name__ == "__main__":			# 4. main fn. execution will start here, we will create binary tree here
    nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
    # 5. create obj of BTree class
    tree = BinaryTree()
    
    # 6. call build tree fn of Btree class obj that returns root node
    root = tree.build_tree(nodes)
    
    print(root.val)

    preorder(root)      # print tree in preorder traversal

    print()
    levelorder(root)


"""

TC - O(N) visiting each idx once 1 traversal.
If the tree is skewed (like a linked list), the height = n, so SC = O(n).
If the tree is balanced, height = O(log n), so SC = O(log n).  (Bcz n is divided into 2 equal parts)

"""
