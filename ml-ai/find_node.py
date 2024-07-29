class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_value(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return find_value(root.left, target) or find_value(root.right, target)


# Example Usage (Binary Tree)
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

# Example Usage (Binary Search Tree)
root2 = TreeNode(8)
root2.left = TreeNode(3)
root2.right = TreeNode(10)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(6)
root2.right.right = TreeNode(14)

target_value = 5
if find_value(root1, target_value):
    print(f"{target_value} found in the first tree!")
else:
    print(f"{target_value} not found in the first tree.")

if find_value(root2, target_value):
    print(f"{target_value} found in the second tree!")
else:
    print(f"{target_value} not found in the second tree.")
