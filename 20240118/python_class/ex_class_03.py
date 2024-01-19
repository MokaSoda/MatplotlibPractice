# ----------------------------------------------
# 2차원 점 클래스 이름 Point2D
# 클래스 속성 : x, y, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# ----------------------------------------------

class Point2D:
    def __init__(self, x, y, color='black', shape='o', size=1):
        print(f"Point2D class is created.")
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    def draw(self):
        print(f"Point2D({self.x}, {self.y}) is drawn.")

    def erase(self):
        print(f"Point2D({self.x}, {self.y}) is erased.")

    def print_info(self):
        print(f"Point2D({self.x}, {self.y})\ncolor={self.color}\nshape={self.shape}\nsize={self.size}")

# ----------------------------------------------
# 3차원 점 클래스 이름 Point3D
# 클래스 속성 : x, y, z, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# 클래스 상속 : Point2D 를 상속받아 클래스 구현
# ----------------------------------------------

class Point3D(Point2D):
    def __init__(self, x, y, z, color='black', shape='o', size=1):
        print("Point3D class is called.")
        super().__init__(x, y, color, shape, size)
        self.z = z

    def print_info(self):
        print(f"Point3D({self.x}, {self.y}, {self.z})\ncolor={self.color}\nshape={self.shape}\nsize={self.size}")

    def draw(self):
        print(f"Point3D({self.x}, {self.y}, {self.z}) is drawn.")

    def erase(self):
        print(f"Point3D({self.x}, {self.y}, {self.z}) is erased.")

# ----------------------------------------------
# 4차원 점 클래스 이름 Point4D
# 클래스 속성 : x, y, z, a, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보출력
# 클래스 상속 : Point3D 를 상속받아 클래스 구현
# ----------------------------------------------

class Point4D(Point3D):
    def __init__(self, x, y, z, a, color='black', shape='o', size=1):
        print("Point4D class is called.")
        super().__init__(x, y, z, color, shape, size)
        self.a = a

    # 메서드 오버라이딩으로 부모관계의 메서드가 실행되지 않고 직접 정의된 메서드가 실행됨
    def print_info(self):
        print(f"Point4D({self.x}, {self.y}, {self.z}, {self.a})\n"
              f"color={self.color}\n"
              f"shape={self.shape}\n"
              f"size={self.size}")

    def draw(self):
        print(f"Point4D({self.x}, {self.y}, {self.z}, {self.a}) is drawn.")

    def erase(self):
        print(f"Point4D({self.x}, {self.y}, {self.z}, {self.a}) is erased.")

    #폴리모피즘 예시
    def __str__(self):
        return f"Point4D({self.x}, {self.y}, {self.z}, {self.a})"



# 테스트
p1 = Point2D(10, 20, '검정', '사각형', 10)
p1.draw()
p1.print_info()
p1.erase()

p2 = Point3D(10, 20, 30, '빨강', '원', 10)
p2.draw()
p2.print_info()
p2.erase()


p3 = Point3D(20, 30, 40, '파랑', '동그라미', 30)
p4 = Point4D(30, 40, 50, 60, '노랑', '세모', 20)
p4.draw()

print(str(p4))
