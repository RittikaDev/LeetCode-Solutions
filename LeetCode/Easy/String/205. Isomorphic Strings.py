class Solution(object):
    def isIsomorphic(self, s:str, t:str) -> bool:
        isomorphicDict = {}
        used_values = set()
        if len(s) != len(t): return False

        for sIndex, sVal in enumerate(s):
            if sVal not in isomorphicDict:
                if t[sIndex] in used_values:
                    return False
                isomorphicDict[sVal] = t[sIndex]
                used_values.add(t[sIndex])
            elif isomorphicDict[sVal] != t[sIndex]:
                return False

        print(isomorphicDict)
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "egg"
    t = "add"
    result = sol.isIsomorphic(s, t)
    print(result)

# BEATS 96.06% USERS IN LEETCODE