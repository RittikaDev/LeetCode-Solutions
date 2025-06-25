from typing import List


class Solution(object):
    def singleNumber(self, nums:List[int]) -> int:
        temp = []

        for num in nums:
            if num not in temp:
                temp.append(num)
            else:
                temp.remove(num)

        return temp[0]


# EXAMPLE USAGE
if __name__ == "__main__":
    sol = Solution()
    nums = [4,1,2,1,2]
    result = sol.singleNumber(nums)
    print(result)