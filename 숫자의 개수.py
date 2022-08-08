data = [int(input()) for i in range(3)]
k = 1
for i in range(3):
    k *= data[i]
k = str(k)
count = [0 for i in range(10)]
for i in k:
    count[int(i)] += 1

for i in count:
    print(i)

    
    