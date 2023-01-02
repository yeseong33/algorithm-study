import sys

def merge_sort(s):
    if len(s) > 1:
        mid = len(s) // 2
        return merge(merge_sort(s[:mid+1]), merge_sort(s[mid+1:]))
    else:
        return s
        
    
    

# def merge(l, r):
#     if l != [] and r != []:
#         if l[0] > r[0]:
#             return [r[0]] + merge(l, r[1:])
#         else:
#             return [l[0]] + merge(l[1:], r)
#     else:
#         return l + r
    

# def merge(l, r):
#     def loop(k, l, r):
#         if l != [] and r != []:
#             if l[0] > r[0]:
#                 return loop(k+[r[0]], l, r[1:])
#             else:
#                 return loop(k+[l[0]], l[1:], r)
#         else:
#             return k + l + r
#     return loop([], l, r)

def merge(l, r):
    k = []
    while l != [] and r != []:
        if l[0] > r[0]:
            k.append(r[0])
            r = r[1:]
        else:
            k.append(l[0])
            l = l[1:]
    return k+l+r

n, k = map(int, sys.stdin.readline().split())



