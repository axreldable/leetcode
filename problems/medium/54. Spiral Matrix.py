from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        offset = 0
        rez = []
        while offset <= m // 2 and offset <= n // 2:
            if offset < m - offset:
                for j in range(offset, n - offset):
                    rez.append(matrix[offset][j])
            if offset < n - offset:
                for i in range(offset + 1, m - 1 - offset):
                    rez.append(matrix[i][n - 1 - offset])
            if offset < m - 1 - offset:
                for j in range(n - 1 - offset, -1 + offset, -1):
                    rez.append(matrix[m - 1 - offset][j])
            if offset < n - 1 - offset:
                for i in range(m - 2 - offset, 0 + offset, -1):
                    rez.append(matrix[i][offset])

            offset += 1

        return rez


if __name__ == "__main__":
    s = Solution()

    rez = s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # [1,2,3,6,9,8,7,4,5]
    print(rez)

    rez = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(rez)

    rez = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
                         [13, 14, 15, 16]])  # [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    print(rez)

    rez = s.spiralOrder([[6, 9, 7]])  # [6, 9, 7]
    print(rez)

    rez = s.spiralOrder([[7], [9], [6]])  # [7, 9, 6]
    print(rez)

    rez = s.spiralOrder([[2, 5, 8], [4, 0, -1]])  # [2,5,8,-1,0,4]
    print(rez)

    rez = s.spiralOrder([[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19],
                         [10, 20]])  # [1,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2]
    print(rez)
