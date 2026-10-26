class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # lookup = {}

        # # create look up dictionary
        # for idx, num in enumerate(nums): 
        #     lookup[num] = idx
        
        
        # result = set()
        # for idx1, first in enumerate(nums): 
        #     for idx2, second in enumerate(nums):
        #         third = -(first + second)

        #         if third in lookup:
        #             idx3 = lookup[third]
        #             result.add({idx1,idx2,idx3})
        
        # return list(result)

        # The above solution doesn't work coz in python the set is not hashable within a set
        # brute force would be to write 3 nested loops 
        
        # we will be using sorted in place array with two pointer approach
        res = []
        nums.sort() 


        for idx, a in enumerate(nums):

            # skip iteration if next two consective elements are same
            if idx > 0 and a == nums[idx - 1]:
                continue

            left = idx + 1 
            right = len(nums) - 1


            while left < right: 

                b = nums[left]
                c = nums[right]
                
                if a + b + c > 0 :
                    right -=1

                elif a + b + c < 0 :
                    left +=1

                else:
                    res.append([a,b,c])
                    left +=1
                    right -=1

                    # skip if two consecutive elements are same from left 
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    
                    # skip if two consecutive elements are same from right 
                    while  right > left and nums[right] == nums [right+1] and right < len(nums)-1:
                        right-=1
        return res
                    














