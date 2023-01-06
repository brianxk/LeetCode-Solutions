class Solution:
    def myAtoi(self, s: str) -> int:

        # Edge case: empty string
        if not s:
            return 0

        INT_MIN = -2 ** 31
        INT_MAX = (2 ** 31) - 1

        i = 0

        # Eliminate leading whitespaces
        while i < len(s) and s[i] == " ":
            i += 1
        
        # Edge case: string was all whitespaces
        if not i < len(s):
            return 0

        negative = False

        if s[i] in ('+', '-'):
            negative = True if s[i] == '-' else False

            i += 1
        
            # Edge case: string ends after sign, or digits do not follow sign
            if not i < len(s) or not s[i].isdigit():
                return 0
        # Edge case: whitespaces not followed by sign or digits
        elif not s[i].isdigit():
            return 0

        start = i

        while i < len(s) and s[i].isdigit():
            i += 1

        end = i

        num = int(s[start:end]) if not negative else -int(s[start:end])

        if num > INT_MAX:
            num = INT_MAX
        elif num < INT_MIN:
            num = INT_MIN
    
        return num
