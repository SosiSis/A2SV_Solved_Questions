class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def bfs(start_node: int) -> None:
            
            queue = deque([start_node])
            visited = {start_node}
          
            while queue:
                current_node = queue.popleft()
              
                for neighbor in adjacency_list[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                
                        ancestors[neighbor].append(start_node)
      
        adjacency_list = defaultdict(list)
        for from_node, to_node in edges:
            adjacency_list[from_node].append(to_node)
      
        ancestors = [[] for _ in range(n)]
      
        for node in range(n):
            bfs(node)
      
        return ancestors