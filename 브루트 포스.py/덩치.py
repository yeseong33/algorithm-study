import sys
n = int(input())



def rank(n):
    people = []
    for i in range(n):
        p = list(map(int, sys.stdin.readline().split()))
        p += [1]
        people.append(p)
    
    for i in range(len(people)):
        for j in range(i+1, len(people)):
            if people[i][0] < people[j][0]:
                if people[i][1] < people[j][1]:
                    people[i][2] += 1 
            elif people[i][0] > people[j][0]:
                if people[i][1] > people[j][1]:
                    people[j][2] += 1
    return people



r = rank(n)
for i in range(n):
    print(r[i][2], end = ' ')    