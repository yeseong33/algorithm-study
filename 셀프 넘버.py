# def selfNum():
#     for i in range(1, 10001):
#         c = 0
#         if i >= 36:
#             for j in range(i-36,i):
#                 selfN = 0
#                 selfN += sum(tuple(map(int, str(j)))) + j 
                
#                 # for k in range(len(n)):
#                 #     selfN += int(n[k])
                
#                 if selfN == i:
#                     c += 1
#                     break
#             if c == 0:
#                 # sys.stdout.write(str(i))
#                 print(i)
#         else:
#             for j in range(i):
#                 selfN = 0
#                 selfN += sum(tuple(map(int, str(j)))) + j 
                
#                 # for k in range(len(n)):
#                 #     selfN += int(n[k])
                
#                 if selfN == i:
#                     c += 1
#                     break
#             if c == 0:
#                 # sys.stdout.write(str(i))
#                 print(i)
#     # self_num()
# # # print('ss')

def selfNum():
    for i in range(1, 10001):
        c = 0
        if i >= 36:
            for j in range(i-36,i):
                selfN = 0
                selfN += sum(tuple(map(int, str(j)))) + j 
                if selfN == i:
                    c += 1
                    break
            if c == 0:
                print(i)
        else:
            for j in range(i):
                selfN = 0
                selfN += sum(tuple(map(int, str(j)))) + j 
                if selfN == i:
                    c += 1
                    break
            if c == 0:
                print(i)

import cProfile

cProfile.run("selfNum()")