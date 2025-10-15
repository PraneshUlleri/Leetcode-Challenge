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
            

## better way to do this : using heap 

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        arr=[]
        while nums:
            a= heapq.heappop(nums)
            b=heapq.heappop(nums)
            arr.append(b)
            arr.append(a)
        return arr
        