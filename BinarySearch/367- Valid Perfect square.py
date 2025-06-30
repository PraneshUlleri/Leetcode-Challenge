

import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=1,num//2
        if num==1:
            return True
        while(l<r):
            mid= math.ceil((l+r)/2 )
            if mid*mid > num:
                r= mid -1
            elif mid*mid <num:
                l=mid
            elif mid*mid == num:
                return True
            else:
                return False
        return False