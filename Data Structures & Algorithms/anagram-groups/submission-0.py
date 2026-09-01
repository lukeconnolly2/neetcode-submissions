class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_counts = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            letter_counts[tuple(count)].append(s)
        return list(letter_counts.values())