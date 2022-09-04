import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        smin = prices[0]
        mprofit = 0
        for i, el in enumerate(prices):
            if el < smin:
                smin = el
            elif el - smin > mprofit:
                mprofit = el - smin

        return mprofit

    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) == 0:
    #         return 0
    #
    #     smin = prices[0]
    #     min_index = 0
    #     smax = prices[0]
    #     max_index = 0
    #
    #     profit = 0
    #
    #     for i, el in enumerate(prices):
    #         if el < smin:
    #             if max_index > min_index:
    #                 tmp = smax - smin
    #                 if tmp > profit:
    #                     profit = tmp
    #
    #             smin = el
    #             min_index = i
    #         else:
    #             if max_index < min_index:
    #                 if el > smin:
    #                     smax = el
    #                     max_index = i
    #             else:
    #                 if el > smax:
    #                     smax = el
    #                     max_index = i
    #
    #     if max_index > min_index:
    #         tmp = smax - smin
    #         if tmp > profit:
    #             profit = tmp
    #     return profit


if __name__ == "__main__":
    st = time.time()

    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))  # 0
    print(s.maxProfit([1, 2, 3, 4]))  # 3
    print(s.maxProfit([4, 3, 2, 1]))  # 0
    print(s.maxProfit([1, 1, 1, 1]))  # 0
    print(s.maxProfit([1, 2, 1, 2]))  # 1
    print(s.maxProfit([]))  # 0
    print(s.maxProfit([1]))  # 0
    print(s.maxProfit([2, 4, 1]))  # 2

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
