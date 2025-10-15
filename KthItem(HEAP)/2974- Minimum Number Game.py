class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        print (nums)
        arr=[]
        while (len(nums)>0):
            x=nums.pop()
            y=nums.pop()
            arr.append(y)
            arr.append(x)
        return arr
            