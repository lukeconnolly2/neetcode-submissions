class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        TARGET = 0
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i-1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1
            twoSumTarget = TARGET - nums[i]
            while l < r: 
                twoSum = nums[l] + nums[r]
                if twoSum < twoSumTarget:
                    l += 1
                elif twoSum > twoSumTarget:
                    r -= 1 
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1


            
        return res

