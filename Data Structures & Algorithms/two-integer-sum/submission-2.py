class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i in range(len(nums)): 
            currNum = nums[i]
            if currNum in targets.keys():
                return [targets[currNum], i]
            
            t = target - currNum
            targets[t] = i
            
        return [-1, -1]