total =  0
before = 0
nums = []

for i in range(10):
    nums.append(int(input()))

for i in range(10):
    before = total
    total += nums[i]
    if total >= 100:
        break
    
if 100-before >= total-100:
    print(total)
else:
    print(before)

