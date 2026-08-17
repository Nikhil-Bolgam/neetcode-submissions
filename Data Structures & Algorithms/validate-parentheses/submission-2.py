class Solution:
    
    
    def isValid(self, s: str) -> bool:
        pairs = {")":"(" ,"]":"[", "}":"{"}
        seen = []

        for literal in s:             

            if literal in pairs.values():
                seen.append(literal)
            
            elif literal in pairs.keys():
                if seen and seen[-1]==pairs[literal]:
                    seen.pop()
                else:
                    return False

        if seen == []:
            return True
        else : return False

