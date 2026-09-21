class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalString =""
        s=s.lower()
        for ch in s:
            if ch.isalnum() :
                finalString += ch
        reverseString = finalString[::-1]
        if finalString != reverseString:
            return False
        
        return True

x = "A man, a plan, a canal: Panama"
result = Solution().isPalindrome(x)
print(result)

