t = int(input())
c = 0

def isPalindrome(s, l, r):
    global c
    c += 1
    
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return isPalindrome(s, l+1, r-1)
    


for i in range(t):
    s = input()
    print(isPalindrome(s, 0, len(s)-1), c)
    c = 0 
