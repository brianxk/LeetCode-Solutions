### SOLUTION CODE ###

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Potential base case of len(s) == 1

        seen_chars = {}
        intervals = {}

        for i, c in enumerate(s):
            if c in seen_chars:
                targets = seen_chars[c]

                for t in targets:
                    interval = Interval(t, i)

                    if interval.length() in intervals:
                        intervals[interval.length()].append(interval)
                    else:
                        intervals[interval.length()] = [interval]

                seen_chars[c].append(i)

            else:
                seen_chars[c] = [i]

        # Sort by interval length
        interval = dict(sorted(intervals.items()))

        for interval_len, interval_list in intervals.items():
            print(interval_len, interval_list)

        return s

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.len = self.end - self.start

    def length(self):
        return self.len

    def __str__(self):
        return "{}:{}".format(self.start, self.end)

    def __repr__(self):
        return self.__str__()

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
                       "abcdefgfedcba", "abcdefghhgfedcba" ]

        # Generate randomized sequence of lowercase a-z and digits
        chars = list(string.ascii_lowercase + string.digits)
        random.shuffle(chars)

        # num_trials = int(input("Enter number of times to repeat random tests: "))
        num_trials = 1
        
        for i in range(num_trials):
            print("Beginning tests for trial {}:".format(i + 1))
            for word in test_cases:
                word = randomize_string(word, chars)
                print(s.longestPalindrome(word))

