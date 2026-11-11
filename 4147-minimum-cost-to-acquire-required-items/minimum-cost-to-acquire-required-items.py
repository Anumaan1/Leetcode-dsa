
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        ans1 = need1 * cost1 + need2 * cost2

        ans2 = (min(need1, need2) * costBoth +
                max(0, need1 - need2) * cost1 +
                max(0, need2 - need1) * cost2)

        ans3 = max(need1, need2) * costBoth

        return min(ans1, ans2, ans3)
