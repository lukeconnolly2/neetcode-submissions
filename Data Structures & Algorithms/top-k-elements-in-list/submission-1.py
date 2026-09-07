class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums: 
            frequencies[num] = frequencies.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums))]

        for key, v in frequencies.items():
            buckets[v - 1].append(key)

        result = []
        
        for i in reversed(range(len(buckets))):
            result.extend(buckets[i])
            if len(result) >= k:
                return result
                
        
        return result
    