﻿class Solution(object):
    def titleToNumber(self, columnTitle: str):
        excelColumn = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
             "J": 10,
             "K": 11,
             "L": 12,
             "M": 13,
             "N": 14,
             "O": 15,
             "P": 16,
             "Q": 17,
             "R": 18,
             "S": 19,
             "T": 20,
             "U": 21,
             "V": 22,
             "W": 23,
             "X": 24,
             "Y": 25,
             "Z": 26,
        }

        array = 0
        for i, val in enumerate(columnTitle[::-1]):
            array = array + (excelColumn[val] * (26 ** i))

        return array




if __name__ == "__main__":
    sol = Solution()
    number = "ZY"
    result = sol.titleToNumber(number)
    print(result)
