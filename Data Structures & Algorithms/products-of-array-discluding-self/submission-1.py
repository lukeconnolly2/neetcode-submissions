class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            prefix[i+1] = nums[i] * prefix[i]

        suffix = [1 for _ in range(len(nums))]
        for i in reversed(range(len(nums))):
            if i == 0: 
                continue
            suffix[i-1] = nums[i] * suffix[i] 

        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res