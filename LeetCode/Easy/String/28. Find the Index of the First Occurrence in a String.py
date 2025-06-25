class Solution(object):
    def strStr(self, haystack:str, needle:str) -> int:
        if not needle:
            return 0

        len_hay, len_ndl = len(haystack), len(needle)

        for i in range(len_hay - len_ndl + 1):
            if haystack[i:i + len_ndl] == needle:
                return i

        return -1



if __name__ == "__main__":
    sol = Solution()
    haystack = "leetcode"
    needle = "leeto"
    result = sol.strStr(haystack, needle)
    print(result)


# BEATS 100% USERS IN LEETCODE