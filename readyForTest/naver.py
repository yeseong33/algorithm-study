def makeMood(watered, plants):
    mood = [0] * len(watered)

    return mood

def morning(w, k, plants, visited):
    if visited[w]:
        for i in range(len(k)):
            if k[i][0] == w:
                k[i][1] = plants[w]
                break
    else:
        visited[w] = 1
        k.append([w, plants[w]])

def evening(day, mood, k, visited):
    newK = []
    mood[day] += len(k)
    for i in range(len(k)):
        k[i][1] -= 1
        if k[i][1] != 0:
            newK.append(k[i])
        else:
            visited[i] = 0

    return newK

def solve(watered, plants):
    mood = makeMood(watered, plants)
    visited = [0] * len(plants)
    k = []
    for day in range(len(watered)):
        w = watered[day]
        morning(w, k, plants, visited)
        k = evening(day, mood, k, visited)

    print(mood)

solve([2, 0, 1, 0, 1], [2, 3, 1, 2])