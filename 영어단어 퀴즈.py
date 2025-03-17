import random

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