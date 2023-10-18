#무한 가위바위보. 0을 입력하면 게임종료 후 결과출력

import random

def rsp_game():
    result = []


    print("가위바위보 게임 시작합니다")

    while True:
        player = input("가위, 바위 , 보 중에 1가지 입력. 0입력시 종료")
        com = random.choice(["가위","바위","보"])

        if player == "0":
            print("게임 종료")
            number = len(result)
            win = result.count("이김")
            lose = result.count("짐")
            draw = result.count("비김")
            print("게임 시행횟수는 {}회이고 {}승 {}패 {}무입니다".format(number,win,lose,draw))
            break

        elif player == "가위":
            print("컴퓨터는",com,"을(를) 냈습니다")
            if player == com:
                print("비김")
                result.append("비김")
            elif com == "보":
                print("이김")
                result.append("이김")
            elif com == "바위":
                print("짐")
                result.append("짐")

        elif player == "바위":
            print("컴퓨터는",com,"을(를) 냈습니다")
            if player == com:
                print("비김")
                result.append("비김")
            elif com == "가위":
                print("이김")
                result.append("이김")
            elif com == "보":
                print("짐")
                result.append("짐")

        elif player == "보":
            print("컴퓨터는",com,"을(를) 냈습니다")
            if player == com:
                print("비김")
                result.append("비김")
            elif com == "바위":
                print("이김")
                result.append("이김")
            elif com == "가위":
                print("짐")
                result.append("짐")

        else:
            print("가위, 바위 , 보 중 한가지를 입력하십시오")
            continue




rsp_game()



