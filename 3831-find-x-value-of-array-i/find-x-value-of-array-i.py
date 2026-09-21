from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            rem = num % k
            new_dp = [0] * k

            # Sirf current element wala subarray
            new_dp[rem] += 1

            # Purane subarrays ko current element ke saath extend karo
            for r in range(k):
                new_rem = (r * rem) % k
                new_dp[new_rem] += dp[r]

            # Sabhi subarrays ka answer me contribution
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans