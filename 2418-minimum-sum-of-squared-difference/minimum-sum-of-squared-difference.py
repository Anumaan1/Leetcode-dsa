class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        from collections import Counter

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        freq = Counter(diff)

        for d in range(max(diff), 0, -1):
            if d not in freq:
                continue

            count = freq[d]
            moves = min(k, count)

            freq[d] -= moves
            freq[d - 1] += moves
            k -= moves

            if k == 0:
                break

        return sum(d * d * count for d, count in freq.items())