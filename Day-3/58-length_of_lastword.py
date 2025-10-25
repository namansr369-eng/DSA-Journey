# 58. Length of Last Word

# Easy

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_s = s.strip()
        length = 0
        for i in reversed(cleaned_s):
            if i == " ":
                break

            length += 1
        
        return length
        