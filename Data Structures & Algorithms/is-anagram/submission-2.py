class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimization with a constraint of strings contain only lower case characters 
        if len(s)!=len(t):
            return False

        # define a 26 charcater array of dictionary 

        count = [0] * 26 

        for char_s,char_t in zip(s,t):
            
            # increment when char is in s 
            count[ord(char_s) - ord('a')]+= 1

            #decrement when char is in t 
            count[ord(char_t) - ord('a')] -= 1
        
        for val in count :
            if val !=0:
                return False
        
        return True