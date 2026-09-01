class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        for s_letter in s: 
            s_counts[s_letter] = s_counts.get(s_letter, 0) + 1

        t_counts = {}
        for t_letter in t: 
            t_counts[t_letter] = t_counts.get(t_letter, 0) + 1

        return s_counts == t_counts