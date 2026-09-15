class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        for i in range(len(height) -1):
            prefix[i+1] = max(prefix[i], height[i])

        for i in reversed(range(1, len(height))):
            suffix[i-1] = max(suffix[i], height[i])

        totalTrappedWater = 0

        for i, currH in enumerate(height):
            maxh = min(prefix[i], suffix[i])
            trappedWater = maxh - currH
            if trappedWater > 0:
                totalTrappedWater += trappedWater
        
        return totalTrappedWater