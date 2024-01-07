# def solution(text):
#     index = dict()
#     index['A'] = 0
#     index['B'] = 1
#     k = []
#     idx = 0
    
#     while idx <= len(text):
#         print('dic', index)
#         end = idx +1
#         key = text[idx:end]
#         print('start key', key)
#         print(idx, end)
#         while end <= len(text):
#             print('now key', key)
#             if key not in index:
#                 end -= 1
#                 key = key[:-1]
#                 break
#             end +=1
#             if end > len(text):
#                 end -= 1 
#                 break
#             key += text[end-1]
#         k.append(index[key])
#         if end == len(text):
#             break
#         else:
#             key += text[end]
#             index[key] = len(index)
#         idx = end
#     print(k)
#     return
        
    
# solution('ABABAABAB')

from collections import Counter
arr = [5, 5, 5, 5, 5]

count = Counter(arr)
r = dict()
c = dict()

for i in count:
    cc = count[i]//2
    rr = count[i]%2
    if cc != 0:
        c[i] = cc
    if rr != 0:
        r[i] = rr

c = dict(sorted(c.items(), reverse=True))
r = dict(sorted(r.items(), reverse=True))
print(sum(c.values()), r)
while sum(c.values()) > sum(r.values()):
    print(c,  r)
    tmp = min(c.keys())
    c[tmp] -= 1
    if c[tmp] ==  0:
        del c[tmp]
    if tmp not in r:
        r[tmp] = 2
    else:
        r[tmp] += 2
ans = 0
for i in c:
    ans += i * c[i] +1
        
print(ans)
    