class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        
        left = 0 
        longest_substring = 0

        for right in range(len(s)):
            while s[right] in sub_string:
                sub_string.remove(s[left])
                left+=1
            sub_string.add(s[right])
            
            longest_substring = max(longest_substring,right - left + 1)

        return longest_substring

