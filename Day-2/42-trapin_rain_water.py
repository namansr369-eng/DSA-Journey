# 42. Trapping Rain Water
# Hard


# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# ---> this question can be solved either by using two poiners approach or by using dynamic programming with DP arrays to store left max heignts and right max heights for each index.
# ---> but the Two Pointers approach is more optimal in terms of performance as it uses O(1) space complexity compared to O(n) space complexity of DP approach.
# ---> which results in the faster execution time for the two pointers approach.


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 1. Initialize pointers and max wall heights
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        total_water = 0
        
        # 2. Iterate until the pointers meet (single pass)
        while left < right:
            
            # Decide which side to process based on the shorter current wall
            if height[left] < height[right]:
                # We are limited by the left wall's height
                
                if height[left] >= max_left:
                    # Update max_left wall (no water trapped at 'left')
                    max_left = height[left]
                else:
                    # Trapped water = (Max Wall) - (Current Bar Height)
                    total_water += max_left - height[left]
                
                # Move the left pointer inward
                left += 1
                
            else: # height[right] <= height[left]
                # We are limited by the right wall's height
                
                if height[right] >= max_right:
                    # Update max_right wall (no water trapped at 'right')
                    max_right = height[right]
                else:
                    # Trapped water = (Max Wall) - (Current Bar Height)
                    total_water += max_right - height[right]
                    
                # Move the right pointer inward
                right -= 1
                
        return total_water

