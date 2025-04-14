import random

def transformation_efficiency(plasmid_size, dna_concentration, voltage, gel_concentration):
    efficiency = 0.3

    if plasmid_size < 3000:
        efficiency *= 1.2
    elif plasmid_size > 5000:
        efficiency *= 0.8

    if 10 <= dna_concentration <= 100:
        efficiency *= 1.5
    elif dna_concentration < 10 or dna_concentration > 1000:
        efficiency *= 0.5

    if 50 <= voltage <= 150:
        efficiency *= 1.2
    elif voltage > 200:
        efficiency *= 0.5

    if 0.8 <= gel_concentration <= 1.2:
        efficiency *= 1.3
    elif gel_concentration > 2.0:
        efficiency *= 0.7

    efficiency *= random.uniform(0.95, 1.05)  # 변동 폭을 줄임

    return round(min(efficiency, 0.85), 2)

try:
    plasmid_size = int(input("플라스미드 크기 (bp): "))
    dna_concentration = float(input("DNA 농도 (ng/μL): "))
    voltage = float(input("전압 (V): "))
    gel_concentration = float(input("젤 농도 (%): "))

    result = transformation_efficiency(plasmid_size, dna_concentration, voltage, gel_concentration)
    print(f"\n예상 형질전환 효율: {result:.2f}")

    if result >= 0.7:
        print("👍 형질전환 성공 가능성이 매우 높습니다!")
    elif result >= 0.4:
        print("⚠️ 형질전환이 가능하긴 하지만 개선의 여지가 있습니다.")
    else:
        print("❌ 조건이 좋지 않아 형질전환 효율이 낮을 수 있습니다. 조건을 다시 확인하세요.")

except ValueError:
    print("입력값은 숫자여야 합니다.")