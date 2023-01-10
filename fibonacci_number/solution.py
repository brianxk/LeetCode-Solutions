class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        prev_1 = 1
        prev_2 = 0

        i = 2
        fib_n = 0

        while i <= n:
            fib_n = prev_1 + prev_2

            prev_2 = prev_1
            prev_1 = fib_n
            
            i += 1

        return fib_n

if __name__ == "__main__":
    user_input = input("Enter a number: ")

    s = Solution()

    while user_input:
        user_input = int(user_input)
        print(s.fib(user_input))
        user_input = input("Enter a number: ")
