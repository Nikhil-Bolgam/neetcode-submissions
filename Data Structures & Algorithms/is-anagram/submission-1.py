class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        # Base case to check if the length are equal first 
        # if length are not are equal they are not valid anagrams
        if len(s)!= len(t):
            return False
        
        # Second level we will check the occurence of characters 
        # if occurence of chars in string 1 is not equal to string 2 then they are not valid anagrams
        freq_s = {}
        freq_t = {}

        for c in s:
            freq_s[c] = freq_s.get(c,0) + 1
        
        for c in t: 
            freq_t[c] = freq_t.get(c,0) + 1 

        for c in freq_s:
            if freq_s[c] != freq_t.get(c,0):
                return False
        
        return True



        