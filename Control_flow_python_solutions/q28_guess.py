import random
s=random.randint(1,10)
while True:
    g=int(input())
    if g==s:print("Correct");break
    elif g<s:print("Higher")
    else:print("Lower")
