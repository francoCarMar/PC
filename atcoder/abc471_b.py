n = int(input())

dict = {} 
winner = 0
for i in range(n):
    s = input().lower()
    dict[s] = dict.get(s, 0) + 1 
    winner = max(winner, dict[s])
print(winner)

