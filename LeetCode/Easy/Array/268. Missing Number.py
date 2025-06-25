from typing import List


class Solution(object):
    def missingNumber(self, nums:List[int]) -> int :
          sumVal = 0
          rValue = 0

          for i in range(0, len(nums)):
              sumVal = sumVal + nums[i]
              orgSum = len(nums) * (len(nums) + 1) // 2
              if orgSum > sumVal:
                 rValue = orgSum - sumVal
              else:
                  rValue = 0

          return rValue


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2]
    result = sol.missingNumber(nums)
    print(result)