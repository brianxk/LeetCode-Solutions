from enum import Enum

class Solution:
    Palindrome = Enum("Palindrome", "even odd not_")

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        seen_chars = {}
        p_type = self.Palindrome.not_
        p_data = [0, 0] # [0: middle index, 1: length]
        all_palindromes = {} # {p_len:(i, p_type)}
        p_same = False

        for i, c in enumerate(s):
            if p_type is not self.Palindrome.not_:
                p_mid = p_data[0]
                p_len = p_data[1]

                # Checking mirror indices does not work when the entire substring consists of all the same chars
                if p_same and s[i] == s[i - 1]:
                    if p_type is self.Palindrome.even:
                        p_type = self.Palindrome.odd
                    else:
                        p_data[0] += 1 
                        p_data[1] += 1
                        p_type = self.Palindrome.even
                elif p_same and s[i] != s[i - 1]:
                    p_same = False

                if not p_same:
                    target_i = p_mid - (p_len + 1)

                    if target_i >= 0 and s[target_i] == s[i]:
                        p_data[1] += 1
                    else:
                        if p_len not in all_palindromes or p_type is self.Palindrome.odd:
                            all_palindromes[p_len] = (p_mid, p_type)

                        if c in seen_chars:
                            p_type = self.in_palindromic_range(i, seen_chars[c])
                        else:
                            seen_chars[c] = [i]
                            p_type = self.Palindrome.not_

                        if p_type is not self.Palindrome.not_:
                            p_data[0] = i if p_type is self.Palindrome.even else i - 1
                            p_data[1] = 1

            else:
                if c in seen_chars:
                    p_type = self.in_palindromic_range(i, seen_chars[c])

                    if p_type is not self.Palindrome.not_:
                        if p_type is self.Palindrome.even:
                            p_data[0] = i
                            p_same = True
                        else:
                            p_data[0] = i - 1

                        p_data[1] = 1
                                        
                    seen_chars[c].append(i)

                else:
                    seen_chars[c] = [i]

        if p_type is not self.Palindrome.not_:
            p_len = p_data[1]
            p_mid = p_data[0]

            if p_len not in all_palindromes or p_type is self.Palindrome.odd:
                all_palindromes[p_len] = (p_mid, p_type)

        print(all_palindromes)
        if all_palindromes:
            all_palindromes = sorted(all_palindromes.items(), reverse=True)
            longest_palindrome = all_palindromes[0]

            p_len = longest_palindrome[0]
            p_mid = longest_palindrome[1][0]
            p_type = longest_palindrome[1][1]

            begin = p_mid - p_len
            end = p_mid + p_len if p_type is self.Palindrome.even else p_mid + p_len + 1
        else:
            begin = 0
            end = 1

        return s[begin:end]

    def in_palindromic_range(self, i, indices):
        min_i = i - 2

        for candidate in indices:
            if candidate >= min_i:
                diff = i - candidate

                if diff % 2 == 0:
                    return self.Palindrome.odd
                else:
                    return self.Palindrome.even

        return self.Palindrome.not_

if __name__ == "__main__":
    s = Solution()

    user_inp = input("Enter a string: ")

    while user_inp:
        print(s.longestPalindrome(user_inp))
        user_inp = input("Enter a string: ")

