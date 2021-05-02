w = 20
d = [[0 for j in range(w)] for i in range(w)]
tmp = [0] * w

# 입력받은 값 바둑판 채우기
for i in range(1, w):
    tmp = input().split()
    for j in range(1, w):
        d[i][j] = tmp[j-1]

# 입력받은 좌표의 행, 열 뒤집기
n = int(input())
for i in range(n):
    x, y = input().split()
    for j in range(1, w):
        if j != int(x) and j != int(y):
            d[int(x)][j] = (1 if d[int(x)][j] == 0 else 0)
            d[j][int(y)] = (1 if d[j][int(y)] == 0 else 0)
# 출력
for i in range(1,w):
    for j in range(1,w):
        print(d[i][j], end = ' ')
    print()