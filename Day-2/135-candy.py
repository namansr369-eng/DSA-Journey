# 135. Candy
# Hard

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        
        # 1. Initialize the candies array: Every child gets at least 1 candy.
        candies = [1] * n
        
        # 2. FIRST PASS: Left-to-Right (Satisfy Left Neighbor Condition)
        for i in range(1, n):
            # If current child's rating is higher than the left neighbor
            if ratings[i] > ratings[i - 1]:
                # Give them 1 more candy than the left neighbor
                candies[i] = candies[i - 1] + 1
                
        # 3. SECOND PASS: Right-to-Left (Satisfy Right Neighbor Condition)
        # We start from the second-to-last child down to the first
        for i in range(n - 2, -1, -1):
            # If current child's rating is higher than the right neighbor
            if ratings[i] > ratings[i + 1]:
                # We update the candy count only if the new requirement (right neighbor's + 1) 
                # is greater than the current count (which satisfied the left neighbor).
                candies[i] = max(candies[i], candies[i + 1] + 1)
                
        # 4. Final Result: The sum of all candies
        return sum(candies)  
            