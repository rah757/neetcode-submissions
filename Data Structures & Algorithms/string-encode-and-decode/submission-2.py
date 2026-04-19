class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        final = []
        while s!='':
            hashPosition=0
            for i in s:
                if i != '#':
                    hashPosition += 1
                else:
                    break
            length = int(s[:hashPosition])
            temp = ''
            temp = s[hashPosition+1:length+hashPosition+1]
            s = s[length+hashPosition+1:]
            final.append(temp)
        return final