from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rez = []
        rez.extend(self.postorderTraversal(root.left))
        rez.extend(self.postorderTraversal(root.right))
        rez.append(root.val)

        return rez

    def postorderTraversalIter(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(3)
    tree = TreeNode(2, left=tree)
    tree = TreeNode(1, right=tree)
    print(s.postorderTraversal(tree))  # [3,2,1]
    print(s.postorderTraversalIter(tree))  # [3,2,1]

    print(s.postorderTraversal(None))  # []
    print(s.postorderTraversalIter(None))  # []

    tree = TreeNode(1)
    print(s.postorderTraversal(tree))  # [1]
    print(s.postorderTraversalIter(tree))  # [1]
