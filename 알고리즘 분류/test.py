def solution(N):
    
    nums = []

    while N != 1:
        a = N//2
        b = N%2
        nums.append(b)
        N = a
    nums.append(N)
    nums.reverse()
    print(nums)
    lens = 0
    i = 0
    while i < len(nums):
        if nums[i] == 1:
            i += 1
            count = 0
            t = False
            for _ in range(len(nums)-i):
                if nums[i] == 1:
                    t = True
                    break
                count += 1
                i += 1
            if t:
                if count > lens:
                    lens = count
    print(count)
    print(lens)
solution(1041)