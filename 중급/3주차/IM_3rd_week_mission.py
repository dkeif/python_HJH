# Ai반 2기 python 중급반 - 3주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!

[저번주 복습]
1. 함수 mssion: 거북이 무지개 함수 만들기
2. tuple 생성 및 제어와 연습문제 풀이
'''

# [튜플(tuple)]
## 연습문제5: 튜플과 관련된 함수
## ※ 결과 확인이 중요!!
'''
numbers = 100, 546, 896, 10, 777, 30, 4, 78, 546, 10
print(max(numbers))         # max(): 튜플에서 최댓값을 반환하는 함수
print(min(numbers))         # min(): 튜플에서 최솟값을 반환하는 함수
print(sum(numbers))         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print(numbers.count(10))         # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print(numbers.index(777))         # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)
'''

## [딕셔너리]
## : 키(key)와 데이터(value)를 가지고 있는 "사전과 같은 자료형"
## key값을 통해 value값을 불러올 수 있다.

## 연습문제1: 딕셔너리 만들기
## : 자신이 좋아하는 youtuber 채널이름(key)과 구독자 수(value)를 말해보자.
##   그리고, 모두가 말한 youtuber들의 이름과 구독자수로 dictionary 자료형을 만들어보자.
##   만약, 남은 시간이 얼마 없다면, 미리 작성해놓은 데이터를 사용하도록 하자
'''
youtuber = {
    '승우아빠':1540000,
    '비웬':120000,
    'aespa':2910000,
    '긱블':782000,
    '찬사':4940,
    '오킹':1540000,
    '로보티즈노원':15
}
print(youtuber)
print((type(youtuber))) #dict

## 연습문제2: 딕셔너리 제어1-값에 접근하기
## : 자신이 가장 좋아하는 youtuber의 구독자 수를 출력해보자

print(youtuber['긱블'])     # ()안에 값에 접근하는 문장 넣어주기

## 연습문제3: 딕셔너리 제어2-값 할당(or 수정)하기
## : 자신이 가장 좋아하는 유투버의 구독자 수에 1000이 더 큰 숫자를 넣고 이를 출력해보자

youtuber['긱블'] = 782001          # 딕셔너리 값 할당 명령 수행
print(youtuber["긱블"])

## 연습문제3: 딕셔너리 제어3-삭제하기
## : 자신이 두번째로 좋아하는 youtuber를 딕셔너리에서 삭제해보자

del youtuber['긱블']                              # 딕셔너리 값 지우기 명령 수행
print(youtuber)

## 연습문제4: 딕셔너리 관련 함수
## .items(), .keys(), .values()의 결과와 데이터 타입을 출력해보자
## ※ 결과 확인이 중요!!
print("딕셔너리 함수")
print(youtuber.items())     # .items(): key와 value 쌍을 반환하는 함수
print(youtuber.keys())     # .keys(): 원소가 key로 이루어진 데이터를 포함하는 list를 반환하는 함수
print(youtuber.values())     # .values(): 원소가 value로 이루어진 데이터를 포함하는 list를 반환하는 함수
'''

# [클래스(class)]
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## case1: class를 활용하지 않은 경우
# 정보 출력 함수 정의
'''
# character_info() 함수 정의하기
def character_info(name, attack, health, speed):
    # name 출력
    # 기본 공격력(attack) 출력
    # 기본 체력(health) 출력
    # 기본 속도(speed) 출력

# character1 만들어주기(정보 할당)
    ## character1의 name 정의
    ## character1의 attack 정의
    ## character1의 health 정의
    ## character1의 speed 정의
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

# <character_info()를 호출하여 character1의 정보 출력하기 >

# character2 만들어주기(정보 할당)
    ## character1의 name 정의
    ## character1의 attack 정의
    ## character1의 health 정의
    ## character1의 speed 정의
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character_info(character2_name, character2_attack, character2_health, character2_speed)
'''
## >> 캐릭터를 하나 만들 때마다 작성해야 하는 코드가 많고 복붙해서 수정하기도 귀찮다...

## case2: 클래스를 사용한 경우
# Character class 정의해주기
    # 생성자 정의 - name, attack, health, speed 입력
        # self.name
        # self.attack
        # self.healrh
        # self.speed
        # 소환사 협곡! 환영!

    # character_info() 메서드 정의
        # name 출력
        # attack 출력
        # health 출력
        # speed 출력

# 첫번째 캐릭터 만들기
# 두번째 캐릭터 만들기

# 첫번째 캐릭터의 character_info() 메서드 호출
# 두번째 캐릭터의 character_info() 메서드 호출

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

## 연습문제: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자
'''
a = 12              # int
b = 0.125           # float
c = '안녕하세요'      # str
d = True            # bool

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
<Cat class 만들기!>
'''

## <생성자>
## : 객체가 생성될 때 자동으로 호출되는 메서드.
## [문법] class 클래스이름:
##           def __init__(self, 입력변수들):
##               초기화 실행 문장

## 생성자 연습문제
## : Monster 클래스를 만들고 step에 따라 생성자와 메서드가 추가된 Monster 클래스를 만들어보자.
## step1) 가장 기본적인 Monster 클래스를 만들어 보자
##        : say 메서드만을 가지는 Monster 클래스
'''
<Moster class 만들기>

<Monster 객체 생성 및 say 메서드 호출하기>
'''
## step2) Monster 클래스에 속성(name, health, attack, speed)을 추가하여 초기화해보자.
##        또한, 인스턴스 생성 시에 say의 내용이 출력되도록 만들어보자.
'''
<step1)에서의 Monster class 생성자의 속성 추가>

<goblin 객체 만들기(Monster 객체)>
'''

## step3) Monster 클래스에 메서드(decrease_health, get_health, info)를 추가한 후,
##        goblin과 wolf 객체를 생성하여 각 메서드들을 호출해보자.
'''
<Monster 객체에 여러가지 메서드 추가하기 >

<golblin과 wolf를 Monster 객체로 선언하고 메서드 호출하기>
'''

## <상속>
## : 부모 클래스의 속성과 메서드를 자식클래스가 물려받을 수 있도록 만든 기능
## 상속을 사용하는 이유: 클래스들에 중복된 코드를 제거하고 유지보수를 하기 위해 사용하기 위해서 사용.

## <메서드 오버라이딩(덮어쓰기)>
## : 부모 클래스에 있는 메서드를 자식클래스에서 동일한 이름으로 다시 만드는 것

## 상속 연습문제
## :Monster 클래스를 만들고, 상속을 활용하여 Wolf, Shark, Dragon 클래스를 만들어,각각의 객체를 생성해보자.
##
## step1) 부모 클래스: Monster 클래스 정의하기
## - 속성: name, health, attack
## - 메서드: move("self.name 지상에서 이동하기"를 출력하는 메서드, 이후 해당 몬스터의 이동방법이 출력되도록 할 것임.)
'''
<Monster class 작성하기>
'''

## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
<Moster class를 상속받은 Wolf, Shark, Dragon class 작성하기>

<각 class들로 객체 만든 후, move 메서드 호출하기>
'''

