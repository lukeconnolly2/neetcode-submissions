class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        starts = []

        for n in nums:
            if n - 1 in numsSet:
                continue
            starts.append(n)

        print(starts)
        longest = 0

        for s in starts:
            currLen = 1
            while s + 1 in numsSet: 
                currLen += 1
                s += 1
            
            if currLen > longest:
                longest = currLen

        return longest 
                

