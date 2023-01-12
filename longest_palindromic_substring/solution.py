### SOLUTION CODE ###

class Solution:
    def longestPalindrome(self, s: str) -> str:
        seen_chars = {}
        intervals = {}

        for i, c in enumerate(s):
            if c in seen_chars:
                targets = seen_chars[c]

                for t in targets:
                    interval = (t, i)
                    interval_len = i - t

                    if interval_len in intervals:
                        intervals[interval_len].add(interval)
                    else:
                        intervals[interval_len] = {interval}

                seen_chars[c].append(i)

            else:
                seen_chars[c] = [i]

        # Sort by interval length
        intervals = dict(sorted(intervals.items()))

        palindrome_len = 1
        palindrome_start = 0
        palindrome_end = 1

        # Explore even palindromes 
        base_intervals = (1, 2)
        
        for base_interval in base_intervals:
            if base_interval in intervals:
                for interval in intervals[base_interval]:
                    interval_len = base_interval

                    interval_start = interval[0]
                    interval_end = interval[1]

                    target_interval = (interval_start - 1, interval_end + 1)
                    target_interval_len = interval_len + 2

                    while target_interval_len in intervals and target_interval in intervals[target_interval_len]:
                        interval_len = target_interval_len

                        interval_start = target_interval[0]
                        interval_end = target_interval[1]

                        target_interval = (interval_start - 1, interval_end + 1)
                        target_interval_len = interval_len + 2

                    if interval_len + 1 > palindrome_len:
                        palindrome_len = interval_len + 1
                        palindrome_start = interval_start
                        palindrome_end = interval_end + 1

        return s[palindrome_start:palindrome_end]

### TESTING CODE ###

import string
import random

def randomize_string(s, chars):
    num_leading_chars = random.randrange(0, 9)
    num_trailing_chars = random.randrange(0, 9)

    leading_chars = ""
    trailing_chars = ""

    for _ in range(num_leading_chars):
        leading_chars += random.choice(chars)

    for _ in range(num_trailing_chars):
        trailing_chars += random.choice(chars)

    return leading_chars + s + trailing_chars

if __name__ == "__main__":
    s = Solution()

    testing_mode = int(input("1 for manual testing, 2 for randomized testing: "))

    if testing_mode == 1:
        input_str = input("Enter a string: ")

        while input_str:
            print(s.longestPalindrome(input_str))
            input_str = input("Enter a string: ")

    elif testing_mode == 2:
        test_cases = [ "abcddd", "abcdddd", "babad", "abcddc", "abcdddc", "abcddddc",
                       "ababababa", "n", "nn", "nnn", "nnnn", "nnnnn", "nnnnnnnnnnnn"
                       "babaababd", "cbbd", "abccba", "abcba", "abcddcba", "abcdefedcba"
                       "abcdefgfedcba", "abcdefghhgfedcba", "aabbaabbaabbaa" ]

        # Generate randomized sequence of lowercase a-z and digits
        chars = list(string.ascii_lowercase + string.digits)
        random.shuffle(chars)

        # num_trials = int(input("Enter number of times to repeat random tests: "))
        num_trials = 1
        
        for i in range(num_trials):
            print("Beginning tests for trial {}:".format(i + 1))
            for word in test_cases:
                word = randomize_string(word, chars)
                print("s: {} p: {}".format(word, s.longestPalindrome(word)))

