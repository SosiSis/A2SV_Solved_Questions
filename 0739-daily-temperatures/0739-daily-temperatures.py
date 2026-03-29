class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n= len(temperatures)
        answer = [0]*n

        for i,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                j = stack.pop()
                answer[j] = i-j
            stack.append(i)
        return answer        