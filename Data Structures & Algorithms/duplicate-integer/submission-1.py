class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {} # num -> count 

        for num in nums:
            if counts.get(num, 0) == 1:
                return True

            counts[num] = 1

        return False