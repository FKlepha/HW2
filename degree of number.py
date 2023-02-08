N = int(input())

deg = 0
num = 2
count = num ** deg

while count < N:
    print(count)
    deg += 1
    count = num ** deg
