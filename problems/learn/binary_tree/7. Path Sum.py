from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum_bottom_up(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def leaf_sums(root: Optional[TreeNode]):
            if not root:
                return []

            rez = []
            if root.left:
                for s in leaf_sums(root.left):
                    rez.append(s + root.val)
            if root.right:
                for s in leaf_sums(root.right):
                    rez.append(s + root.val)

            if not root.left and not root.right:
                rez.append(root.val)

            return rez

        sums = leaf_sums(root)
        # print(sums)
        return targetSum in sums

    def hasPathSum_top_down(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum_top_down(root.left, targetSum) or self.hasPathSum_top_down(root.right, targetSum)


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(5,
                    left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))),
                    right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, right=TreeNode(1)))
                    )
    print(s.hasPathSum_bottom_up(tree, 22))  # True
    print(s.hasPathSum_top_down(tree, 22))  # True

    tree = TreeNode(1,
                    left=TreeNode(2),
                    right=TreeNode(3)
                    )
    print(s.hasPathSum_bottom_up(tree, 5))  # False
    print(s.hasPathSum_top_down(tree, 5))  # False
