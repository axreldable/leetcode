from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        start = head
        l = 0
        while head:
            l += 1
            head = head.next
        for_drop = l - n - 1
        if for_drop == -1:
            return start.next
        l = 0
        head = start
        while head:
            if l == for_drop:
                head.next = head.next.next
            head = head.next
            l += 1
        return start

    def print_list(self, list):
        rez = []
        while list:
            rez.append(list.val)
            list = list.next
        print(rez)


if __name__ == "__main__":
    s = Solution()

    list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rez = s.removeNthFromEnd(list, 2)  # [1,2,3,5]
    s.print_list(rez)

    list = ListNode(1)
    rez = s.removeNthFromEnd(list, 1)  # []
    s.print_list(rez)

    list = ListNode(1, ListNode(2))
    rez = s.removeNthFromEnd(list, 1)  # [1]
    s.print_list(rez)

    list = ListNode(1, ListNode(2))
    rez = s.removeNthFromEnd(list, 2)  # [2]
    s.print_list(rez)
