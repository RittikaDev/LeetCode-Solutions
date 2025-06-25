from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target:int):

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 6]
    index = sol.searchInsert(nums, 7)
    print("Index", index)


