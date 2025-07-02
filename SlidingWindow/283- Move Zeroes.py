class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeroes= nums.count(0)
        # print (zeroes)
        j=0
        for i in range (0, len (nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
            if i> (len(nums)-1)-zeroes:
                nums[i]=0