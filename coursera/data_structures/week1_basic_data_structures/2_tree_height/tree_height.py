# python3
import sys
import threading


class Node:
    def __init__(self, val, level=1):
        self.val = val
        self.children = []
        self.level = level

    def height(self):
        h = 0
        q = [self]
        last_level_elem = self
        while len(q) != 0:
            node = q.pop(0)
            # print(node.val)
            for c in node.children:
                q.append(c)
            if node == last_level_elem:
                h += 1
                if len(q) > 0:
                    last_level_elem = q[len(q) - 1]

        return h

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
        return self.print_tree(self, "")


def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
            # print("current", current)
            # print("height", height)
        max_height = max(max_height, height)
    return max_height


def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = []
    for i in range(n):
        nodes.append(Node(i))

    root = None
    for child_i in range(n):
        parent_i = parents[child_i]
        if parent_i == -1:
            root = nodes[child_i]
        else:
            nodes[parent_i].children.append(nodes[child_i])

    return root.height()


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# if __name__ == "__main__":
# main()
#
# files = listdir("tests")
# files.sort()
# for i, file in enumerate(files):
#     if file.endswith(".a"):
#         with open("tests/" + files[i - 1], "r") as f:
#             content = f.readlines()
#             n = int(content[0])
#             parents = list(map(int, content[1].split()))
#         answer = open("tests/" + files[i], "r").read().strip()
#         rez = compute_height_tree(n, parents)
#         # print(n, parents, answer, rez)
#         # print(answer, rez)
#         assert str(rez) == str(answer)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
