from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        while head:
            s.append(str(head.val))
            head = head.next

        return self.is_palindrom("".join(s))

    def is_palindrom(self, s: str):
        while len(s) > 1:
            if s[0] != s[len(s) - 1]:
                return False
            s = s[1:len(s) - 1]
        return True


if __name__ == "__main__":
    s = Solution()

    list = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    rez = s.isPalindrome(list)  # true
    print(rez)

    list = ListNode(1, ListNode(2))
    rez = s.isPalindrome(list)  # false
    print(rez)
