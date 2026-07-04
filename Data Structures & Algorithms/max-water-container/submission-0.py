class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0 
        right = len(heights)-1
        while left < right :
            water = min(heights[left],heights[right])*(right-left)
            if heights[left]<heights[right] :
                left += 1
            else:
                right -= 1
            result = max(result,water)        
        return result
    