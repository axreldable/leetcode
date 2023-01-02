from typing import Optional


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def conect_s(root: 'Optional[Node]', parent: 'Optional[Node]', stype: str):
            if not root:
                return None

            if not parent or not parent.next:
                root.next = None

            if stype == 'l':
                root.next = parent.right
            elif stype == 'r' and parent.next:
                root.next = parent.next.left

            conect_s(root.left, root, 'l')
            conect_s(root.right, root, 'r')

            return root

        return conect_s(root, None, '')

    def level_connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = []
        q.append(root)

        while len(q) > 0:
            n = len(q)

            for i in range(n):
                if i != n - 1:
                    q[i].next = q[i + 1]

            for _ in range(n):
                el = q.pop(0)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
        return root

    def level_traverse(self, tree: Optional[Node]):
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
                if not el.next:
                    rez.append('#')
        return rez


if __name__ == "__main__":
    s = Solution()

    tree = Node(1,
                left=Node(2, left=Node(4), right=Node(5)),
                right=Node(3, left=Node(6), right=Node(7))
                )

    rez = s.level_traverse(tree)
    print(rez)
    # connected = s.connect(tree)
    connected = s.level_connect(tree)
    rez = s.level_traverse(connected)
    print(rez)
