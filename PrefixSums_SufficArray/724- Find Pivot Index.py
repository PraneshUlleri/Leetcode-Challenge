class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suml,sumr=0,0
        print (sum(nums[0:2]))
        l=len(nums)
        for i in range(len(nums)):
            if sum(nums[0:i])==sum(nums[i+1:l]):
                return i
        return -1
