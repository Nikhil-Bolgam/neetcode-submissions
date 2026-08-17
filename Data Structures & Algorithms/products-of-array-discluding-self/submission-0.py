class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #brute force solution 
        final_output = [1] * len(nums)
        
        for  index, num in enumerate(nums):
            new_list = nums.copy()
            new_list.pop(index)
            
            for mul in new_list:
                final_output[index] = final_output[index]*mul
        return  final_output


# This is a brute force solution 
# Learnings
# 1. list.copy() method to copy contents of the list 
# 2. intialize list with 1 for the length of input list


