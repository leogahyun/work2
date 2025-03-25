class Sing:
    def __init__(self):
        self.name = "가수명"
        self.nums = 0
        self.char = "랩"
    def enter(self):
        self.name = input("이름은?")
        self.age = int(input("나이는?"))
        self.char = input("특기는?")
    def output(self):
        print(f"이름은:{self.name},나이는:{self.age},특기:{self.char}")
    def main(self):
        num = int(input("몇명을 입력할래?"))
        slist = []

        for i in range(num):
            p1 = Sing()
            p1.enter()
            slist.append(p1)
        print("====================")
        print("최종명단출력")
        for singer in slist: 
            singer.output()
