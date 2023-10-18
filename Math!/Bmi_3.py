#사용자로부터 이름,성별(남자,여자), 허리둘레(cm),엉덩이둘레(cm), 신장(cm), 체중(Kg)을 입력받은 후
#리스트에 저장하고 각각 WHP,BMI값을 계산하여 사용자의 성별에 따른 비만여부와 BMI계산값을 화면에 출력

def bmi():
    while True:
        print("\n비만, BMI 검사 시작합니다")
        a = []
        b = ["이름", "성별(남,여로 입력)", "허리둘레", "엉덩이둘레", "신장", "체중"]
        for i in range(6):
            put = input("{}을 입력해 주십시오".format(b[i]))
            a.append(put)

        waist = float(a[2])
        hip = float(a[3])
        whp = waist / hip  # WHP 구하기

        height = float(a[4])
        weight = float(a[5])
        bmi = (weight / ((height / 100) ** 2))

        if a[1] == "남":
            if whp >= 0.9:
                print("WHP 비만입니다")
            else:
                print("WHP 비만이 아닙니다.")

        elif a[1] == "여":
            if whp >= 0.85:
                print("비만입니다")
            else:
                print("비만이 아닙니다.")

        if bmi <= 19.9:
            print("bmi 오류입니다. 재측정하세요")
            continue
        elif bmi >=20 and bmi <=24.9:
            print("BMI 정상입니다")
            break
        elif bmi >=25 and bmi <=29.9:
            print("BMI 과체중")
            break
        elif bmi >=30:
            print("BMI 비만입니다")
            break
bmi()
