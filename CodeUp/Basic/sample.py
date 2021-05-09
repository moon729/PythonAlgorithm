a = int(input())
b = int(input())

sum = 0
tmp = b
x = [None] * 3

for i in range(3):
    x[i] = (tmp % 10) * a
    tmp = tmp // 10

for i in range(3):
    print(x[i])
    sum += x[i] * (10**i)

print(sum)
