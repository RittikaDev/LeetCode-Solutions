from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n // 2:
                return num



# EXAMPLE USAGE
if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1,1,1,1,2,2]
    result = sol.majorityElement(nums)
    print(result)

