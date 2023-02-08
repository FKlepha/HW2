N = int(input())
numb = 2
count = 1
while count <= N:
    if N == count:
        print('YES')
        break
    count = numb * count
else:
    print('NO')