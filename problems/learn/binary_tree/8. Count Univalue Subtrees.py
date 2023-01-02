from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def is_uni(root: TreeNode) -> bool:
            if not root.left and not root.right:
                return True

            if root.left and root.right:
                return root.val == root.left.val and root.val == root.right.val and is_uni(root.left) and is_uni(
                    root.right)
            elif root.left:
                return root.val == root.left.val and is_uni(root.left)
            else:
                return root.val == root.right.val and is_uni(root.right)

        if not root:
            return 0

        stack = []
        count = 0
        stack.append(root)

        while len(stack) > 0:
            el = stack.pop()
            if is_uni(el):
                count += 1
            if el.right:
                stack.append(el.right)
            if el.left:
                stack.append(el.left)

        return count


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(5,
                    left=TreeNode(1, left=TreeNode(5), right=TreeNode(5)),
                    right=TreeNode(5, right=TreeNode(5))
                    )
    print(s.countUnivalSubtrees(tree))  # 4

    tree = TreeNode(5,
                    left=TreeNode(5, left=TreeNode(5), right=TreeNode(5)),
                    right=TreeNode(5, right=TreeNode(5))
                    )
    print(s.countUnivalSubtrees(tree))  # 6

    tree = TreeNode(1,
                    left=TreeNode(1, left=TreeNode(5), right=TreeNode(5)),
                    right=TreeNode(1, right=TreeNode(5))
                    )
    print(s.countUnivalSubtrees(tree))  # 3
