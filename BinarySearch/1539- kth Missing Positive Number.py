class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ind=0
        i=1
        smallest=0
        while(k>0):
            if (ind==len(arr)):
                break
            if (i!=arr[ind]):
                k-=1
                i+=1
            else:
                i=i+1
                ind+=1
        if k>0:
            return i+k-1
        return i-1

            
