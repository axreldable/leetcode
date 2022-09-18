import time

# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children or []


class NAryTree:
    def __init__(self, val):
        self.root = Node(val)

    def find_node(self, node: Node, val) -> Node:
        if node is None or node.val == val:
            return node
        for child in node.children:
            rez_node = self.find_node(child, val)
            if rez_node:
                return rez_node
        return None

    def add(self, parent_val, val):
        parent_node = self.find_node(self.root, parent_val)
        parent_node.children.append(Node(val))

    def print_tree(self, node, rez_str):
        if node is None:
            return ""
        rez_str = str(node.val) + "("
        for i in range(len(node.children)):
            rez_str += self.print_tree(node.children[i], rez_str)
            if i < len(node.children) - 1:
                rez_str += ","
        rez_str += ")"
        return rez_str

    def __str__(self):
        return self.print_tree(self.root, "")

    @staticmethod
    def from_arr(arr):
        rez = NAryTree(arr[0])

        i = 2
        if len(arr) < i:
            return rez

        el = arr[i]
        parent_i = 0
        while i < len(arr) - 1:
            parent = arr[parent_i]
            while el is not None:
                el = arr[i]
                print(parent, el)
                rez.add(parent, el)
                i += 1
            i += 1
            el = arr[i]
            parent_i = i

        return rez


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        return []


if __name__ == "__main__":
    st = time.time()

    tree = NAryTree(1)
    tree.add(1, 3)
    tree.add(1, 2)
    tree.add(1, 4)
    tree.add(3, 5)
    tree.add(3, 6)

    print(tree)
    print(NAryTree.from_arr([1, None, 3, 2, 4, None, 5, 6]))

    # s = Solution()
    # print(s.preorder([1, None, 3, 2, 4, None, 5, 6]))  # [1,3,5,6,2,4]
    # print(s.preorder(
    #     [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None,
    #      14]))  # [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

    et = time.time()
    elapsed_time = et - st
    print("Execution time:", elapsed_time, "seconds")

    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
