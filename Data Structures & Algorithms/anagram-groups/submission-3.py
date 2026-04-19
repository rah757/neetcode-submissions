class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        allItems={}
        for item in strs:
            sorted_word = ''.join(sorted(item))
            if sorted_word not in allItems:
                allItems[sorted_word] = [item]
            else:
                allItems[sorted_word].append(item)
        return allItems.values()