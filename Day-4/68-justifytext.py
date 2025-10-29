# Given an array of strings words and a width maxWidth, format the text such that
#  each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line does not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.


class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        n = len(words)
        i = 0  # Pointer to the first word of the current line

        while i < n:
            # --- PHASE 1: Determine which words fit on the current line ---
            
            j = i + 1  # Pointer to the word *after* the current line's words
            line_length = len(words[i])  # Starts with the first word's length
            
            # Continue adding words as long as they fit (length + word + 1 space)
            while j < n and line_length + len(words[j]) + 1 <= maxWidth:
                line_length += len(words[j]) + 1  # +1 for the mandatory space
                j += 1
            
            # Words for the current line are from index i to j-1
            current_words = words[i:j]
            num_words = len(current_words)
            
            # ----------------- PHASE 2: Justification Logic -----------------
            
            # Calculate total length of characters (excluding spaces)
            words_len = sum(len(w) for w in current_words)
            
            # Calculate the total number of spaces we need to distribute
            total_spaces = maxWidth - words_len
            
            # Determine if this is the last line or if it has only one word
            is_last_line = (j == n)
            
            # 1. CASE: Last Line or Single Word Line
            if is_last_line or num_words == 1:
                # Left-justify: Put one space between words and pad the rest on the right.
                line = " ".join(current_words)
                
                # Add trailing spaces to meet maxWidth
                line += " " * (maxWidth - len(line))
                
            # 2. CASE: Standard Justified Line (Multiple words, not the last line)
            else:
                num_gaps = num_words - 1
                
                # Calculate base spaces: the minimum number of spaces for every gap
                base_spaces = total_spaces // num_gaps
                
                # Calculate extra spaces: these are distributed one by one to the first 'extra' gaps
                extra_spaces = total_spaces % num_gaps
                
                line = ""
                for k in range(num_words):
                    line += current_words[k]
                    
                    # Do not add spaces after the last word
                    if k < num_words - 1:
                        # Add the base number of spaces
                        line += " " * base_spaces
                        
                        # Add one extra space to the first 'extra_spaces' gaps
                        if k < extra_spaces:
                            line += " "

            result: list[str] = []  # just for the type hint
            result.append(line)
            
            # Move the main pointer 'i' to the start of the next line
            i = j
            
        return result