class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for number, count in frequencies.items():
            buckets[count].append(number)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
            if len(res) >= k:
                break
        return res