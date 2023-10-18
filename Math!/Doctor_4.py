#질병 입력받기

def doctor():
    A = {"K20":"식도염", "K21":"위-식도역류병","K22":"식도의 기타 질환","K23*":"달리 분류된 질환에서의 식도의 장애",
         "K25":"위궤양","K26":"십이지장궤양","K27":"상세불명 부위의 소화성 궤양","K28":"위공장궤양",
         "K29": "위염 및 십이지장염","K30":"기능성 소화불량","K31":"위 및 십이지장의 기타 질환"}

    B = {}
    for i in range(5):
        name = input("환자명 입력")
        B[name] = input("질병코드 입력. 단, 동일 질병 2인 이상 입력")


    P_NAME = input("환자 이름을 입력하세요")  #환자 이름 입력받기

    for key,value in B.items():
        if key == P_NAME:
            print("환자이름은 {}, 질병코드는 {}, 질병명은 {} 입니다".format(P_NAME, value, A[value]))


    D_NUM2 = input("질병 코드를 입력하세요")  # 질병코드 입력받기
    for key,value in B.items():
        if value == D_NUM2:
            print("환자이름은 {}, 질병코드는 {}, 질병명은 {} 입니다".format(key, D_NUM2, A[value]))

doctor()