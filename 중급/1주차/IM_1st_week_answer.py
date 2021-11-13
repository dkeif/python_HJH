# Ai반 2기 python 중급반 - 1주차 정규수업(16:30~18:30) answer

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값

## docstring: 함수에 대한 설명을 나타내는 문장

## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
def DrawStar_100():
    """한 변의 길이가 100인 별모양 그리기 함수"""
    for i in range(4):
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.left(72)

win = turtle.Screen()
DrawStar_100()
win.mainloop()
'''

## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
def DrawStar(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.left(72)

win = turtle.Screen()
DrawStar(5)
win.mainloop()
'''
## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
def getRandomNum():
    return random.randint(1, 100)

num = getRandomNum()
print(num)
'''
## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
def add(x, y):
    return x+y

X = add(55, 78)
print(X)
'''

