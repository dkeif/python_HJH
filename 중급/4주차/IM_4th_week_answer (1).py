# Ai반 2기 python 중급반 - 4주차 정규수업(16:30~18:30) answer

# [클래스(class)]
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## case1: class를 활용하지 않은 경우
'''
character1_name = "레넥톤"
character1_health = 575
character1_attack = 69
character1_speed = 345

print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character2_name = "리신"
character2_health = 575
character2_attack = 70
character2_speed = 345

print(f"{character2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

## 여기에서 캐릭터를 하나 더 추가해보자.
character3_name = "오른"
character3_health = 590
character3_attack = 69
character3_speed = 335

print(f"{character3_name}님 소환사의 협곡에 오신 것을 환영합니다.")


## 캐릭터의 이름과 기본 공격력(attack)을 출력하는 함수를 정의하여 세 캐릭터의 공격력을 출력해보자
def basic_info(name, attack, health, speed):
    print(f"[{name}]")
    print(f"기본공격력: {attack}")
    print(f"기본체력: {health}")
    print(f"기본속도: {speed}")


basic_info(character1_name, character1_attack, character1_health, character1_speed)
basic_info(character2_name, character2_attack, character2_health, character2_speed)
basic_info(character3_name, character3_attack, character3_health, character3_speed)

print("=========클래스를 사용한 경우==========")
'''

## case2: 클래스를 사용한 경우
'''
class Character:
    def __init__(self, name, attack, health, speed):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        print(f"{self.name}님 소환사의 협곡에 오신 것을 환영합니다.")

    def basic_info(self):
        print(f'[{self.name}]')
        print(f'기본공격력: {self.attack}')
        print(f'기본체력: {self.health}')
        print(f'기본속도: {self.speed}')


renekton = Character("레넥톤", 69, 575, 345)
leesin = Character("리신", 70, 575, 345)
ornn = Character("오른", 69, 590, 335)  ## 역시 하나의 챔피언 추가

# 챔피언 정보 출력하기
renekton.basic_info()
leesin.basic_info()
ornn.basic_info()
'''
# [class]
## <class 생성 및 호출>
## <class 생성 문법>
## class 클래스 이름:
##     def 메서드 이름1(self, 입력변수1, 입력변수2, ...):
##         실행명령
##     def 메서드 이름2(self, 입력변수1, 입력변수2. ...):
##         실행명령

## <class 호출 문법>
## 클래스 선언하기: 인스턴스 = 클래스이름()
## 매서드 호출하기: 인스턴스.메서드()

## 연습문제2: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자
'''
a = 12
b = 0.125
c = '안녕하세요'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a.__dir__())
print(b.__dir__())
print(c.__dir__())
print(d.__dir__())
'''

## class Mission1
## : Mission에 언급된 내용대로 Cat class를 만들어 보자
'''
class Cat():
    def cry(self):
        print("야옹!")
    def tail_wag(self):
        print("야옹! 야옹!!")
    def translate_cry(self):
        print("하찮은 닝겐! 나에게 밥을 대령해라!")
    def translate_tw(self):
        print("심심하다! 특별히 나와 놀게 해주겠다 닝겐!")

# 객체 생성 후 매서드 호출하기
siamese = Cat()

siamese.cry()
siamese.tail_wag()
siamese.translate_cry()
siamese.translate_tw()
'''

