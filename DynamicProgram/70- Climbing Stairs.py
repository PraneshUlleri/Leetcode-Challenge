class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        stair= [1,2]
        
        for i in range (3, n+1):
            stair.append( stair[-1]+stair[-2])
        
        return stair[-1]