import random

# 분야별 OX 퀴즈 문제 (문제, 정답, 해설)
quiz_data = {
    "인체": [
        {"question": "인체의 가장 큰 장기는 간이다. (O/X)", "answer": "X", "explanation": "인체의 가장 큰 장기는 피부입니다."},
        {"question": "성인의 뼈 개수는 206개이다. (O/X)", "answer": "O", "explanation": "성인의 뼈 개수는 일반적으로 206개입니다."},
        {"question": "인체에서 가장 강한 근육은 혀이다. (O/X)", "answer": "X", "explanation": "가장 강한 근육은 엄지발가락을 움직이는 근육입니다."},
        {"question": "사람의 심장은 주먹 크기만 하다. (O/X)", "answer": "O", "explanation": "성인의 심장은 대략 주먹 크기와 비슷합니다."},
        {"question": "인체의 모든 혈관을 이으면 지구를 두 바퀴 반 돌 수 있다. (O/X)", "answer": "O", "explanation": "성인의 혈관 길이를 모두 합치면 약 96,000km로, 지구를 두 바퀴 반 정도 돌 수 있습니다."}
    ],
    "질병": [
        {"question": "감기는 바이러스가 아닌 박테리아에 의해 발생한다. (O/X)", "answer": "X", "explanation": "감기는 주로 바이러스에 의해 발생합니다."},
        {"question": "당뇨병은 완치가 가능하다. (O/X)", "answer": "X", "explanation": "당뇨병은 관리는 가능하지만 완치는 어렵습니다."},
        {"question": "모든 암은 유전적 요인에 의해 발생한다. (O/X)", "answer": "X", "explanation": "일부 암은 유전적 요인이 있지만, 모든 암이 그런 것은 아닙니다."},
        {"question": "고혈압은 '침묵의 살인자'라고 불린다. (O/X)", "answer": "O", "explanation": "고혈압은 증상이 없어 '침묵의 살인자'로 불립니다."},
        {"question": "알츠하이머병은 노화의 정상적인 과정이다. (O/X)", "answer": "X", "explanation": "알츠하이머병은 정상적인 노화 과정이 아닌 뇌질환입니다."}
    ],
    "생명": [
        {"question": "모든 생물은 세포로 이루어져 있다. (O/X)", "answer": "O", "explanation": "모든 생명체는 하나 이상의 세포로 구성되어 있습니다."},
        {"question": "식물은 밤에 이산화탄소를 흡수한다. (O/X)", "answer": "X", "explanation": "식물은 주로 낮에 광합성을 통해 이산화탄소를 흡수합니다."},
        {"question": "모든 박테리아는 해롭다. (O/X)", "answer": "X", "explanation": "많은 박테리아가 인체에 유익하거나 중요한 역할을 합니다."},
        {"question": "DNA는 모든 생명체에서 유전 정보를 저장한다. (O/X)", "answer": "X", "explanation": "일부 바이러스는 RNA를 유전 물질로 사용합니다."},
        {"question": "인간의 유전자 수는 다른 모든 생물보다 많다. (O/X)", "answer": "X", "explanation": "인간의 유전자 수는 일부 다른 생물보다 적습니다."}
    ]
}

# 분야 선택
print("=== O/X 건강 퀴즈 ===")
print("분야를 선택하세요:")
fields = list(quiz_data.keys())
for idx, field in enumerate(fields):
    print(f"{idx + 1}. {field}")

field_choice = int(input("번호를 입력하세요: ")) - 1

if 0 <= field_choice < len(fields):
    selected_field = fields[field_choice]
    print(f"\n[선택한 분야: {selected_field}]\n")

    questions = quiz_data[selected_field]
    random.shuffle(questions)

    score = 0

    for i, quiz in enumerate(questions, 1):
        print(f"Q{i}. {quiz['question']}")
        user_answer = input("답변 (O/X): ").strip().upper()

        if user_answer == quiz["answer"]:
            print("✅ 정답입니다!\n")
            score += 1
        else:
            print(f"❌ 틀렸습니다. 정답은 {quiz['answer']}입니다.")
            print(f"💡 해설: {quiz['explanation']}\n")

    print(f"총 점수: {score} / {len(questions)}")
else:
    print("잘못된 번호입니다. 프로그램을 종료합니다.")
