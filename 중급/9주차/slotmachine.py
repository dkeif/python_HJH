import random

def RandomNumber():
    num1 = random.randint(33, 39)
    num2 = random.randint(33, 39)
    num3 = random.randint(33, 39)
    return num1, num2, num3

def SlotMachine():
    num1, num2, num3 = RandomNumber()
    coin = input('<Slot Machine>\n코인을 넣어주세요! 1.코인넣기//2.그만히기>>')
    try:
        user_answer2 = int(coin)
    except ValueError:
        print('잘못 입력하셨습니다')
    if int(coin) == 1:
        print("%c"%chr(num1))

print('[SlotMachine GAME]')
main = input('1.게임시작//2.나가기>>')

try:
    user_answer = int(main)
except ValueError as e:
    print('잘못 입력하셨습니다')
if int(main) == 1:
    print('와')