#1,000이하의 소수 나열하기(알고리즘 개선 2)
#n의 제곱근 이하의 수로 나누어지지 않으면 '소수'이다 

counter = 0 #나눗셈 횟수 카운트
ptr = 0 #이미 찾은 소수의 개수
prime = [None] * 500 #소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i], end = ' ')
print(f'나눗셈 실행 횟수 : {counter}')
