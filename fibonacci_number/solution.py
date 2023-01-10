class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        fib_seq = [0] * (n + 1)

        fib_seq[0] = 0
        fib_seq[1] = 1

        for i in range(2, len(fib_seq)):
            fib_seq[i] = fib_seq[i - 2] + fib_seq[i - 1]

        return fib_seq[n]

if __name__ == "__main__":
    user_input = input("Enter a number: ")

    s = Solution()

    while user_input:
        user_input = int(user_input)
        print(s.fib(user_input))
        user_input = input("Enter a number: ")
