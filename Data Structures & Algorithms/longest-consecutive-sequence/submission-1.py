class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for num in nums:
            if (num - 1) in numSet:
                continue
            currentSequence = 1
            while (num + currentSequence) in numSet:
                currentSequence += 1
            
            if currentSequence > longestSequence:
                longestSequence = currentSequence

        return longestSequence

