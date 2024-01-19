class Star:
    # 최상위 부모 클래스인 object 에서부터 상속받은 함수들
    # def __finalize__(self):
    #     print("finalize")
    # def __del__(self):
    #     print("del")
    # # def __init__(self, *args, **kwargs):
    # #     print("init")
    # def __new__(cls, *args, **kwargs):
    #     print("new")
    # 클래스 변수
    count = 0
    # 클래스 필드 속성, 해당 클래스로 생성된 객체(인스턴스가)가 공유하는 속성
    timezone = 'night'

    # 기존에 있는 함수를 자신의 입맛에 맞게 수정하는 것
    # 오버라이딩
    def __init__(self, size, color, brightness):
        print("초기 색상 = " + color)
        # 힙 영역의 각 속송의 주소들을 저장함
        self.size = size
        self.__color = color
        self.brightness = brightness

    def twinkle(self):
        original = self.brightness
        self.brightness /= 2
        print(f"{self.__color}별 " + "반짝임")
        print(self.brightness)
        self.brightness = original
        print(self.brightness)

    def fall(self):
        print(f"{self.__color}별 " + "떨어짐")
        self.brightness = 0

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def del_color(self):
        del self.__color


# 별 인스턴스 생성
star1 = Star(10, "yellow", 3)
star2 = Star(5, "white", 2)
yourStar = Star(100, "red", 100)

# 별 크기, 색상, 밝기 변경
star1.size = 15
star1.__color = "blue"
print(f"스타1 {star1.__color}")
star1.brightness = 4
print(star1.get_color() , '내부 입니다.')


# 별 메서드 사용
star1.twinkle()  # 반짝임
star2.fall()  # 떨어짐
yourStar.twinkle()  # 반짝임
print(star2.timezone)

Star.__dict__


