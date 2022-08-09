data = [int(input()) for i in range(3)]
k = 1
for i in range(3):
    k *= data[i]
k = str(k)
for i in range(10):
    print(k.count(str(i)))




# count = [0 for i in range(10)]
# for i in k:
#     count[int(i)] += 1

# for i in count:
#     print(i)


    