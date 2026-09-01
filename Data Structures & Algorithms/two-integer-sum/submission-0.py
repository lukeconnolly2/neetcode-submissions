class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for index in range(len(nums)): 
            if nums[index] in differences.keys():
                return [differences[nums[index]], index]

            diff = target - nums[index]
            differences[diff] = index