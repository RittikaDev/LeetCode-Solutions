class Solution(object):
    def romanToInt(self, s: str) -> int :
        symbolVal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }


        returnVal = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and symbolVal[s[i]] < symbolVal[s[i + 1]]:
                returnVal += symbolVal[s[i + 1]] - symbolVal[s[i]]
                i += 2
            else:
                returnVal += symbolVal[s[i]]
                i += 1

        return returnVal


if __name__ == "__main__":
    sol = Solution()
    s = "MCMXCIV"
    result = sol.romanToInt(s)
    print(result)


# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.