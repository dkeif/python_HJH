# Ai반 2기 python 중급반 - 8주차 정규수업(16:30~18:30) answer

# [파일 입출력]
## 파일 입출력 연습문제1: 파일 쓰기(w: 새로쓰기 혹은 덮어쓰기)
'''
file = open('D:/My_file/Github_asdfrv20/Python_deep/file_make.txt', 'w', encoding="utf-8")
for i in range(1, 11):
    file.write(f"{i}번째 줄 입력입니다.\n")
file.close()
'''
## 파일 입출력 연습문제2: 파일 추가하기(a: 추가하기)
'''
file = open(r'D:\My_file\Github_asdfrv20\Python_deep\file_make.txt', 'a', encoding="utf-8")
for i in range(11, 21):
    file.write(f"{i}번째 줄 입력입니다.\n")
file.close()
'''

## 파일 입출력 연습문제3: 파일 읽기(r: 읽기)
## way1) readline 함수 사용(한 줄 씩 읽어오기)
'''
file = open('D:/My_file/Github_asdfrv20/Python_deep/file_make.txt', 'r', encoding="utf-8")
while True:
    data = file.readline()
    print(data, end='')
    if data == "":
        break
file.close()
'''
## way2) readlines 함수 사용(모든 줄을 읽어와, 각 줄을 리스트의 요소로 반환)
'''
file = open('D:/My_file/Github_asdfrv20/Python_deep/file_make.txt', 'r', encoding='utf-8')
data = file.readlines()
print(data)
for data_line in data:      # 출력
    print(data_line ,end='')
file.close()
'''
## way3) read 함수 사용(문서 전체를 하나의 문자열로 가져오기)
'''
file = open('D:/My_file/Github_asdfrv20/Python_deep/file_make.txt', 'r', encoding='utf-8')
data = file.read()
print(data)
file.close()
'''

# [이벤트 처리]
## turtle 마우스 이벤트 처리 연습문제

import turtle as t
import random

# randomColor 함수: 랜덤한 r,g,b 값을 반환하는 함수
def randomColor():
    r = random.random()     # random.random(): 0~1상이의 랜덤한 값 할당
    g = random.random()
    b = random.random()
    return r, g, b

# leftClick 핸들링 함수: 거북이 스탬프 모양을 찍는 함수
def turtleStamp(x, y):
    t.hideturtle()                          # 거북이 숨기기
    t.goto(x, y)                            # (x,y)좌표로 거북이 이동
    t.setheading(random.randint(0, 360))    # 랜덤하게 거북이의 머리 방향 지정(0~360도)
    t.shapesize(random.randint(1, 10))      # 랜덤하게 거북이의 크기 설정(1~10)
    r, g, b = randomColor()                 # 랜덤 r,g,b 값 가져오기(randomColor 함수 사용하기)
    t.fillcolor(r, g, b)                    # 스템프 색상 설정(랜덤 r,g,b 값 넣기)
    t.pencolor(r, g, b)                     # 스템프 테두리 색성 설정(랜덤 r,g,b 값 넣기)
    t.stamp()                               # 스템프 찍기 명령

t.title("거북이 도장찍기")
t.shape("turtle")           # 도장 모양을 turtle으로 설정
t.speed(0)                  # 속도 설정
t.penup()                   # 펜 들기

t.onscreenclick(turtleStamp, 1)

t.mainloop()


