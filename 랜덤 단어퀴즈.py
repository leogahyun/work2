import random

def gh() :
    d = {"teacher" : ["교사","쌤","선생님","스승님","스승"],
         "table" : ["책상","탁상","테이블","탁자","식탁"],
         "dog" : ["개","멍멍이","댕댕이","강아지"],
         "ocean" : ["바다","대양","해양"],
         "right" : ["오른쪽","권리","올바른","정확한"]}

    qlist = list(d.keys())
    random.shuffle(qlist)

    print("퀴즈게임을 시작합니다.")
    c = 0
    for i in qlist :
        a = input(f"{i}에 해당하는 뜻를 쓰시오")
        
        if a in d[i]:
            print("정답입니다")
            c=c+1
        else:
            print("오답입니다")
    print(f"총 5개 중에 {c}개 맞았습니다")
    
def sso() :
    d = {"animal" : ["cat","dog","pig","kitty"],
     "emotion" : ["angry","sad","glad"],
     "sport" : ["baseball","soccer"],
     "subject" : ["math", "Korean", "English"],
     "flavor" : ["spicy","sweet","salty"]}


    print("영단어 퀴즈 게임을 시작합니다.")
    c=0
    for i in d:
        a = input(f"{i}에 해당하는 영단어를 쓰세요.")
       
        if a in d[i]:
            print("정답입니다")
            c = c + 1
        else:
            print("오답입니다")
        print(i)
    print(f"총 {c}개 맞추었습니다")

print("""게임의 세계에 오신 걸 환영합니다.
      =========================
      메뉴
      1. 영단어의 한국어 뜻 맞추기
      2. 분야에 해당하는 영단어 맞추기
      """)

a = int(input("    메뉴를 선택하세요 : "))
if a == 1:
    gh()
elif a == 2:
     sso()
else:
     print("종료합니다.")
