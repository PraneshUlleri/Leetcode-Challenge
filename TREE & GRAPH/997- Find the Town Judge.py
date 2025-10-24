class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)
        
        for a, b in trust:
            count[a] -= 1  # a trusts someone
            count[b] += 1  # b is trusted by someone
        print(count)
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        return -1
