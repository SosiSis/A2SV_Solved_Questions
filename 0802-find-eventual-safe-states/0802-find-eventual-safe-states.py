class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree_count = [0] * n
        reversed_graph = defaultdict(list)

        for u in range(n):
            for v in graph[u]:
                reversed_graph[v].append(u)
                indegree_count[u] += 1

        queue = deque([i for i in range(n) if indegree_count[i] == 0])
        safe_nodes = []

        while queue:
            current = queue.popleft()
            safe_nodes.append(current)

            for neighbor in reversed_graph[current]:
                indegree_count[neighbor] -= 1
                if indegree_count[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe_nodes)