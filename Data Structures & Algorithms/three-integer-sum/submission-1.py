class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSumTarget = 0
        result = []
        nums.sort()

        for i, e in enumerate(nums):
            if i > 0 and nums[i-1] == e:
                continue

            l, r = i+1, len(nums) - 1
            twoSumTarget = threeSumTarget - e
            while l < r:
                if nums[l] + nums[r] < twoSumTarget:
                    l += 1
                elif nums[l] + nums[r] > twoSumTarget:
                    r -= 1
                else: 
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result