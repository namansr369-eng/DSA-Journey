# 238. Product of Array Except Self
# Medium
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List  # Import List for type hinting
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 1. Initialize the answer array and calculate prefix products.
        # This array will first store all the prefix products.
        answer = [0] * n
        answer[0] = 1
        
        # Calculate prefix products: answer[i] = product of nums[0]...nums[i-1]
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
            
        # 2. Calculate suffix products and the final result.
        # Use a single variable 'suffix_product' to track the running product from the right.
        suffix_product = 1
        
        # Iterate backward from the second-to-last element
        for i in range(n - 1, -1, -1):
            # answer[i] currently holds the prefix product.
            # Multiply it by the accumulated suffix product (product of nums[i+1]...nums[n-1]).
            answer[i] = answer[i] * suffix_product
            
            # Update the running suffix product for the next iteration (i-1)
            suffix_product = suffix_product * nums[i]
            
        return answer