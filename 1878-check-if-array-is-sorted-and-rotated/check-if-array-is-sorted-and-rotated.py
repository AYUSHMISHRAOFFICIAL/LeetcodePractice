class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(0,n):
             if nums[i]>nums[(i+1)%n]:
                count=count+1

        return count<=1

x = [25,26,75,79,95]
if Solution().check(x):
    print("Array is sorted and rotated")
                