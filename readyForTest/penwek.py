import sys


def makeSettings():
    n, m, k = map(int, sys.stdin.readline().split())
    arr = [0] * (n+1)
    tree = [0] * (n+1)

    for i in range(1, n+1):
        value = int(sys.stdin.readline().strip())
        arr[i] += value
        updateTree(i, n, value, tree)

    return arr, tree, n, m, k


def updateTree(i, n, dif, tree):
    while i <= n:
        tree[i] += dif
        i += (i&-i)

def sumOfTree(i, tree):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result


def printAll(n, m, k, tree, arr):
    for _ in range(m+k):
        comd, a, b = map(int, sys.stdin.readline().split())
        if comd == 1:
            print(tree)
            updateTree(a, n, b-arr[a], tree)
            arr[a] = b
            print(tree)
        else:
            print(sumOfTree(b, tree) - sumOfTree(a-1, tree))


def solve():
    arr, tree, n, m, k = makeSettings()
    printAll(n, m, k, tree, arr)


solve()