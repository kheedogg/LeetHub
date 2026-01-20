class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
    
        # # TLE: O(N^2)
        # max_water = 0
        # for i in range(N):
        #     for j in range(i, N):
        #         h = min(height[i], height[j]) # height of blue area
        #         w = (j-i) # width of blue area

        #         max_water = max(w*h, max_water)

        # TLE: O(N)
        left, right = 0, N-1
        max_water = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            
            water = (right - left) * min(height[left], height[right])
            max_water = max(water, max_water)

        
        return max_water

