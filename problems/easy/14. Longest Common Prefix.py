from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_length = 0
        for i in strs:
            if len(i) > max_length:
                max_length = len(i)

        if max_length == 0:
            return ""

        for i in reversed(range(max_length)):
            is_all_same = True
            first = strs[0][0:i+1]
            for s in strs:
                if s[0:i+1] != first:
                    is_all_same = False
                    break
            if is_all_same:
                # print(first)
                return first

        return ""


if __name__ == "__main__":
    s = Solution()

    s.longestCommonPrefix(["flower", "flow", "flight"])  # "fl"
    s.longestCommonPrefix(["dog", "racecar", "car"])  # ""
    s.longestCommonPrefix([""])  # ""
    s.longestCommonPrefix(["a"])  # "a"
    print("done")
