# Ai반 2기 - 8주차 정규수업(16:30~18:30) answer

## 반복문 mission5-2: turtle을 활용한 미디어아트2
'''
import turtle as t

n = 60
color = ['red', 'yellow', 'green', 'blue']
t.bgcolor('black')
t.speed(0)

for i in range(n):
    t.circle(80)
    t.color(color[i%4])
    t.left(360/n)
t.mainloop()
'''


# [반복문 추가 문제]
## 이중 for문 연습문제(warming-up)
## : 이중 for문을 활용하여 높이5의 직각삼각형 만들기
'''
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print("")
'''

## 반복문 추가문제 Mission1: Up-Down 게임 만들기(feat. random 함수)
## >> random 함수를 활용하여 1~100까지의 숫자를 생성하고 up-down 게임 만들어보기
'''
import random

print("[Up-Down Game]")
random_num = random.randint(1, 100)
while True:
    your_num = int(input("숫자를 입력하세요>> "))
    if random_num == your_num:
        print("정답입니다~~!")
        break
    elif random_num < your_num:
        print("Down")
    else:
        print("Up")
'''

## 반복문 추가문제 Mission3: turtle 모듈을 활용하여 무지개 만들기
### for 반복문 Mission2: turtle 모듈을 활용하여 무지개 만들기
'''
import turtle
# 변수 및 객체 선언
win = turtle.Screen()
t = turtle.Turtle('turtle')
t.shapesize(10)
rainbow_size = 500         # 무지개 크기(너비)
pen_size = 30              # 펜 굵기
rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']      # 활용할 색상 지정
t.speed(10)                # 거북이 속도 설정 (1~10 숫자가 클수록 빠름, but 0은 가장 빠른 속도)

# 펜 초기 설정
t.pensize(pen_size)

# for 반복문 실행(무지개 그리기)
for i in range(7):
    t.setheading(90)
    t.penup()
    t.setpos(rainbow_size/2 - i*pen_size, 0)
    t.pencolor(rainbow_color[i])
    t.pendown()
    t.circle(rainbow_size/2 - i*pen_size, 180)

turtle.mainloop()
'''



