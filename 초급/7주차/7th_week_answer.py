# Ai반 2기 - 7주차 정규수업(16:30~18:30) answer

## while 반복문
## : "조건"에 대한 반복문
## [문법] while 조건:
##          반복할 문장
## while문 연습문제1: 기본적인 활용
'''
i = 1
while i <= 3:
    print(f"{i} 꼬마")
    i += 1      # i = i + 1
    if i == 4:
        break
print('인디언!')
'''

## while문 연습문제2: 무한루프와 break를 활용하여 게임 시작메뉴를 만들어보자
'''
while True:
    choose = int(input("1을 입력하여 게임을 종료하세요>> "))
    if choose == 1:
        break
print("끝")
'''

## while문 연습문제3: continue
## : continue 문을 활용하여 1~10까지 숫자 중 홀수만 출력하는 프로그램 작성
'''
num = 0
while num < 10:
    num += 1            # num = num + 1
    if num % 2 == 0:
        continue
    print(num, end=' ')
'''

## 반복문 mission1-1: 원하는 단의 구구단만 출력하기
## for 반복문을 활용하여 출력을 원하는 구구단의 단 수를 입력받고, 1~9까지 곱한 구구단 출력하기
'''
num = int(input("구구단 단 수를 입력하세요>>"))
for i in range(1,10):
    print("%d * %d = %d" %(num, i, num*i))
'''

## 반복문 mission1-2: 2~9단 모두 출력하기
## for 반복문을 활용하여, 2단~9단까지 모두 출력하기
'''
print("[구구단 전체 출력]")
for i in range(2,10):
    print("[%d단]" %i)
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j))
    print("------------------")
'''

## 반복문 mission2-1: while문을 활용하여 반복문 mission1-1과 같은 결과를 출력해보자
'''
num = int(input("구구단 단 수를 입력하세요>>"))
i = 1
while i<10:
    print("%d * %d = %d" %(num, i, num*i))
    i += 1
'''

## 반복문 mission2-2: while문을 활용하여 반복문 mission1-2와 같은 결과를 출력해보자.
'''
print("[구구단 전체 출력]")
i = 2
while i<10:
    print("[%d단]" % i)
    j = 1
    while j<10:
        print("%d * %d = %d" %(i,j,i*j))
        j += 1
    print("---------------")
    i += 1
'''

## 반복문 mission3: 영단어 타자연습 프로그램
# -영타연습 Program-
# 1. 연습할 영단어가 담긴 리스트를 만든다.
# 2. 리스트에서 순서대로 단어를 가져와 화면에 출력한다
# 3. 프로그램 사용자는 단어를 그대로 입력한다.
# 4. 입력이 끝나면 전체 문제, 맞은 문제, 틀린 문제의 수가 출력된다.
'''
word_list = ['study', 'pizza', 'overwatch', 'I love chicken']

print("Let's Leanring English")
score = 0
for word in word_list:
    print(word)
    data = input()
    if word == data:
        score += 1

print("전체 문제 개수:", len(word_list))
print("맞힌 문제 개수:", score)
print("틀린 문제 개수:", len(word_list)-score)
'''

## 반복문 mission4-1: turtle을 활용한 미디어아트1
'''
import turtle as t

t.title("turtle을 활용한 미디어아트1")
t.bgcolor('black')
t.pencolor('yellow')
t.speed(0)

for i in range(500):
    t.forward(i)
    t.right(89)
t.mainloop()
'''
## 반복문 mission4-2: turtle을 활용한 미디어아트
'''
import turtle as t

color = ['red', 'yellow', 'green', 'blue']
t.title("turtle을 활용한 미디어아트1")
t.bgcolor('black')
t.speed(0)

for i in range(500):
    t.pencolor(color[i%4])
    t.forward(i)
    t.right(89)
t.mainloop()
'''
## 반복문 mission5-1: turtle을 활용한 미디어아트2
'''
import turtle as t

n = 60
t.bgcolor('black')
t.color('green')
t.speed(0)

for i in range(n):
    t.circle(80)
    t.left(360/n)
t.mainloop()
'''

