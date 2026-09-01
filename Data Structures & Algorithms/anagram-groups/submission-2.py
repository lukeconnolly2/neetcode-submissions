class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            letter_counts = [0] * 26
            for l in s:
                index = ord(l) - ord('a')
                letter_counts[index] = letter_counts[index] + 1
            
            key = tuple(letter_counts)
            if key not in groups.keys():
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())