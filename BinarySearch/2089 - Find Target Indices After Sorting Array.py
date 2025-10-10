class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ns= (sorted(nums))
        print (ns)
        l=[]

        for i in range (len (nums)):
            if (target == ns[i]):
                l.append(i)
            if (target< ns[i]):
                break
        return l