from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[List[int]]:
        arr = []

        for row in range(rowIndex+1):
            temp = []

            for col in range(row + 1):
                if col == 0 or col == row:
                    temp.append(1)
                else:
                    val = arr[-1][col - 1] + arr[-1][col]
                    temp.append(val)

            arr.append(temp)

        return arr[rowIndex]



# EXAMPLE USAGE
if __name__ == "__main__":
    sol = Solution()
    rowIndex = 3
    result = sol.getRow(rowIndex)
    print(result)
