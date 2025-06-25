from typing import List


class Solution(object):
    def removeElement(self, nums: List[int], val:int) -> int:

        i = 0
        length = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                length += 1

        return length



if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3,2,3]
    length = sol.removeElement(nums, 3)
    print("Length:", length)
    print("Modified nums:", nums[:length])