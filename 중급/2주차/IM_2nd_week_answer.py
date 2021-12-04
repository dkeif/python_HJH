# Ai반 2기 python 중급반 - 2주차 정규수업(16:30~18:30) answer

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 16p참고
'''
# draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    :return:
    """
    # 설정
    rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    t.pensize(pen_size)

    # 그리기
    for i in range(7):
        t.setheading(90)
        t.penup()
        t.setpos(x+(rainbow_size / 2 - i * pen_size), y)
        t.pencolor(rainbow_color[i])
        t.pendown()
        t.circle((rainbow_size / 2 - i * pen_size), 180)

import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

draw_rainbow(t, 500, 30, 200, 200)
draw_rainbow(t, 500, 30, -100, -150)
draw_rainbow(t, 100, 8, 100, 100)
draw_rainbow(t, 200, 10, -20, -300)
draw_rainbow(t, 180, 15, 200, -40)
draw_rainbow(t, 100, 5, -50, 70)
draw_rainbow(t, 80, 3, -200, -100)
draw_rainbow(t, 50, 3, -100, -100)
draw_rainbow(t, 50, 3, 70, -30)

turtle.mainloop()
'''

## [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값고 자료형을 출력해보자.
'''
numbers1 = (4, 5, 6, 7)
numbers2 = 1, 2, 3, 4
print(numbers1, type(numbers1))
print(numbers2, type(numbers2))
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
'''
num1 = (77)
num2 = (77,)
num3 = 77
num4 = 77,
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))
'''
## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.
'''
numbers = (100, 110, 10)
numbers = list(numbers)
print(numbers, type(numbers))
numbers = tuple(numbers)
print(numbers, type(numbers))
'''
## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
'''
a = 7
b = 8
numbers = a, b
print("numbers:", numbers, type(numbers))
c, d = numbers
print("c: ", c, type(c))
print("d: ", d, type(d), end='\n\n')

print("a: ", a)
print("b: ", b)
a, b = b, a         
print("a: ", a)
print("b: ", b)
'''

