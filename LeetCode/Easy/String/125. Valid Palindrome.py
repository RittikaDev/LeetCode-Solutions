import re


class Solution(object):
    def isPalindrome(self, s:str) -> bool:
        cleanText = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        half = len(cleanText) // 2

        if half == 0:
            return True

        firstHalf = cleanText[:half]
        secondHalf = cleanText[-half:]

        if firstHalf == secondHalf[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    text = "a"
    result = sol.isPalindrome(text)
    print(result)