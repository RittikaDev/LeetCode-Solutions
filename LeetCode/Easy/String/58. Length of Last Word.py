class Solution(object):
    def lengthOfLastWord(self, s:str) -> int:
       return len(s.split()[-1])


if __name__ == "__main__":
    sol = Solution()
    sentence = "   fly me   to   the moon  "
    result = sol.lengthOfLastWord(sentence)
    print(result)

# BEATS 100% USERS IN LEETCODE