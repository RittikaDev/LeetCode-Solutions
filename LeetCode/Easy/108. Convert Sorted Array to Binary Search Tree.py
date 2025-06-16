from collections import deque
from typing import List, Optional, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2 # // 2 IS AN INTEGER DIVISION
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid]) # LIST SLICING IN PYTHON. IT MEANS: TAKE ALL ELEMENTS FROM THE BEGINNING OF THE LIST UP TO (BUT NOT INCLUDING) INDEX MID.
        root.right = self.sortedArrayToBST(nums[mid+1:]) # SLICES FROM MID + 1 TO THE END
        return root



# HELPER FUNCTION TO PRINT THE TREE IN PREORDER
def level_order_with_nulls(root):
    if not root:
        return []

    result = []
    queue: deque[Any] = deque([root]) # DEQUE IS A SPECIAL LIST FROM COLLECTIONS THAT MAKES POPPING FROM THE FRONT FAST

    while queue:
        node = queue.popleft()

        if not node:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # TRIM THE TRAILING NONE VALUES
    while result and result[-1] is None:
        result.pop()

    return result



if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    newArray = sol.sortedArrayToBST(nums)
    print("Converted Binary Tree (Preorder):", level_order_with_nulls(newArray))