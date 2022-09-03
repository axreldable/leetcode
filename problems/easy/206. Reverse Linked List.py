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

        cur = ListNode(arr[0])
        rez = cur
        i = 1
        while i < len(arr):
            cur.next = ListNode(arr[i])
            cur = cur.next
            i += 1

        return rez


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        ptr = head
        arr = [ptr.val]
        while ptr.next is not None:
            ptr = ptr.next
            arr.append(ptr.val)

        cur = None
        rez = None
        for i in range(len(arr) - 1, -1, -1):
            if cur is None:
                cur = ListNode(arr[i])
                rez = cur
            else:
                cur.next = ListNode(arr[i])
                cur = cur.next

        return rez


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    s.reverseList(ListNode.from_arr([1, 2, 3])).print()  # [3,2,1]
    print()

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(n)")
    print("Space complexity: O(n)")

    arr = []
    for i in range(4, -1, -1):
        arr.append(i)
    print(arr)
