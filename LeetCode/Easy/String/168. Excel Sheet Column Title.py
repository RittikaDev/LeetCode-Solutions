class Solution(object):
    def convertToTitle(self, columnNumber:int) -> str:
        excelColumn = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            26: "Z"
        }

        array = []
        while columnNumber > 0:
            columnNumber, r = divmod(columnNumber - 1, 26)
            array.append(excelColumn[r + 1])

        finalString = ''.join(array[::-1])

        return finalString


if __name__ == "__main__":
    sol = Solution()
    number = 28
    result = sol.convertToTitle(number)
    print(result)



# BEATS 100% USERS IN LEETCODE