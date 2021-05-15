#Sliding window approach


# window_size - repating_character = non_repeating_character
# if non_repeating_character > k   --> constraint violation  --> decrease window size from left

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        char_map = defaultdict(int)     # dict with default value 0 for new key entry
        max_freq_char = 0
        
        for right in range(len(s)):
            curr_char = s[right]
            char_map[curr_char] += 1

            window_size = right-left+1

            max_freq_char = max(max_freq_char, char_map[curr_char])

            if window_size - max_freq_char > k:
                # constraint violation...so decrease window size from left
                char_map[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans