class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arrodd=[]
        arreven=[]
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                arreven.append(nums[i])
            else: 
                arrodd.append(nums[i])
        finalarr = arreven + arrodd
        return finalarr

arrGiven = [3,1,2,4]
print(Solution().sortArrayByParity(arrGiven))