class Solution(object):
    def isValid(self, s:str) -> bool :
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        rType = False

        if len(s) % 2 != 0:
            return False
        for i, char in enumerate(s):
            if char in "([{" :
                stack.append(char)
                rType = False
            elif len(stack) > 1 and i == len(s) - 1:
                return False
            elif len(stack) > 0 and stack.pop() == mapping[char]:
                rType = True
            else:
                return False

        return rType


if __name__ == "__main__":
    sol = Solution()
    s = "(()("
    result = sol.isValid(s)
    print(result)


# BEATS 100% USERS IN LEETCODE