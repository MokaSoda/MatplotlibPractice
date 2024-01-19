# ------------------------------
# 자동차 클래스
# 자동차의 기능
# ------------------------------
class Car:
    WHEEL = 4
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
        self.gas_amount = 0

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def add_gas(self, amount):
        self.gas_amount += amount

    def drive(self, distance):
        if self.gas_amount >= distance:
            self.gas_amount -= distance
        else:
            print("Not enough gas!")
# ------------------------------

car1  = Car("Tesla", "Model S", 2022)
car2  = Car("Hyundai", "Elantra", 2021)
car3  = Car("Kia", "Soul", 2022)


print(car1.brand)
print(car2.model)
print(car3.year)

car1.start()
car2.stop()
car3.add_gas(20)
car3.drive(100)

print(car1.is_running)
print(car2.is_running)
print(car3.gas_amount)


class Car:
    maker = "현대"

    # 생성자 메서드 (인스턴스 생성 매서드)
    def __init__(self, wheel, color, number, kind):
        self.wheel = "19인치"
        self.color = "레드"
        self.number = 1234
        self.kind = '세단'

    def driving(self, destination = '집'):
        print(f"{destination}에 {self.number}있는 차가 운전중입니다.")

    def stop(self):
        print(f"{self.number}번 차가 정지되었습니다.")

    def back(self):
        print(f"{self.number}번 차가 후진합니다.")

car1 =  Car("16인치", "검정", 1234, "세단")
car2 =  Car("16인치", "검정", 5678, "SUV")

print(car1.wheel)
print(car1.color)
print(car1.number)
print(car1.kind)

car1.driving()
car2.stop()
car2.back()
import random

# -----------------------------------------------
# class MBTI
# show 16 kinds of MBTI using class
class MBTI:

    mbtiList = ["INFJ", "ENFJ", "INFP", "ENFP", "INTJ", "ENTJ", "INTP", "ENTP", "ISTJ", "ESTJ", "ISTP", "ESTP", "ISFJ", "ESFJ", "ISFP", "ESFP"]
    def __init__(self):

        self.__mbti = random.choice(self.mbtiList)

    def show(self):
        print(self.__mbti)

    def __str__(self):
        return self.__mbti

    def __repr__(self):
        return self.__mbti

    @property
    def mmmm(self):
        return self.__mbti

    @mmmm.setter
    def mmmm(self, mbti):
        if mbti in self.mbtiList:
            self.__mbti = mbti
        else:
            print("INVALID MBTI")
    @mmmm.getter
    def mmmm(self):
        print(f"{self.__mbti} 입니다")
    @staticmethod
    def get_mbti_list():
        return MBTI.mbtiList

    @classmethod
    def set_random_mbti(cls):
        return random.choice(cls.mbtiList)

mbti1= MBTI()
print(mbti1.mmmm)
mbti1.mmmm = 1213
mbti1.mmmm = "INTP"
mbti1.__mbti = "INTF"
print(mbti1.mmmm)

# ---------------------------------------------
# 계산기만들기 : Calc
class Calc:
    brand = "Casio"
    def __init__(self, start = 0):
        self.year = 2022
        self.price = 20000
        self.__size = 1015
        # __ 설정시 클래스 밖에서 속성을 읽거나 쓰기 불가
        self.result = start

    def add(self, num):
        self.result += num

    def sub(self, num):
        self.result -= num

    def mul(self, num):
        self.result *= num

    def div(self, num):
        if num:
            self.result /= num
        else:
            self.result = '0으로 나누었습니다.'

    def mod(self, num):
        if num:
            self.result %= num
        else:
            self.result = '0으로 나누었습니다.'
    def show(self):
        print(self.size, "셀프사이즈")
        print(self.result, '셀프리조트')
        return self.result

    #메서드지만 속성의 읽기 쓰기 방식으로 접근할 수 있음
    @property
    def size(self):
        pass
    @size.getter
    def size(self):
        print("getter에서 불러짐")
        return self.__size
    @size.setter
    def size(self, value):
        if value > 0:
            self.__size = value
        else:
            print("크기가 0이거나 작습니다.")

# 인스턴스에서는 클래수 내부의 변수와 메서드를 모두 볼 수 있음
# 클래스 자체에서는 메서드는 보이나 self로 인해 실행이 안되며
# 클래스 내부 변수는 없는 상황이다
#


calc1 = Calc(-100)
# print(calc1.__size)
calc1.show()
calc1.add(-10)
calc1.show()
print(calc1.size)
calc1.add(1000)
print(calc1.size)
calc1.size = 11111
print(calc1.size)

# calc1 의 속성 읽기
calc1.add(-11111111)
print(calc1.size)
calc1.show()