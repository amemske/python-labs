from typing import List, Tuple #type hinting

#self is the first argument and represents the instance of the class
class Solution:
    def findPair(self, nums: List[int], target: int) -> List[Tuple[int]]:
        pairs = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    pairs.append((nums[i], nums[j]))
                
        return pairs

solution = Solution()

nums1 = [8,7,2,5,3,1]
target1 = 10
output1 = solution.findPair(nums1, target1)
print(output1)