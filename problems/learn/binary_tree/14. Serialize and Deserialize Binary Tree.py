from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def ser_arr(tree):
            q = []
            rez = []
            q.append(tree)

            while len(q) > 0:
                n = len(q)
                for _ in range(n):
                    el = q.pop(0)
                    if type(el) == str:
                        rez.append(el)
                    else:
                        rez.append(el.val)
                        if el.left:
                            q.append(el.left)
                        else:
                            q.append('null')
                        if el.right:
                            q.append(el.right)
                        else:
                            q.append('null')

            return rez

        if not root:
            return '[]'

        rez = ser_arr(root)
        return '[' + ','.join(list(map(lambda x: str(x), rez))) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        elements = data[1:len(data) - 1].split(',')

        stack = []
        rez = TreeNode(int(elements.pop(0)))
        stack.append(rez)

        while len(stack) > 0:
            n = len(stack)
            for _ in range(n):
                if not stack[0]:
                    stack.pop(0)
                    continue
                left = elements.pop(0)
                right = elements.pop(0)
                if left == 'null':
                    left = None
                else:
                    left = TreeNode(int(left))
                if right == 'null':
                    right = None
                else:
                    right = TreeNode(int(right))
                stack[0].left = left
                stack[0].right = right
                stack.append(left)
                stack.append(right)
                stack.pop(0)

        return rez

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
    ser = Codec()

    tree = TreeNode(3,
                    left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8))
                    )
    rez = ser.serialize(tree)
    print(rez)

    ans = ser.deserialize(rez)
    print(ser.level_traverse(ans))

    tree = TreeNode(1,
                    left=TreeNode(2),
                    right=TreeNode(3, left=TreeNode(4), right=TreeNode(5))
                    )
    rez = ser.serialize(tree)
    print(rez)
    ans = ser.deserialize(rez)
    print(ser.level_traverse(ans))

    tree = None
    rez = ser.serialize(tree)
    print(rez)
    ans = ser.deserialize(rez)
    print(ser.level_traverse(ans))
