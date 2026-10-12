class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        for i in range(len(nums)):
            leftSum += nums[i]
            if leftSum == totalSum:
                return i
                break
            totalSum -= nums[i]
        return -1

x = [1,7,3,6,5,6]
result = Solution().pivotIndex(x)
if result != -1:
    print("the index is ", result)
else:
    print("0")  