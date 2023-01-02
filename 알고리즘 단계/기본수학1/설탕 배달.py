def suga(n):
    mini = 0
    if n // 5 == 0 and n % 3 != 0 or n ==7:
        mini = -1 
    elif n % 5 == 0:
        mini = n // 5
    elif n % 5 == 1 or n % 5 == 3:
        mini = n // 5 + 1
    elif n % 5 == 2 or n % 5 == 4:
        mini = n // 5 + 2 

    print(mini)

n = int(input())
suga(n) 
       
