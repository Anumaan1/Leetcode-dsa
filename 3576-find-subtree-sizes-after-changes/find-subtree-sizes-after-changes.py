
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        stack = [(0, 0, -1)]

        while stack:
            node, state, old = stack.pop()
            ch = s[node]

            if state == 0:
                old = last.get(ch, -1)

                if old != -1:
                    new_parent[node] = old

                last[ch] = node

                stack.append((node, 1, old))

                for child in reversed(children[node]):
                    stack.append((child, 0, -1))

            else:
                if old == -1:
                    del last[ch]
                else:
                    last[ch] = old

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        order = [0]

        for node in order:
            for child in new_children[node]:
                order.append(child)

        ans = [1] * n

        for node in reversed(order):
            for child in new_children[node]:
                ans[node] += ans[child]

        return ans
