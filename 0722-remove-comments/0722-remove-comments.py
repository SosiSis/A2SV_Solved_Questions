class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        new_line = []
        
        for line in source:
            i = 0
            
            if not in_block:
                new_line = []
            
            while i < len(line):
                
                if not in_block:
                    if line[i:i+2] == '/*':
                        in_block = True
                        i += 1 
                    elif line[i:i+2] == '//':
                        break 
                    else:
                        new_line.append(line[i])
                
                
                else:
                    if line[i:i+2] == '*/':
                        in_block = False
                        i += 1 
                i += 1
            
            
            if not in_block and new_line:
                res.append("".join(new_line))
                
        return res