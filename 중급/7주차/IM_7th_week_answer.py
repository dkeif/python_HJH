# Ai반 2기 python 중급반 - 7주차 정규수업(16:30~18:30) answer

## class Mission: 아이템 구성안과 설계도를 활용하여, class와 객체를 생성해 보자
## 이때, 부모 클래스: Item // 자식 클래스: WearableItem, UsableItem 이다.
'''
## 아이템 클래스
## 모든 아이템들의 아이템 수를 500개로 제한한다.(클래스 변수)
class Item:
    Item_num = 500
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def display_ItemInfo(self):
        print(f"<[{self.name}] 정보>")
        print(f"가격: {self.price}")
        print(f"무게: {self.weight}")
        print(f"버리기 가능여부: {self.isdropable}")
    def sale(self):
        print(f'[{self.name}]의 가격: {self.price}Gold')
        while True:
            sale_choose = int(input("물건을 판매하시겠습니까?(1.판매//2.취소)>>"))
            if sale_choose == 1:
                print(f"[{self.name}]의 판매가 완료되었습니다. {self.price}가 지급됩니다.")
            elif sale_choose == 2:
                print("거래가 취소되었습니다.")
            else:
                print("잘못된 입력입니다.")
            if sale_choose == 1 or sale_choose == 2:
                break
    def discard(self):
        while True:
            discard_choose = int(input("아이템을 버리시겠습니까?(1.버리기//2.취소)>>"))
            if not self.isdropable:
                print("버릴 수 없는 아이템 입니다.")
                break
            else:
                if discard_choose == 1:
                    print(f"[{self.name}]을 버립니다.")
                elif discard_choose == 2:
                    print("버리기를 취소합니다.")
                else:
                    print("잘못된 입력입니다.")
                if discard_choose == 1 or discard_choose == 2:
                    break

## 장비 아이템 클래스
class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        while True:
            wear_choose = int(input("장비를 착용합니까?(1.착용/2.취소)>> "))
            if wear_choose == 1:
                print(f"[{self.name}]을 착용하였습니다. 효과 '{self.effect}'이(가) 적용됩니다.")
            elif wear_choose == 2:
                print("취소되었습니다.")
            else:
                print("잘못된 입력입니다.")
            if wear_choose == 1 or wear_choose == 2:
                break

# 소모품 아이템 클래스
class UsableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        while True:
            use_choose = int(input("아이템을 사용하시겠습니까?(1.사용/2.취소)>> "))
            if use_choose == 1:
                print(f"[{self.name}]을 사용합니다. 효과 '{self.effect}'이(가) 적용됩니다.")
            elif use_choose == 2:
                print("취소되었습니다.")
            else:
                print("잘못된 입력입니다.")
            if use_choose == 1 or use_choose == 2:
                break

# 객체 생성(각 객체 생성 및 테스트)
iron_armor = WearableItem("철갑옷", 2000, 40, True, "방어력+100")
iron_armor.display_ItemInfo()
iron_armor.wear()
iron_armor.sale()
iron_armor.discard()

flame_sword = WearableItem("플레임 소드", 5000, 5, False, "공격 시, 화염 속성 추가 데미지")
flame_sword.display_ItemInfo()
flame_sword.wear()
flame_sword.sale()
flame_sword.discard()

aqua_shoes = WearableItem("아쿠아슈즈", 4000, 3, True, "물 속성 내성")
aqua_shoes.display_ItemInfo()
aqua_shoes.wear()
aqua_shoes.sale()
aqua_shoes.discard()

raspberry = UsableItem("산딸기", 50, 0.1, True, "체력 50 증가")
raspberry.display_ItemInfo()
raspberry.use()
raspberry.sale()
raspberry.discard()

red_potion = UsableItem("빨간 포션", 100, 0.2, True, "체력 100 회복")
red_potion.display_ItemInfo()
red_potion.use()
red_potion.sale()
red_potion.discard()

blue_potion = UsableItem("파란 포션", 150, 0.2, True, "마력 150 회복")
blue_potion.display_ItemInfo()
blue_potion.use()
blue_potion.sale()
blue_potion.discard()

Goddess_Tear = UsableItem("여신의 눈물", 90000, 0.1, False, "30분 동안 파티원들의 모든 능력치가 80% 증가합니다.")
blue_potion.display_ItemInfo()
blue_potion.use()
blue_potion.sale()
blue_potion.discard()
'''

# [예외처리]
# : 프로그램 실행 중에 발생하는 예외를 미연에 방지하는 것.

## 예외처리가 필요한 이유 예시:  계산기 프로그램
'''
num1 = float(input("첫번짼 숫자를 입력해주세요.(숫자로 입력해주세요)>>"))
num2 = float(input("두번째 숫자를 입력해주세요.(숫자로 입력해주세요)>>"))
result = num1 + num2
print('결과: ', result)
'''
## 예외처리 연습문제: 환율 계산 문제

won = input('원화 금액을 입력하세요>>')
dollar = input('달러 금액을 입력하세요>>')

try:
    print(int(won)/int(dollar))
except ValueError as e:
    print("문자열 예외가 발생하였습니다.", e)
except ZeroDivisionError as e:
    print("나누기 0은 불가능 합나다.", e)
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("예외가 발생하건, 하지 않건 무조건 실행하는 코드 입니다.")


## 에러 발생시키기 연습문제
'''
string = input("입력>>")
if string == "까마귀 날자":
    raise Exception("배 떨어진다.")
'''

## 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자
'''
word_list = ['apple', 'banana', 'pitch']

count = 0
i = 0
print('[English word typing practice]')
while True:
    try:
        user_answer = input(word_list[i]+'\n')
    except:
        break
    if user_answer == word_list[i]:
        count += 1
    i += 1
print(f'전체 문제 수: {len(word_list)}')
print(f'맞은 문제 수: {count}')
print(f'틀린 문제 수: {len(word_list)-count}')
'''

