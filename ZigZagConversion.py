# The string "PAYPALISHIRING" is written in a zigzag pattern 
# on a given number of rows like this: (you may want to display this 
# pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"


class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        row = 0
        length = len(s)
        arr = [[] for i  in range(n)]
        down = True
        
        for i in range(length):
            arr[row].append(s[i])
            
            if row == n - 1:
                down = False
            elif row == 0:
                down = True
            
            if down:
                row += 1
            else:
                row -= 1
        
        flat_list = [item for sublist in arr for item in sublist]
        return "".join(flat_list)
