# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def custom_sort(log):
            idt, content = log.split(" ", 1)
            if content[0].isalpha():
                return (0, content, idt)
            return (1, None, None)
        
        return sorted(logs, key=custom_sort)