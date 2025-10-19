class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]

        for i in range(1, len(nums)):
            # either start a new subarray or extend current one
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
            print (i, nums[i],curr_sum, max_sum)
        return max_sum
