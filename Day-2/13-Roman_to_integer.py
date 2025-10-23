# 13. Roman to Integer

# Easy
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        # This is our lookup table: it connects Roman characters to their numerical values.
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # This variable will store our final calculated number.
        integer = 0
        
        # This flag helps us skip the smaller character after a subtraction (e.g., skip 'I' in 'IV').
        skip_index = -1
        
        # We process the Roman numeral string BACKWARD, from right to left. 
        # This is the easiest way to catch the tricky subtraction cases (like 'IV' or 'IX').
        # The loop runs from the second-to-last character (len(s)-1) down to the first (0).
        for i in range(len(s)-1, -1, -1):
            
            # CHECK 1: If we previously performed a subtraction, we skip this character
            # because its value was already accounted for in the previous step.
            if i == skip_index:
                continue

            # CHECK 2: Look for a subtraction case. This happens when the current character 
            # is SMALLER than the character just before it (to the left), AND we aren't at the start of the string.
            # Example: When we are on 'V', we look back at 'I'.
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                
                # ACTION 1 (Subtraction): Calculate the combined value and add it to the total.
                # Example: 'V' (5) - 'I' (1) = 4.
                integer += (roman[s[i]] - roman[s[i-1]])
                
                # ACTION 2: Set the flag to skip the smaller character ('I') in the next loop iteration.
                skip_index = i - 1
            else:
                # ACTION 3 (Standard Addition): If it's not a subtraction case, just add the character's value.
                # Example: 'X' is added directly, or the 'V' in 'VII'.
                integer += roman[s[i]]

        # The loop is finished, so the final total is returned.
        return integer