import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Create a min heap with first k elements
        heap = nums[:k]
        heapq.heapify(heap)
        
        # Step 2: For remaining numbers
        for num in nums[k:]:
            if num > heap[0]:  # if current num is bigger than smallest in heap
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        # Step 3: root of heap is kth largest
        return heap[0]
