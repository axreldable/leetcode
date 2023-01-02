from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])
        index = -1
        for i, el in enumerate(inorder):
            if el == root.val:
                index = i
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        return root

    def preorder_traverse(self, tree: Optional[TreeNode]):
        rez = []

        if not tree:
            rez.append('null')
            return rez

        rez.append(tree.val)
        rez.extend(self.preorder_traverse(tree.left))
        rez.extend(self.preorder_traverse(tree.right))

        return rez


if __name__ == "__main__":
    s = Solution()

    print([1, 2, 3][:1])
    print([1, 2, 3][1:-1])

    rez = s.preorder_traverse(
        s.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))  # [3,9,20,null,null,15,7]
    print(rez)
    rez = s.preorder_traverse(s.buildTree(inorder=[-1], postorder=[-1]))  # [-1]
    print(rez)
