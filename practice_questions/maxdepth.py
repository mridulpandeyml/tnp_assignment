# leetcode 104. Maximum Depth of Binary Tree
#https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1950375007

class TreeNode:
    def __init__(self, value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


class solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1