import sys


def selfNum():
    nums = [0] * (2 * 10**4)

    for i in range(1, 10030):
        idx = i + (i % 10) + (i//10)%10 + (i//100)%10 + (i//1000)%10
        nums[idx] = 1


    for i in range(1,10001):
        if nums[i] == 0:
            print(i)


selfNum()

# import cProfile

# cProfile.run("selfNum()")