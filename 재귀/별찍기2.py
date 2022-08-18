# import math

# def star(n):
#     s = []
#     if n==1:
#         s.append('***')
#         s.append('* *')
#         s.append('***')
        
#     if n>=2:
#         t = star(n-1)
#         for i in range(len(t)):
#             s.append(t[i]*3)
#         for i in range(len(t)):
#             s.append(t[i] + ' '*(3**(n-1)) + t[i])
#         for i in range(len(t)):
#             s.append(t[i]*3)
#     return s

# num = int(input())
# n = math.ceil(math.log(num,3))

# s = star(n)
# for i in range(len(s)):
#     print(s[i])


def draw_stars(n):
  if n==1:
    return ['*']

  Stars=draw_stars(n//3)

  star_list=[]

  for iteration in Stars:
    star_list.append(iteration*3)

  for iteration in Stars:
    star_list.append(iteration+' '*(n//3)+iteration)

  for iteration in Stars:
    star_list.append(iteration*3)

  return star_list

N=int(input())

# print(draw_stars(N))
print('\n'.join(draw_stars(N)))