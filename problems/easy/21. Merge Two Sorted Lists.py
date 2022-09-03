# Definition for singly-linked list.
import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        ptr = self
        while ptr is not None:
            print(ptr.val, end=" ")
            ptr = ptr.next


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, item):
        tmp = ListNode(item)

        if self.root is None:
            self.root = tmp
        else:
            ptr = self.root
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = tmp

    def print(self):
        ptr = self.root
        while ptr is not None:
            print(ptr.val, end=" ")
            ptr = ptr.next


def fromArr(arr):
    rez = LinkedList()
    for i in arr:
        rez.insert(i)
    return rez.root


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val <= list2.val:
            ptr_s = list1
            ptr_l = list2
        else:
            ptr_s = list2
            ptr_l = list1

        rez = None
        cur = None
        while ptr_s is not None:
            print(ptr_s.val)
            if cur is not None:
                cur.next = ListNode(ptr_s.val)
                cur = cur.next
            else:
                cur = ListNode(ptr_s.val)
            if rez is None:
                rez = cur

            ptr_s = ptr_s.next
            if ptr_s is not None:
                if ptr_s.val > ptr_l.val:
                    ptr_tmp = ptr_s
                    ptr_s = ptr_l
                    ptr_l = ptr_tmp

        while ptr_l is not None:
            if cur is not None:
                cur.next = ListNode(ptr_l.val)
                cur = cur.next
                ptr_l = ptr_l.next
            else:
                cur = ListNode(ptr_l.val)
                ptr_l = ptr_l.next

        return rez


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    s.mergeTwoLists(fromArr([1, 2, 4]), fromArr([1, 3, 4])).print()  # [1,1,2,3,4,4]
    print()
    print(s.mergeTwoLists(fromArr([]), fromArr([])))  # []
    s.mergeTwoLists(fromArr([]), fromArr([0])).print()  # [0]
    print()

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(s+t)")
    print("Space complexity: O(1)")
