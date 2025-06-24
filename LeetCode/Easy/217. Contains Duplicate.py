from itertools import count
from typing import List


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

if __name__ == "__main__":
    sol = Solution()
    nums = [0,4,5,0,3,6]
    result = sol.containsDuplicate(nums)
    print(result)