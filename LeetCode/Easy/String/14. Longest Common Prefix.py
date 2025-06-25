from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs:List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            current = strs[i]
            match_len = 0
            for j in range(min(len(prefix), len(current))):
                if prefix[j] == current[j]:
                    match_len += 1
                else:
                    break
            prefix = prefix[:match_len]
            if prefix == "":
                break

        return prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    result = sol.longestCommonPrefix(strs)
    print(result)