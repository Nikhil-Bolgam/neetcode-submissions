class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = []
        mapping = {")":"(" ,"]":"[", "}":"{"}

        for bracket in s:

            if bracket in mapping.values():
                brackets.append(bracket)
            elif bracket in mapping:
                if brackets and brackets[-1]== mapping[bracket]:
                    brackets.pop()
                else: return False
                    
        return not brackets