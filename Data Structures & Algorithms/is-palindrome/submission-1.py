class Solution:
    def isPalindrome(self, s: str) -> bool:
    
        words = [c.lower() for c in s if c.isalnum()]
        return words == words[::-1]
        
        