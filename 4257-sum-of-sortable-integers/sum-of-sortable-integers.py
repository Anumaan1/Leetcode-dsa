
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        prefMax = [0] * (n + 1)
        suffMin = [float('inf')] * (n + 1)
        prefDrop = [0] * (n + 1)

        for i in range(n):
            prefMax[i + 1] = max(prefMax[i], nums[i])
            prefDrop[i + 1] = prefDrop[i]
            if i > 0 and nums[i - 1] > nums[i]:
                prefDrop[i + 1] += 1

        for i in range(n - 1, -1, -1):
            suffMin[i] = min(suffMin[i + 1], nums[i])

        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                j = i + k - 1

                drops = prefDrop[j + 1] - prefDrop[i + 1]
                if nums[j] > nums[i]:
                    drops += 1

                if drops > 1 or prefMax[i] > suffMin[i]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
