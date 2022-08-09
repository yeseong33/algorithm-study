import sys

n = int(sys.stdin.readline())
l = [sys.stdin.readline().strip() for i in range(n)]
# strip() 함수는 디폴트 시 공백과 \n 를 모두 제거해준다.
for i in l:
    score = 0
    score_s = 0
    for j in range(len(i)):
        if i[j] == 'O':
            score_s += 1
            score += score_s
        else:
            score_s = 0
    print(score)
                            
