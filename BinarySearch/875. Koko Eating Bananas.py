class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            m = (l + r) // 2
            total = 0
            for pile in piles:
                total += (pile + m - 1) // m  # faster ceiling division
            
            if total <= h:
                r = m  # can try slower
            else:
                l = m + 1  # too slow, go faster
        
        return l
