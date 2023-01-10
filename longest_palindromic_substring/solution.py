class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        substrings = self.generate_all_substrings(s, n)

        lps = ""
        lps_len = 0
        for substring in substrings:
            if self.is_palindrome(substring) and len(substring) > lps_len:
                lps = substring
                lps_len = len(lps)

        return lps

    def is_palindrome(self, s):
        return s == s[::-1]

    def generate_all_substrings(self, s, n):
        substrings = []

        for i in range(n):
            for j in range(i, n):
                substrings.append(s[i:j + 1])

        return substrings

if __name__ == "__main__":
    s = Solution()
    
    user_s = input("Enter a string: ")

    while user_s:
        s.longestPalindrome(user_s)
        user_s = input("Enter a string: ")
