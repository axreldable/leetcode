class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        arr = []
        for c in s:
            if c in arr:
                if len(arr) > max_length:
                    max_length = len(arr)
                for i, e in enumerate(arr):
                    if e == c:
                        arr = arr[i+1:]
                        # print(arr)
            arr.append(c)
            # print(arr)

        if len(arr) > max_length:
            max_length = len(arr)

        # print(max_length)
        return max_length


if __name__ == "__main__":
    s = Solution()

    s.lengthOfLongestSubstring("abcabcbb")  # 3
    s.lengthOfLongestSubstring("bbbbb")  # 1
    s.lengthOfLongestSubstring("pwwkew")  # 3
    s.lengthOfLongestSubstring("abcade")  # 5
