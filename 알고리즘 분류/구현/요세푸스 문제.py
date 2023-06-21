import sys

n, k = map(int, sys.stdin.readline().split())  


yo = [i for i in range(1, n+1)]

# 1 2 3 4 5 6 7
def kill(yo):
    
    ans = []
    p = 0
    
    while True:
      count = k-1 
      while count != 0:
        p = (p + 1) % n
        if yo[p] != 0:
          count -= 1
      
            
      ans.append(yo[p])
      yo[p] = 0
      c = 0
      
      if any(yo) == 0:
        break
      
      while yo[p] == 0:
        p = (p + 1) % n
    
    return ans

a = kill(yo)       

a = map(str, a)

print('<' + ', '.join(a) + '>')