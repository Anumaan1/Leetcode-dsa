class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = 0

        while n >= a + 1:
            a += 1
            n -= a

        return a