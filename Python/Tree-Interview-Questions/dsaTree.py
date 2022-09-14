### Given a binary tree root, check it's symmetric around its center. ###

#Example 1:
#Input: root = [1,2,2,3,4,4,3]
#Output: true

#Example 2:
#Input: root = [1,2,2,null,3,null,3]
#Output: false

# 1. Use recursion to check if the left and right subtrees are symmetric
# 2. If the left and right subtrees are symmetric, return True
# 3. If the left and right subtrees are not symmetric, return False

def isSymmetric(root):
    if root is None:
        return True
    else:
        return isMirror(root.left, root.right)

def isMirror(left, right):
    if left is None and right is None:
        return True
    elif left is not None and right is not None:
        if left.val == right.val:
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        else:
            return False
    else:
        return False

# 4. Resultant will be True if the tree is symmetric, False otherwise
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print("Is the tree symmetric?", isSymmetric(root))

# 5. Time complexity is O(n)