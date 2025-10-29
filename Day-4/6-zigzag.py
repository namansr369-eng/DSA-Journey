# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows <= 1 or len(s) <= numRows:
            return s
        
        rows: list[list[str]] = [[] for _ in range(numRows)]   # in latest version of the python -- no need to import the types anymore

        current_row = 0
        direction = 1
        for char in s:
            rows[current_row].append(char) 

            if current_row == 0:
                direction = 1
            if current_row == numRows - 1:
                direction = -1
            

            current_row += direction

        return "".join("".join(row) for row in rows)