# '''

# Given a binary array, in-place sort it in linear time and constant space. The output should contain all zeroes, followed by all ones.

# Input : [1, 0, 1, 0, 1, 0, 0, 1]
# Output: [0, 0, 0, 0, 1, 1, 1, 1]

# Input : [1, 1]
# Output: [1, 1]

# '''

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> None:
        # Initialize pointers for three sections: 0s, 1s, and unexplored
        start = 0
        end = len(nums) - 1
        
        # Iterate through the array
        current = 0
        while current <= end:
            if nums[current] == 0:
                # Swap with the element at the start pointer
                nums[current], nums[start] = nums[start], nums[current]
                # Move the start pointer forward
                start += 1
                # Move the current pointer forward
                current += 1
            elif nums[current] == 1:
                # Move the current pointer forward
                current += 1
            else:
                # Swap with the element at the end pointer
                nums[current], nums[end] = nums[end], nums[current]
                # Move the end pointer backward
                end -= 1

# Example usage:
solution = Solution()
nums1 = [1, 0, 1, 0, 1, 0, 0, 1]
solution.sortArray(nums1)
print(nums1)  # Output: [0, 0, 0, 0, 1, 1, 1, 1]

nums2 = [2, 1]
solution.sortArray(nums2)
print(nums2)  # Output: [1, 1]
