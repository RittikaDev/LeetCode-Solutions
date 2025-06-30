class Solution(object):
    def addBinary(self, a:str, b:str) -> str :
        return bin(int(a, 2) + int(b,2))[2:]


if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    result = sol.addBinary(a,b)
    print(result)



# BEATS 100% USERS IN LEETCODE