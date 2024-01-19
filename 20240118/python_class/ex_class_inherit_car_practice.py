# 차 객체 먼저 생성
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"{self.year}년 {self.make}제조 {self.model} 모델")

    def read_odometer(self):
        print("현재 차의 거리수는" + str(self.odometer_reading) + "KM입니다.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("키로수는 초기화가 불가능합니다.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def forward(self):
        print("주행중입니다.")

    def backward(self):
        print("후진중입니다.")

    def stop(self):
        print("차를 정지하겠습니다.")

# 자동차 객체 생성
my_car = Car('audi', 'a4', 2019)

# 차를 생성했습니다. 하지만 근 미래에는 자율주행 자동차가 만들어지고 상용화됩니다.
# 차인 것은 동일하나 자율 주행이 가능한 기능이 추가되었습니다.
# 해당 기능을 추가한 새로운 차 클래스 AutoGuidedCar 를 만들고 기존 차기능을  상속합니다.
# 추가를 원하는 기능은 scanNearEnvironment, automaticallyGotoDestination 입니다.
class AutoGuidedCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        message = "이 차의 가용거리는" + str(range)
        message += "KM입니다."
        print(message)

    def scanNearEnvironment(self):
        print("Scanning near environment...")

    def automaticallyGotoDestination(self):
        print("Automatically navigating to destination...")

# 자율 주행 자동차 객체 생성
my_auto_car = AutoGuidedCar('tesla', 'model s', 2019)

my_auto_car.describe_battery()
my_auto_car.get_range()
my_auto_car.scanNearEnvironment()
my_auto_car.automaticallyGotoDestination()
my_auto_car.read_odometer()

# 더 먼 미래에는 자동주행기능에 하늘을 나는 기능을 탑재한 차가 상용화됩니다.
# FlyCar 클래스를 기존의 자율주행차 클래스를 상속 받은 후, 차가나는 기능을
# 추가하고 주변 향공기 탐색기능인 scanNearAirpline 기능을 추가합니다.
class FlyCar(AutoGuidedCar):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.wing_state = 100

    def scanNearAirplane(self):
        print("Scanning near airplanes...")

    def landCarlikeAirpline(self):
        print("Landing carlike airplane...")

    def takeOffCar(self):
        print("Taking off car...")

    def checkWingState(self):
        if self.wing_state == 0:
            print("Wing state is 0, please check the wing state.")
        else:
            print("Wing state is normal.")

futurecar = FlyCar('tesla', 'model x', 2020)
futurecar.describe_battery()
futurecar.get_range()
futurecar.scanNearEnvironment()
futurecar.scanNearAirplane()
futurecar.automaticallyGotoDestination()
futurecar.read_odometer()
futurecar.landCarlikeAirpline()
futurecar.takeOffCar()

