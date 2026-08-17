# Brute force solution using hash map/dict and sorting string
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counter = defaultdict(list)

        for word in strs:
            word_sorted = "".join(sorted(word))
            counter[word_sorted].append(word)

        return list(counter.values())
        

        

