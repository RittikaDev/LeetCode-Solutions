from typing import List


class Solution(object):
    def containsNearbyDuplicate(self, nums:List[int], k:int) -> bool:
        lookup = {}

        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            elif i - lookup[num] <= k:
                return True
            lookup[num] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    result = sol.containsNearbyDuplicate(nums, k)
    print(result)