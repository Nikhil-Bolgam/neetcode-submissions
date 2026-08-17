class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # create a set of nums for O(1) look up for both num - 1 and num + 1 
        nums_set = set(nums)

        # initialize longest length to zero        
        longest_length = 0
        
        for num in nums:
            
            # check and adjust start of the sequence based on num - 1 in nums_set
            if (num - 1) not in nums_set:
                current_length = 0
            
                # update current length if num + 1 in nums_set and update current_num to num
                while(num + current_length) in nums_set:
                    current_length+=1 

                longest_length = max(longest_length,current_length)
        return longest_length

            
            
            
