class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_tracker = {}

        for num in nums:
            count_tracker[num] = 1 + count_tracker.get(num,0)


        sorted_counts = sorted(count_tracker.items(), key=lambda item: item[1],reverse=True)

        return list(dict(sorted_counts[:k]).keys())


# solution using O(n + m logn)