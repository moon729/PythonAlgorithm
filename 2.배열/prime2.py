#1,000이하의 소수 나열하기(알고리즘 개선)

counter = 0 #나눗셈 횟수 카운트
ptr = 0 #이미 찾은 소수의 개수
prime = [None] * 500 #소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

for i in range(3, 1001, 2):
    for n in range(1, ptr):
        counter += 1
        if i % prime[n] == 0:
            break
    else:
        prime[ptr] = i
        ptr += 1

for i in range(ptr):
    print(prime[i], end = ' ')
print(f'나눗셈 실행 횟수 : {counter}')
