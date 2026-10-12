class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n <=0 :
            return 0
        else:
            return math.isqrt(n)
x = 10
print(Solution().bulbSwitch(x))
