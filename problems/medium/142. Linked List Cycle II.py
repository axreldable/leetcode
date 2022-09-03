import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        c = 20
        ptr = self
        while ptr is not None:
            print(ptr.val, end=" ")
            ptr = ptr.next

            c -= 1
            if c < 0:
                break

    @staticmethod
    def from_arr(arr, pos):
        if len(arr) == 0:
            return None

        cur = None
        rez = None
        cycle_elem = None
        for i, el in enumerate(arr):
            if cur is None:
                cur = ListNode(el)
                rez = cur
            else:
                cur.next = ListNode(el)
                cur = cur.next

            if i == pos:
                cycle_elem = cur

        if cycle_elem is not None:
            cur.next = cycle_elem

        return rez


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        s = set()

        cur = head
        rez = None
        while cur is not None:
            if cur in s:
                rez = cur
                break

            s.add(cur)
            cur = cur.next

        return rez


if __name__ == "__main__":
    st = time.time()

    ListNode.from_arr([1, 2, 3], -1).print()
    print()
    ListNode.from_arr([1, 2, 3], 0).print()
    print()
    ListNode.from_arr([1, 2, 3], 1).print()
    print()
    ListNode.from_arr([1, 2, 3], 2).print()
    print()
    print()

    s = Solution()
    s.detectCycle(ListNode.from_arr([1, 2, 3, 4, 5], 1)).print()  # [2, 3, 4, 5, ...]
    print()
    s.detectCycle(ListNode.from_arr([3, 2, 0, -4], 1)).print()  # [2, 0, -4, ...]
    print()
    print(s.detectCycle(ListNode.from_arr([1], -1))) # []
    print()

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(n)")
    print("Space complexity: O(n)")

    for index, item in enumerate([1, 2, 3]):
        print(index, item)
