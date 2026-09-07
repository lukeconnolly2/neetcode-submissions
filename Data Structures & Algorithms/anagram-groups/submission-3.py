class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)

        for s in strs:
            character_array = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                character_array[i] = character_array[i] + 1
            
            groups[tuple(character_array)].append(s)

        res = [x for x in groups.values()]

        return res

        