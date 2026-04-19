class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        d = {}
        heap=[]
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for key, value in d.items():
            heapq.heappush(heap,(value, key))
            if len(heap)>k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
