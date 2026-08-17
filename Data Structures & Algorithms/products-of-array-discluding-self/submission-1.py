class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # optimal solution 
        # prefix suffix method using associative property of multiplication
        # Hint a * (b * c) = b * (a * c)
        # consider 'a' is prefix and 'b * c' as suffix 
        # pattern hint "find except an element or within range"

        output_array = [1] * len(nums)

        # process to store prefix multiplications
        prefix = 1
        
        for i in range(len(nums)):
            
            #store current element index perfix in output array
            output_array[i] = prefix

            # update prefix (prefix * current element in the array) used for next iteration
            prefix *= nums[i]

        # process to store suffix multiplications
        suffix = 1

        for i in range(len(nums) -1, -1, -1):

            # update current element of output array with suffix
            # multiplying output array with current suffix element
            output_array[i] *= suffix 
            
            # update suffix with new value using current element for next iteration
            suffix *= nums[i]


        return output_array


