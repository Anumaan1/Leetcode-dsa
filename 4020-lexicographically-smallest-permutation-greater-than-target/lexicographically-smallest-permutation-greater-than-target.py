class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        i = 0

        while i < len(target):
            x = ord(target[i]) - 97

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            i += 1

        for j in range(i, -1, -1):

            if j < i:
                x = ord(target[j]) - 97
                cnt[x] += 1

            if j == len(target):
                continue

            x = ord(target[j]) - 97

            for k in range(x + 1, 26):
                if cnt[k] > 0:
                    cnt[k] -= 1

                    ans = target[:j] + chr(k + 97)

                    for p in range(26):
                        ans += chr(p + 97) * cnt[p]

                    return ans

        return ""