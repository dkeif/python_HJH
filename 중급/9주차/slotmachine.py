import random

def SlotMachine():
    inputcoin = int(input('코인을 넣어주세요! 1.코인넣기//2.그만히기>>'))
    if inputcoin == 2:
        quit()

main = input('1.게임시작//2.나가기>>')
if main == 1:
    SlotMachine()
elif main == 2:
    quit()
try:
    user_answer = int(main)
except ValueError as e:
    print('잘못 입력하셨습니다')