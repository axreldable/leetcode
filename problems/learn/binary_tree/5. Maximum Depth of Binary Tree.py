from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return max(l, r) + 1


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    tree = TreeNode(3, left=TreeNode(9), right=tree)
    print(s.maxDepth(tree))  # 3

    print(s.maxDepth(None))  # 0

    tree = TreeNode(1)
    print(s.maxDepth(tree))  # 1
