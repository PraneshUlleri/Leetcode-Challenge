class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0

        for i in range(1,len(nums)):
            if nums[j]!=nums[i]:
                j+=1
                nums[j] =nums[i]
                
            else: 
                nums[i]=0
        return (j+1)