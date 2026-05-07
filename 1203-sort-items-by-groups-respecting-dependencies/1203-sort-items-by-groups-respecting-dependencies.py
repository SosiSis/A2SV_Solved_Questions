class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:

      
        def topological_sort(in_degree: List[int], adjacency_list: List[List[int]], nodes: List[int]) -> List[int]:
           
            queue = deque(node for node in nodes if in_degree[node] == 0)
            sorted_result = []
          
            while queue:
                current_node = queue.popleft()
                sorted_result.append(current_node)
              
                for neighbor in adjacency_list[current_node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            return sorted_result if len(sorted_result) == len(nodes) else []

        next_group_id = m
        groups_to_items = [[] for _ in range(n + m)]  
      
        for item_id, group_id in enumerate(group):
            if group_id == -1:
                
                group[item_id] = next_group_id
                next_group_id += 1
            groups_to_items[group[item_id]].append(item_id)
      
        item_in_degree = [0] * n
        group_in_degree = [0] * (n + m)
        item_adjacency = [[] for _ in range(n)]
        group_adjacency = [[] for _ in range(n + m)]
      
        for current_item, current_group in enumerate(group):
            for prerequisite_item in beforeItems[current_item]:
                prerequisite_group = group[prerequisite_item]
              
                if current_group == prerequisite_group:
                    
                    item_in_degree[current_item] += 1
                    item_adjacency[prerequisite_item].append(current_item)
                else:
                    
                    group_in_degree[current_group] += 1
                    group_adjacency[prerequisite_group].append(current_group)
      
        sorted_groups = topological_sort(group_in_degree, group_adjacency, list(range(n + m)))
        if not sorted_groups:
            return []  
      
        final_result = []
        for group_id in sorted_groups:
            items_in_group = groups_to_items[group_id]
            sorted_items = topological_sort(item_in_degree, item_adjacency, items_in_group)
          
            if len(items_in_group) != len(sorted_items):
                return []  
          
            final_result.extend(sorted_items)
      
        return final_result