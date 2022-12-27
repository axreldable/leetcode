from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate(s: str) -> ListNode:
    l = ListNode(int(s[len(s) - 1]))
    p = l
    for i in reversed(range(0, len(s) - 1)):
        n = ListNode(int(s[i]))
        p.next = n
        p = n
    return l


def print_list(l1: ListNode):
    rez = str(l1.val)
    n = l1.next
    while n is not None:
        rez += " " + str(n.val)
        n = n.next
    print(rez[::-1])
    return rez[::-1]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print_list(l1)
        # print_list(l2)
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            mem = 0
            v = l1.val + l2.val + mem
            if v > 9:
                mem = 1
                v = v - 10
            else:
                mem = 0
            rez = ListNode(v)
            f = l1.next
            s = l2.next
            p = rez
            while f is not None and s is not None:
                v = f.val + s.val + mem
                if v > 9:
                    mem = 1
                    v = v - 10
                else:
                    mem = 0
                p.next = ListNode(v)
                p = p.next
                f = f.next
                s = s.next
            while f is not None:
                v = f.val + mem
                if v > 9:
                    mem = 1
                    v = v - 10
                else:
                    mem = 0
                p.next = ListNode(v)
                p = p.next
                f = f.next
            while s is not None:
                v = s.val + mem
                if v > 9:
                    mem = 1
                    v = v - 10
                else:
                    mem = 0
                p.next = ListNode(v)
                p = p.next
                s = s.next
            if mem != 0:
                p.next = ListNode(mem)
            return rez


if __name__ == "__main__":
    # print_list(generate("807"))
    # print_list(generate("0"))
    # print_list(generate("89990001"))

    s = Solution()
    print_list(s.addTwoNumbers(generate("342"), generate("465")))
    print_list(s.addTwoNumbers(generate("0"), generate("0")))
    print_list(s.addTwoNumbers(generate("9999999"), generate("9999")))
    # assert print_list(s.addTwoNumbers(generate("342"), generate("465"))) == "807"
    # assert print_list(s.addTwoNumbers(generate("0"), generate("0"))) == "0"
    # assert print_list(s.addTwoNumbers(generate("9999999"), generate("9999"))) == "10009998"
