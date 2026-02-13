class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_list=list(pattern)
        s_list=s.split()
        _map=defaultdict(str)

        if len(pattern_list) !=  len(s_list):
            return False

        for pattern_map,s_map in zip(pattern_list,s_list):

            if pattern_map not in _map and s_map not in _map.values():
                _map[pattern_map]=s_map

            else:
                if _map[pattern_map] != s_map :
                    return False  

        return True            