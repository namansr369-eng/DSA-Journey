#151 Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        words.reverse()
        reversed_string = " ".join(words)

        return  reversed_string
    
    