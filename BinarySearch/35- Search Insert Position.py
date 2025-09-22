class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        r=len(nums)-1
        l=0
        while (l<=r):
            mid= (l+r)//2 
            print (mid)
            if (nums[mid]<target):
                l=mid+1
            elif (nums[mid]>target):
                r=mid-1
            elif (nums[mid]==target):
                return mid
        return l