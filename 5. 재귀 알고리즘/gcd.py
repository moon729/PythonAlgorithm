#euclidean algorithm

def gcd(x:int, y:int) -> int:
    if x < y:
        x, y = y, x

    if y == 0: return x
    else:
        return gcd(y, x%y)



if __name__ == '__main__':
    x = int(input('x : '))
    y = int(input('y : '))
    print(f'gcd(x,y) = {gcd(x,y)}')
