import sys
input = sys.stdin.readline

N, M = map(int, input().split())
max_l = N*M
nums_1 = list(map(int, input().split())) 
nums_2 = list(map(int, input().split()))

nums_1_now = 0
nums_2_now = 0
winner = -1

def move_index():
    global nums_1_now, nums_2_now
    nums_1_now += 1
    nums_2_now += 1
    if nums_1_now//N == 1:
        nums_1_now = 0
    if nums_2_now//M == 1:
        nums_2_now = 0

def rsp(nums_1, nums_2, mjp = False):
    global winner
    for _ in range(max_l):
        if not mjp:
            if nums_1[nums_1_now] == nums_2[nums_2_now]:
                move_index()
                continue
        else:
            if nums_1[nums_1_now] == nums_2[nums_2_now]:
                return -1
        big = max(nums_1[nums_1_now], nums_2[nums_2_now])
        if big == nums_1[nums_1_now]:
            small = nums_2[nums_2_now]
            if big - small == 1:
                winner = 0
            else:
                winner = 1
        else:
            small = nums_1[nums_1_now]
            if big - small == 1:
                winner = 1
            else:
                winner = 0
        if not mjp:
            return -4
        else:
            move_index()
            continue
    return -2
            
def mjpa(nums_1, nums_2):
    result = rsp(nums_1, nums_2, mjp=True)
    if result == -1:
        return True
    return False

i = rsp(nums_1, nums_2)    
if i == -2:
    print(0)
else:
    if mjpa(nums_1, nums_2):
        print(winner+1)
    else:
        print(0)