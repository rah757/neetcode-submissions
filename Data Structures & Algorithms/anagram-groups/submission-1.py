class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = {}

        for word in strs:
            sorted_word = tuple(sorted(word))

            if sorted_word in answer_dict:
                answer_dict[sorted_word].append(word)
            else: 
                answer_dict[sorted_word] = [word]
                
        return list(answer_dict.values())