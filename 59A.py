str = str(input())
upper = 0
lower = 0
for i in str:
    if i.isupper():
        upper = upper + 1 
    else:
        lower = lower +1

if upper > lower:
    print(str.upper())
else:
    print(str.lower())
