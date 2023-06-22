import sys

s = sys.stdin.readline().strip()

s_len = len(s)
p = 0
unable = ['<', '>']

while p < s_len:
    
    if s[p] == ' ':
        p += 1
    
    elif s[p] not in unable:
        start = p
        end = p + 1
        while end < s_len:
            if s[end] in unable or s[end] == ' ':
                break
            end += 1 
        end -= 1
        s = s[:start] + s[end:start:-1] + s[start] + s[end+1:]
        
        p = end+1
    else:
        start = p
        end = p + 1
        while end < s_len:
            if s[end] in unable:
                end += 1
                break
                break
            end += 1 
        p = end
        
print(s)
        
    
    