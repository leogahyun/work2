class Ani:
    jong = "종류"
    legs = 0
    color = "색깔"
    
    def enter(self):
        self.jong = input("종을 입력하세요")
        self.legs = int(input("다리 갯수를 입력하세요"))
        self.color = input("색깔을 입력하세요")
    
a1 = Ani()
b1 = Ani()
a1.enter()
b1.enter()
print(a1.jong,a1.legs,a1.color)
print(b1.jong,b1.legs,b1.color)

