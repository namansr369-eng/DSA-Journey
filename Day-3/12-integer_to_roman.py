class Solution:
    def intToRoman(self, num: int) -> str:
        sets_list = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"), 
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        returned_roman = ""
        for integer, roman in sets_list:
            if num >= integer:
                length = num // integer
                returned_roman += roman * length
                num = num % integer

        return returned_roman
        