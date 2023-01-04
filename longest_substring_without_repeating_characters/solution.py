class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_idx = 0
        max_len = 0

        seen_chars = {}

        for i, c in enumerate(s):
            if c in seen_chars and seen_chars[c] >= current_idx:
                current_len = i - current_idx

                if current_len > max_len:
                    max_len = current_len

                current_idx = seen_chars[c] + 1
                current_len = i - seen_chars[c]
                seen_chars[c] = i
            else:
                seen_chars[c] = i

        current_len = len(s) - current_idx

        if current_len > max_len:
            max_len = current_len

        return max_len

