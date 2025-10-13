class Solution:
    def maxDepth(self, s: str) -> int:
        maxim =0
        count =0
        for i in s:
            if i =="(":
                count +=1
            elif i ==")":
                count -=1

            if maxim < count :
                maxim = count

        return maxim
            
