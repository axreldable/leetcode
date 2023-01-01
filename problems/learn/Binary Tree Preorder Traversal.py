from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rez = []
        rez.append(root.val)
        rez.extend(self.preorderTraversal(root.left))
        rez.extend(self.preorderTraversal(root.right))

        return rez

    def preorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        rez = []
        stack.append(root)

        while len(stack) > 0:
            el = stack.pop()
            rez.append(el.val)
            if el.right:
                stack.append(el.right)
            if el.left:
                stack.append(el.left)

        return rez


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(3)
    tree = TreeNode(2, left=tree)
    tree = TreeNode(1, right=tree)
    print(s.preorderTraversal(tree))  # [1,2,3]
    print(s.preorderTraversalIter(tree))  # [1,2,3]

    print(s.preorderTraversal(None))  # []
    print(s.preorderTraversalIter(None))  # []

    tree = TreeNode(1)
    print(s.preorderTraversal(tree))  # [1]
    print(s.preorderTraversalIter(tree))  # [1]
