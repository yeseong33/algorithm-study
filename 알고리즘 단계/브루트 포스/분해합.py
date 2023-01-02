n = int(input())

def hap(n):
    for i in range(n):
        k = 0
        l = len(str(i))
        for j in range(l):
            k += int(str(i)[j])
        k += i
        if k == n:
            return i
    return 0


print(hap(n))



n = int(input())

def hap(n):
    if n < 100:
        for i in range(n):
            k =0
            nums = list(map(int, str(i)))
            k = sum(nums) + i
            if k == n:
                return i
    else:
        lng = len(str(n))
        for i in range(n-9 * lng, n):
            k =0
            nums = list(map(int, str(i)))
            k = sum(nums) + i
            if k == n:
                return i
    return 0

print(hap(n))

