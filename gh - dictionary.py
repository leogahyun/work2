que = ["teacher","student","milk","apple"]
ans = ["교사","학생","우유","사과"]

que1 = "student"
ans1 = "학생"
for i in range (4):
    print(que[i],"는 무슨 뜻입니까?")
    a = input()

    if ans[i] == a :
        print("정답입니다")