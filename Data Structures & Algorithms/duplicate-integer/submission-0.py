class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         one = []
         for i in nums:
            if i in one:
                return True
            else: 
                one.append(i)

         return False
        
            