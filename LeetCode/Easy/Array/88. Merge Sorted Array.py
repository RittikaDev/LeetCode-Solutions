from typing import List


class Solution(object):
    def merge(self, nums1:List[int], m:int, nums2:List[int], n:int) -> None:
        # START FILLING NUMS1 FROM THE END
        i = m - 1  # LAST INDEX OF ACTUAL NUMS1 DATA
        j = n - 1  # LAST INDEX OF NUMS2
        k = m + n - 1  # LAST INDEX OF NUMS1 (PLACEHOLDER SPACE INCLUDED)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # IF NUMS2 STILL HAS ELEMENTS LEFT
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    newArray = sol.merge(nums1, 3, nums2, n)
    print("Modified nums:", newArray)