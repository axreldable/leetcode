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

    @staticmethod
    def from_arr(arr):
        if len(arr) == 0:
            return None

        rez = None
        cur = None
        for i in arr:
            if cur is None:
                cur = ListNode(i)
                rez = cur
            else:
                cur.next = ListNode(i)
                cur = cur.next
        return rez


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        counter = 0
        cur = head
        while cur is not None:
            counter += 1
            cur = cur.next

        middle = round(counter / 2 + 0.6)

        rez = head
        counter = 1
        while counter < middle:
            rez = rez.next
            counter += 1

        return rez


if __name__ == "__main__":
    st = time.time()

    ListNode.from_arr([1, 2, 3]).print()
    print()

    s = Solution()
    s.middleNode(ListNode.from_arr([1, 2, 3, 4, 5])).print()  # [3,4,5]
    print()
    s.middleNode(ListNode.from_arr([1, 2, 3, 4, 5, 6])).print()  # [4,5,6]
    print()
    s.middleNode(ListNode.from_arr([1, 2, 3, 4])).print()  # [3,4]
    print()

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
