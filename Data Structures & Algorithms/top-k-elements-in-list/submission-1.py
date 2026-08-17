class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_tracker = {}
        frequency_tracker = [[] for i in range(len(nums)+1)]

        for num in nums:
            count_tracker[num] = 1 + count_tracker.get(num,0)
        
        for n,c in count_tracker.items():
            frequency_tracker[c].append(n)
        
        res = []
        for i in range(len(frequency_tracker)-1, 0 ,-1):
            if frequency_tracker[i]!=[] and len(res)<k:
                res.extend(frequency_tracker[i])
            elif len(res)==k:
                break

        return res