class Ani:
    def __init__(self,name,nums,furcolor):
        self.jong = name
        self.legs = nums
        self.color = furcolor

    def pp(self):
        print(self.jong,self.legs,self.color)
        
a1 = Ani("강아지",4,"누렁이")
b1 = Ani("새",2,"노랑")
a1.pp()
b1.pp()