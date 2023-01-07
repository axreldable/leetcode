from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        rez = head
        index = 0
        first_even = head.next
        while head:
            next = head.next
            if head.next:
                if head.next.next:
                    head.next = head.next.next
                else:
                    if index % 2 == 0:
                        head.next = first_even
                    else:
                        head.next = None
            else:
                if index % 2 == 0:
                    head.next = first_even

            head = next
            index += 1

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

    list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rez = s.oddEvenList(list)  # [1,3,5,2,4]
    s.print_list(rez)

    list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    rez = s.oddEvenList(list)  # [1,3,5,2,4,6]
    s.print_list(rez)

    list = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    rez = s.oddEvenList(list)  # [2,3,6,7,1,5,4]
    s.print_list(rez)
