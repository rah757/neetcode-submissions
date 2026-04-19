class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        output = []
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        # Sort frequencies in ascending order
        sort = sorted(d.keys(), key=d.get)
        
        while k != 0:
            highest = sort.pop(-1)  # Get the highest frequency
            k -= 1
            output.append(highest)
        
        return output

