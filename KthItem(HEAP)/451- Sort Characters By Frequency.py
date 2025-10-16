import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        max_heap = [(-freq, char) for char, freq in dic.items()]
        heapq.heapify(max_heap)

        res = []
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char * (-freq))

        return ''.join(res)
