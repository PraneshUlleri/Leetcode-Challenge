class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        for i in range(0,len(nums)):
            nums[i]+=s
            s=nums[i]
        return (nums)