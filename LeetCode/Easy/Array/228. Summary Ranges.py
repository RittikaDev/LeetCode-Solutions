from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rType = []
        if not nums:
            return rType

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    rType.append(str(start))
                else:
                    rType.append("{}->{}".format(start, nums[i - 1]))
                start = nums[i]

        if start == nums[-1]:
            rType.append(str(start))
        else:
            rType.append("{}->{}".format(start, nums[-1]))

        return rType


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 2, 4, 5, 7]
    result = sol.summaryRanges(nums)
    print(result)


# BEATS 100% USERS IN LEETCODE