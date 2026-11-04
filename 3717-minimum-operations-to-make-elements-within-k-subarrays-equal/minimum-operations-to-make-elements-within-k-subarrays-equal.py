class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class FenwickSum(Fenwick):
    pass


class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)
        mp = {v: i + 1 for i, v in enumerate(vals)}

        count = Fenwick(m)
        sums = Fenwick(m)

        def add(v, delta):
            p = mp[v]
            count.update(p, delta)
            sums.update(p, v * delta)

        def get_cost():
            mid = vals[count.kth((x + 1) // 2) - 1]
            p = mp[mid]

            left_count = count.query(p)
            left_sum = sums.query(p)

            total_sum = sums.query(m)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (mid * left_count - left_sum +
                    right_sum - mid * right_count)

        costs = []

        for i in range(n):
            add(nums[i], 1)

            if i >= x:
                add(nums[i - x], -1)

            if i >= x - 1:
                costs.append(get_cost())

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]