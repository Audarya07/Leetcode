from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        new_arr = Counter(arr)
        return len(new_arr) == len(set(new_arr.values()))