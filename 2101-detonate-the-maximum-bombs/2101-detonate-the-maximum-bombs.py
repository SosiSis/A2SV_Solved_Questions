class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        num_bombs = len(bombs)
        graph = [[] for _ in range(num_bombs)]
      
        for i in range(num_bombs - 1):
            x1, y1, radius1 = bombs[i]
            for j in range(i + 1, num_bombs):
                x2, y2, radius2 = bombs[j]
              
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
              
                if distance <= radius1:
                    graph[i].append(j)
              
                if distance <= radius2:
                    graph[j].append(i)
      
        max_detonations = 0
      
        for start_bomb in range(num_bombs):
            
            visited = {start_bomb}
            queue = [start_bomb]
          
            for current_bomb in queue:
                for neighbor_bomb in graph[current_bomb]:
                    if neighbor_bomb not in visited:
                        visited.add(neighbor_bomb)
                        queue.append(neighbor_bomb)
          
            if len(visited) == num_bombs:
                return num_bombs
          
            max_detonations = max(max_detonations, len(visited))
      
        return max_detonations