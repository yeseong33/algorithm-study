import sys

n ,m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

start = 0
end = max(nums)
r= 0
while start <= end:
    total = 0
    cut = (start+end)//2
    for i in nums:
        if i > cut:
            total += i-cut

    if  total >= m:
        r = total
        start = cut + 1
    elif total < m:
        end = cut - 1

print(r)

    


# n ,m = map(int, input().split())

# nums = list(map(int, input().split()))

# result = 0 

# start = 0
# end = max(nums)

# while start <= end:
#     total = 0
#     mid = (start+end)//2 
#     for x in nums:
#         if x > mid:
#             total += x-mid
    
#     if total <m :
#         end = mid -1
#     else:
#         result = mid
#         start = mid +1
# print(result)
            