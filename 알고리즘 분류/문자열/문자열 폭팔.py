import sys


# def Boom(S, B):

#     s_idx = 0
#     b_idx = 0
#     string = S
    
#     s_len = len(S)
#     b_len = len(B)
#     visited = [0] * s_len

#     while s_idx < s_len:
#         if visited[s_idx] == 1:
#             s_idx += 1 
#             continue
        
#         if B[b_idx] == string[s_idx]:
#             boom = True
            
#             while b_idx < b_len:
#                 if visited[s_idx]: 
#                     while visited[s_idx]:
#                         s_idx += 1
#                         if s_idx > s_len-1:
#                             return visited

#                 if B[b_idx] != string[s_idx]:
#                     b_idx = 0
#                     boom = False
#                     break
                
#                 b_idx += 1
#                 s_idx += 1
                
#                 if s_idx > s_len:
#                     return visited
#             if boom:
#                 b_idx = 0
#                 count = b_len # 2
#                 i = s_idx-1
#                 while count:
#                     if visited[i]:
#                         i -= 1
#                         continue
#                     visited[i] = 1
#                     count -= 1
#                 s_idx = s_idx - 2*b_len
#                 if s_idx < 0:
#                     s_idx = 0
                    
#         else:
#             s_idx += 1
#     return visited
            

def Boom(S, B):
    
    stack = []
    now_len = 0
    string = S
    tri = B
    s_idx = 0
    s_len = len(S)
    tri_len = len(tri)
    
    for i in range(s_len):
        stack.append(string[i])
        if ''.join(stack[-tri_len:]) == tri:
            for i in range(tri_len):
                stack.pop()
    
    return stack
    
s = input()
b = input()

ans = Boom(s, b)

if ans == []:
    print("FRULA")
else: 
    print(''.join(ans))

