class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_ref = {}
        
        
        for idx, num in enumerate(nums):
            

            difference = target - num

            if difference in nums_ref:
                return [nums_ref[difference],idx]
            nums_ref[num] = idx
