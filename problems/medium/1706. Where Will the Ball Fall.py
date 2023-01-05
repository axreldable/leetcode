from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def is_blocked(i, j):
            el = grid[i][j]
            if el == 1:
                if j == n - 1:
                    return True
                if grid[i][j + 1] == -1:
                    return True
                return False
            else:
                if j == 0:
                    return True
                if grid[i][j - 1] == 1:
                    return True
                return False

        rez = []
        for k in range(n):
            i = 0
            j = k
            while i < m and not is_blocked(i, j):
                if grid[i][j] == 1:
                    j += 1
                else:
                    j -= 1
                i += 1
            if i == m:
                rez.append(j)
            else:
                rez.append(-1)

        return rez


if __name__ == "__main__":
    s = Solution()

    rez = s.findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1],
                      [-1, -1, -1, -1, -1]])  # [1,-1,-1,-1,-1]
    print(rez)

    rez = s.findBall([[-1]])  # [-1]
    print(rez)

    rez = s.findBall(
        [[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]])  # [0,1,2,3,4,-1]
    print(rez)
