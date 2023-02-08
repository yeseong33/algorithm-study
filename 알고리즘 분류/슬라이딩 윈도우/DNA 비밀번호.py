import sys
s, p = map(int, sys.stdin.readline().split())

dna = input()

start = 0
end = start + p -1
count = 0

A, C, G, T = map(int, sys.stdin.readline().split())

pw_dict = dict()
pw_dict['A'] = 0
pw_dict['C'] = 0
pw_dict['T'] = 0
pw_dict['G'] = 0


pw = dna[start:end+1]

for i in pw:
    pw_dict[i] += 1
    
while end < s:
    if start > 0:
        
        pw_dict[dna[start-1]] -= 1
        pw_dict[dna[end]] += 1
    
    
    if pw_dict['A'] >= A and pw_dict['C'] >= C and pw_dict['T'] >= T and pw_dict['G'] >= G:
        count += 1
    
    start += 1
    end += 1
         

print(count)

# 백준(DNA 비밀번호, 12891)

# 시간 복잡도 문제를 딕셔너리를 사용해 해결
