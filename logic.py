# 마방진 만들기
def magicSquare(num):

    arr = []  # 배열 생성
    for i in range(num):  # n개만큼의 이차원배열 생성을 위한 루프
        arr.append([0]*num)  # 0으로 초기화

    # 시작을 위한 위치 설정
    sx = 0
    sy = int(num/2)
    # 시작위치에 1을 넣고 시작
    arr[sx][sy] = 1

    # 오른쪽, 위의 위치에 값이 있을경우 되돌아오기위3해 위치를 넣을 변수 생성
    x = 0
    y = 0

    # 마방진 생성 루프
    for i in range(2, num*num+1):
        x = sx
        y = sy

        sx -= 1
        sy += 1

        if(sx < 0):
            sx = num-1

        if(sy > num-1):
            sy = 0

        if(arr[sx][sy] == 0):
            arr[sx][sy] = i
        else:
            sx = x+1
            sy = y
            arr[sx][sy] = i
    return arr
