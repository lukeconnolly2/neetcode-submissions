class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]

        totalWater = 0

        for i in range(1, len(height), 1):
            prefix[i] = max(prefix[i-1], height[i-1])

        for i in reversed(range(0, len(height) - 1)):
            suffix[i] = max(height[i+1], suffix[i+1])

        for i in range(len(height)):
            h = min(prefix[i], suffix[i]) - height[i]
            if h > 0:
                totalWater += h 
        
        return totalWater
                
        
            

