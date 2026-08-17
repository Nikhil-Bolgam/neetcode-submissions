# This solution uses the concept character of frequency
# compute character frequency array to create keys of a dictinary
# append to the list matching character frequency key

# key can be tuple or string or integer
# we can utilzie string as shown below


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:

            freq = [0]*26

            for c in s: 

                freq[ord(c) - ord("a")]+=1

            res[str(freq)].append(s)
        
        return list(res.values())