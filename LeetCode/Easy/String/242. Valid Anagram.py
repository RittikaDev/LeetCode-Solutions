class Solution(object):
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t): return False

        for sIndex, sVal in enumerate(s):
            if sIndex == len(s)-1:
               if s[sIndex] == t:
                   return True
               else: return False
            for tIndex, tVal in enumerate(t):
                if sVal == tVal:
                    t = t[:tIndex] + t[tIndex+1:]
                    break

        return True


if __name__ == "__main__":
    sol = Solution()
    s = "ac"
    t = "bb"
    result = sol.isAnagram(s, t)
    print(result)