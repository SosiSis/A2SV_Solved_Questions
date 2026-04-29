class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        radj = defaultdict(list)
        badj = defaultdict(list)

        for a, b in redEdges: radj[a].append(b)
        for a, b in blueEdges: badj[a].append(b)

        bans = [float("inf")] * n
        rans = [float("inf")] * n

        bans[0] = rans[0] = 0

        q = deque([(0, "r"), (0, "b")])

        # bfs
        while q:
            curr, last = q.popleft()
            if last == "b":
                for nei in radj[curr]:
                    if bans[curr] + 1 < rans[nei]:
                        rans[nei] = bans[curr] + 1
                        q.append((nei, "r"))
            else:
                for nei in badj[curr]:
                    if rans[curr] + 1 < bans[nei]:
                        bans[nei] = rans[curr] + 1
                        q.append((nei, "b"))

        ans = [float("inf")] * n
        for i in range(n):
            ans[i] = min(bans[i], rans[i])
            if ans[i] == float("inf"): ans[i] = -1
        return ans