class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map=defaultdict(list)

        for path in paths:
            path_split=path.split()
            directory=path_split[0]

            for i in range(1,len(path_split)):
                parts=path_split[i].split('(')
                file_name=parts[0]
                content=parts[1][:-1]

                path_=f'{directory}/{file_name}'
                content_map[content].append(path_)
        return [group for content,group in content_map.items() if len(group) > 1]