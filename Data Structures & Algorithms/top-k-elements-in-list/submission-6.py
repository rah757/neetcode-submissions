class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tot = {}
        op = []
        for i in nums:
            tot[i] = tot.get(i,0)+1
        while k:
            max_key = max(tot, key=tot.get)
            op.append(max_key)
            tot[max_key] = 0
            k-=1

        return op