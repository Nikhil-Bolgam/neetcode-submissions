# simplest solution is to use a non-ascii character as delimiter

class Solution:

    def encode(self, strs: List[str]) -> str:

        final_string = ""
        
        for text in strs:
            final_string += text + "§"
        return final_string


    def decode(self, s: str) -> List[str]:
        
        strs = s.split('§')
        
        strs.pop(-1)
        return strs
