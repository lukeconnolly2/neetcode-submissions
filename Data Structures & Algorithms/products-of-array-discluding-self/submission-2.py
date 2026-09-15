class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums) - 1):
            prefix[i+1] = prefix[i] * nums[i]

        for i in reversed(range(1, len(nums))):
            suffix[i - 1] = suffix[i] * nums[i]


        res = []

        for p, s in zip(prefix, suffix):
            res.append(p * s)

        return res