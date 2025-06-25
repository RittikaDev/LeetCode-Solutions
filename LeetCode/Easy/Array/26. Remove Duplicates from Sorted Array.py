from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length - 1]:
                nums[length] = nums[i]
                length += 1

        return length



if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    length = sol.removeDuplicates(nums)
    print("Length:", length)
    print("Modified nums:", nums[:length])
