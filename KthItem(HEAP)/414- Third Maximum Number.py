class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums=set(nums)
        nums= list (nums)
        nums.sort()
        count =0
        maxi=max(nums)
        print (nums)
        for i in range (3):
            if len(nums)==0:
                break
            x=nums.pop()
            count +=1
        if count ==3:
            return x
        else:
            return maxi


