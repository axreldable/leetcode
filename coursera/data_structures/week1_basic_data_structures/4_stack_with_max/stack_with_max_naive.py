# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.smax = None

    def Push(self, a):
        if len(self.__stack) == 0:
            self.smax = a
            self.__stack.append(a)
        elif self.smax < a:
            max_replacer = 2 * a - self.smax
            self.__stack.append(max_replacer)
            self.smax = a
        else:
            self.__stack.append(a)

    def Pop(self):
        assert (len(self.__stack))
        # print(self.__stack, self.smax)
        el = self.__stack.pop()
        if len(self.__stack) == 0:
            self.smax = None
            return el
        if el < self.smax:
            return el
        else:
            for_return = self.smax
            self.smax = 2 * for_return - el
            return for_return

    def Max(self):
        assert (len(self.__stack))
        return self.smax


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert (0)
