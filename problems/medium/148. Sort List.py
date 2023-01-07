from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        list = []

        while head:
            list.append(head.val)
            head = head.next

        list.sort()
        rez_list = ListNode(list[0])
        rez = rez_list
        for i in list[1:]:
            rez_list.next = ListNode(i)
            rez_list = rez_list.next

        return rez

    def print_list(self, list):
        rez = []

        while list:
            rez.append(list.val)
            list = list.next

        print(rez)
        return rez


if __name__ == "__main__":
    s = Solution()

    list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    rez = s.sortList(list)  # [1,2,3,4]
    s.print_list(rez)

    list = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    rez = s.sortList(list)  # [-1,0,3,4,5]
    s.print_list(rez)

    list = None
    rez = s.sortList(list)  # []
    s.print_list(rez)
