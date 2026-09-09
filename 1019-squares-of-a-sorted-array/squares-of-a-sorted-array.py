class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arrNew = []
        for i in range(len(nums)):
            x= nums[i]
            x=x*x
            arrNew.append(x)
            arrNew.sort()
        return arrNew
arrGiven=[1,2,3,4,5]
result = Solution().sortedSquares(arrGiven)
print(result)    