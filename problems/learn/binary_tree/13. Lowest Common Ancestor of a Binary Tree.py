from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root is None:
            return None

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if (left_res and right_res) or (root.val in [p.val, q.val]):
            return root
        else:
            return left_res or right_res

    def level_traverse(self, tree: Optional[TreeNode]):
        if not tree:
            return None

        q = []
        rez = []
        q.append(tree)

        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                el = q.pop(0)
                rez.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
        return rez


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(3,
                    left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8))
                    )
    rez = s.level_traverse(tree)
    print(rez)
    ancestor = s.lowestCommonAncestor(tree, TreeNode(5), TreeNode(1))
    rez = s.level_traverse(ancestor)
    print(rez)

    tree = TreeNode(3,
                    left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8))
                    )
    rez = s.level_traverse(tree)
    print(rez)
    ancestor = s.lowestCommonAncestor(tree, TreeNode(5), TreeNode(4))
    rez = s.level_traverse(ancestor)
    print(rez)

    tree = TreeNode(3,
                    left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8))
                    )
    rez = s.level_traverse(tree)
    print(rez)
    ancestor = s.lowestCommonAncestor(tree, TreeNode(5), TreeNode(8))
    rez = s.level_traverse(ancestor)
    print(rez)

    tree = TreeNode(3,
                    left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8))
                    )
    rez = s.level_traverse(tree)
    print(rez)
    ancestor = s.lowestCommonAncestor(tree, TreeNode(7), TreeNode(4))
    rez = s.level_traverse(ancestor)
    print(rez)

    print(None or None)
