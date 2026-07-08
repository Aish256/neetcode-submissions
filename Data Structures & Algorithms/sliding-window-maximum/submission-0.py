from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # remove from front if outside window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # remove from back if smaller than current
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # add to result once first window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result