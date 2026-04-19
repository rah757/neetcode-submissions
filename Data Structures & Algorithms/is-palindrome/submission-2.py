class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left<right and not s[left].isalnum():
                left+=1
            while left<right and not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False 
            left +=1 
            right -=1 
        return True 








        # string = ''.join(c.lower() for c in s if c.isalnum())
        # for i in range (len(string)//2):
        #     if string[i] != string[len(string)-1-i]:
        #         return False
        # return True
