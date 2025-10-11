class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr=0
        count=0
        for i in range (0,len(nums)):
            if nums[i]==val:
                count+=1
                continue
            else:
                nums[ptr]=nums[i]
                ptr+=1
        for i in range (count ):
            nums.pop()
        print (count)
