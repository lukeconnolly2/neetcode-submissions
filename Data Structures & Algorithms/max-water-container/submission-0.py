class Solution:
    def calculateArea(self, left, leftHeight, right, rightHeight):
        w = right - left
        h = min(leftHeight, rightHeight)
        return h * w

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAmount = 0

        while l < r:
            maxAmount = max(maxAmount, self.calculateArea(l, heights[l], r, heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAmount