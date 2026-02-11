class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        all_response=[]
        for response in responses:
            remove_duplicate=list(set(response))
            for response in remove_duplicate:
                all_response.append(response)
        count_response=Counter(all_response)
        ans= sorted(count_response.items(), key=lambda x: (-x[1], x[0]))
        return ans[0][0] if ans else ""