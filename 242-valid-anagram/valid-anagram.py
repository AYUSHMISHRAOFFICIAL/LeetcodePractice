class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charCounts = {}
        for char in s:
            charCounts[char] = charCounts.get(char,0)+1

        for char in t:
            if char not in charCounts or charCounts[char] == 0:
                return False
            charCounts[char] -= 1
        
        return True

s = "anagram"
t= "nagaram"
print(Solution().isAnagram(s,t))
        