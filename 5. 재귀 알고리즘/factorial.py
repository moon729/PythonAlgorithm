#factorial

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n-1)
    elif n == 0:
        return 1
    else: #n이 음수로 들어옴
        raise ValueError

if __name__ == '__main__':
    n = int(input('팩토리얼 출력할 값 입력 : '))

    try:
        print(f'{n}의 팩토리얼 : {factorial(n)}')
    except ValueError:
        print('팩토리얼 구할 수 없음')
