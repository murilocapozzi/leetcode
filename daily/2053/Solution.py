class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        
        occurrences = {}

        for c in arr:
            if c in occurrences: occurrences[c] += 1
            else: occurrences[c] = 1

        for occ in occurrences:
            if occurrences[occ] == 1: k -= 1
            if k == 0: return occ

        return ""