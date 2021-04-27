
#10진수 정숫값 입력받아 2~36진수로 변환 출력

def card_carv(x: int, r: int)-> str:

    d = ''
    dchar = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x%r]
        x //= r
    return d[::-1]

if __name__ == '__main__':

    print('10진수를 n진수로 반환')

    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수 입력 : '))
            if no > 0:
                break
        while True:
            cd = int(input('몇 진수로 변환? :'))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_carv(no, cd)}입니다.')

        retry = input("한번 더 변환 ? Y/N")
        if retry in {'N', 'n'}:
            break
