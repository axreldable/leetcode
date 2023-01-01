from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The algorithm starts with a root node and visit the node itself first.
# Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth.
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        rez = []
        q = []
        q.append(root)

        while len(q) > 0:
            sub_rez = []
            n = len(q)
            for _ in range(n):
                i = q.pop(0)
                sub_rez.append(i.val)
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)
            rez.append(sub_rez)

        return rez


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    tree = TreeNode(3, left=TreeNode(9), right=tree)
    print(s.levelOrder(tree))  # [[3],[9,20],[15,7]]

    print(s.levelOrder(None))  # []

    tree = TreeNode(1)
    print(s.levelOrder(tree))  # [1]
