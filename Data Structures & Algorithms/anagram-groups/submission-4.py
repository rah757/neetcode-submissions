class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        for word in strs:
            key = [0] *26
            for i in word:
                val = ord(i) - ord('a')
                key[val] +=1
            theKey = tuple(key)
            if theKey not in hashset:
                hashset[theKey] = []
            hashset[theKey].append(word)
        return list(hashset.values())