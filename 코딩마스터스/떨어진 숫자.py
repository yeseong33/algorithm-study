import sys
input = sys.stdin.readline
print = sys.stdout.write
a = sorted((map(int, input().strip())))
b = sorted((map(int, input().strip())))

if a == b:
    print('YES')
else:
    print('NO')
