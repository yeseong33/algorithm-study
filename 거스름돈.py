price = int(input())
change = 1000 - price
count = 0 
while change != 0:
    if change >= 500:
        count += change//500
        change  = change%500
    elif change >= 100:
        count += change//100
        change = change%100
    elif change >= 50:
        count += change//50
        change = change%50
    elif change >= 10:
        count += change//10
        change = change%10
    elif change >= 5:
        count += change//5
        change = change%5
    else:
        count += change
        change = 0
print(count)


won_500 = change//500
won_100 = change%500//100
won_50 = change%500%100//50
won_10 = change%500%100%50//10
won_5 = change%500%100%50%10//5
won_1 = change%500%100%50%10%5
print(won_500+won_100+won_50+won_10+won_5+won_1)


####
price = int(input())
change = 1000 - price
coin = [500, 100, 50, 10 , 5, 1]
count = 0
for i in coin:
    count += change//i
    change = change%i
print(count)