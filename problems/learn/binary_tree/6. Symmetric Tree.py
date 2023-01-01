from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                if i == 'null':
                    sub_rez.append(-1)
                else:
                    sub_rez.append(i.val)
                    if i.left:
                        q.append(i.left)
                    else:
                        q.append('null')
                    if i.right:
                        q.append(i.right)
                    else:
                        q.append('null')
            rez.append(sub_rez)

        return rez

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return True

        pre_order_1 = self.level_order(root.left)
        pre_order_2 = self.level_order(root.right)

        for i, e in enumerate(pre_order_2):
            pre_order_2[i] = e[::-1]

        # print(pre_order_1)
        # print(pre_order_2)
        return pre_order_1 == pre_order_2

    def is_mirror(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and self.is_mirror(l.left, r.right) and self.is_mirror(l.right, r.left)

    def isSymmetric_2(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)


if __name__ == "__main__":
    s = Solution()

    tree = TreeNode(1,
                    left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                    right=TreeNode(2, left=TreeNode(4), right=TreeNode(3))
                    )
    print(s.isSymmetric(tree))  # True
    print(s.isSymmetric_2(tree))  # True

    tree = TreeNode(1,
                    left=TreeNode(2, right=TreeNode(3)),
                    right=TreeNode(2, right=TreeNode(3))
                    )
    print(s.isSymmetric(tree))  # False
    print(s.isSymmetric_2(tree))  # False
