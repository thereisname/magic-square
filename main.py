# from flask import Flask, render_template, request
from logic import magicSquare
import os
import sys
import time


# app = Flask("magic square")

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/show")
# def show():
#     magic = []
#     num = request.args.get('num')
#     num = int(num)
#     if num % 2 == 0:
#         return render_template("index.html")
#     else:
#         magic = magicSquare(num)
#         return render_template("show.html", magic=magic, num=num)

# app.run()
def question():
    while True:
        try:
            reString = (input('계속 하시겠습니까? (y/n) > '))
            if reString == 'y' or reString == 'Y':
                os.system('cls')
                return
            elif reString == 'n' or reString == 'N':
                sys.exit()
            else:
                print('알맞은 값을 입력하시오.')
        except ValueError:
            print('다시 입력해주세요.')


def start():
    print('*** magic square ***\n')

    print()
    num = input('계속하려면 아무 키나 누르십시오...')


num = 0
start()
while True:
    os.system('cls')
    try:
        num = int(input('원하는 크기의 사이즈를 입력하시오 > '))
        if num % 2 != 0 and num > 1:
            magic = magicSquare(num)
            for i in range(num):
                for j in range(num):
                    print('{0:5d}'.format(magic[i][j]), end='')
                print()
            question()
        else:
            print('1보다 큰 홀수만 입력하시오.')
            time.sleep(1)

    except ValueError:
        print('정수를 입력하시오.')
        time.sleep(1)
