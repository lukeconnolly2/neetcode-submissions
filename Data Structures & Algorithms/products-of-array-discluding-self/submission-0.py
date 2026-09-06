class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixFactor = [1 for _ in range(len(nums))]
        suffixFactor = [1 for _ in range(len(nums))]

        res = []

        for i in range(len(nums) - 1):
            prefixFactor[i + 1] = nums[i] * prefixFactor[i]
        
        for i in reversed(range(len(nums))):
            if i == 0:
                #Prevent underflow of the array
                break

            suffixFactor[i - 1] = nums[i] * suffixFactor[i]

        for i in range(len(prefixFactor)):
            res.append(prefixFactor[i] * suffixFactor[i])

        return res