from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rez = []
        rez.extend(self.inorderTraversal(root.left))
        rez.append(root.val)
        rez.extend(self.inorderTraversal(root.right))

        return rez

    def inorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        rez = []
        curr = root

        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            rez.append(curr.val)
            curr = curr.right

        return rez


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(3)
    tree = TreeNode(2, left=tree)
    tree = TreeNode(1, right=tree)
    print(s.inorderTraversal(tree))  # [1,3,2]
    print(s.inorderTraversalIter(tree))  # [1,3,2]

    print(s.inorderTraversal(None))  # []
    print(s.inorderTraversalIter(None))  # []

    tree = TreeNode(1)
    print(s.inorderTraversal(tree))  # [1]
    print(s.inorderTraversalIter(tree))  # [1]
