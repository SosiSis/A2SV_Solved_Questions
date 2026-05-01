class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
 
        adjacency_list = defaultdict(list)
        in_degree = [0] * n
      
        for prerequisite, course in relations:
       
            adjacency_list[prerequisite - 1].append(course - 1)
            in_degree[course - 1] += 1
      
       
        queue = deque()
        completion_time = [0] * n
        max_completion_time = 0
      
        for course_id in range(n):
            if in_degree[course_id] == 0:
                queue.append(course_id)
                completion_time[course_id] = time[course_id]
                max_completion_time = max(max_completion_time, completion_time[course_id])
      
        while queue:
            current_course = queue.popleft()

            for next_course in adjacency_list[current_course]:
                completion_time[next_course] = max(
                    completion_time[next_course], 
                    completion_time[current_course] + time[next_course]
                )
                max_completion_time = max(max_completion_time, completion_time[next_course])

                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
      
        return max_completion_time