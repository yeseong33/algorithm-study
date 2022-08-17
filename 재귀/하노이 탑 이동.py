n = int(input())
c = 0
def ha(n, start, via, to):
    global c
    if n > 1:
        ha(n-1, start, to, via)
        print(start, to)
        c +=1 
        ha(n-1, via, start, to)
    else:
        print(start, to)
        c += 1

# print(2**n-1)
ha(n, 1, 2, 3)
print(c)


# ha(3, 1, 2, 3)
#     ha(2, 1, 3, 2)
#         ha(1, 1, 2, 3)
#         print(1, 3)
#     print(1,2)
#         ha(1, 3, 1, 2)
#         print(3, 2)
    
#     print(1, 3 )
    
#     ha(2, 2, 1, 3)
#         ha(1, 2, 3, 1)
#         print(2, 1)
#     print(2, 3)
#         ha(1, 1, 2, 3)
#         print(1, 3)
    
    
        
