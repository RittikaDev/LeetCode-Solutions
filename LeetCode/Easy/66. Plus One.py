from typing import List

# range(start, stop, step) =>
# START: WHERE TO BEGIN (INCLUSIVE)
# STOP: WHERE TO END (EXCLUSIVE) => WILL STOP BEFORE THE SET INDEX, THAT IS WHY TO STOP AT 0, WE MENTIONED -1
# STEP: THE AMOUNT TO INCREASE OR DECREASE BY

class Solution(object):
    def plusOne(self, digits:List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):  # START FROM THE LAST DIGIT => range(start, stop, step)
            if digits[i] < 9:
                digits[i] += 1
                return digits  # NO CARRY NEEDED
            digits[i] = 0  # SET TO 0 AND CARRY TO NEXT LOOP ITERATION

            # IF ALL DIGITS WERE 9 (E.G., [9,9,9]), WE GET [0,0,0] HERE
        return [1] + digits # BECOMES [1, 0, 0, 0] => [1] IS NOT THE INDEX, IS THE LEADING 1 DIGIT OF THE ARRAY



if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([4,3,2,1]))
