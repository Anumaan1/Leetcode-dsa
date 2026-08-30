class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        left = min(mn, mx)
        right = max(mn, mx)

        return min(
            right + 1,          # dono front se
            n - left,           # dono back se
            left + 1 + n - right # ek front, ek back
        )