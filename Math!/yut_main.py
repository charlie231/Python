import random
#무작위로 윷을 던지고 결과를 출력
yuts = []
count =0

def yut_start():

    print("윷놀이 게임 START")

    while True:
        YN = input("Y누르면 계속, N누르면 종료")
        if YN == 'N':
            def count_yut():
                global count
                global yuts
                print("윷놀이 {}회 했다 ㅋㅋ".format(count))
                print(yuts)

                print("도는 {}회".format(yuts.count("도")))
                print("개는 {}회".format(yuts.count("개")))
                print("걸는 {}회".format(yuts.count("걸")))
                print("윷는 {}회".format(yuts.count("윷")))
                print("모는 {}회".format(yuts.count("모")))


            count_yut()
            print("윷놀이 종료요ㅋㅋ")
            break

        elif YN =='Y':
            def doldol_yut():
                yut = []
                for i in range(1, 5):
                    yut.append(random.randrange(0, 2))
                print(yut)
                yut_sum = sum(yut)

                if int(yut_sum) == 0:
                    print("모")
                    return "모"
                elif int(yut_sum) == 1:
                    print("도")
                    return "도"
                elif int(yut_sum) == 2:
                    print("개")
                    return "개"
                elif int(yut_sum) == 3:
                    print("걸")
                    return "걸"
                elif int(yut_sum) == 4:
                    print("윷")
                    return "윷"

            yuts.append(doldol_yut())

            global count
            count+=1


        else:
            print("다시 쳐라 ㅋㅋ")
yut_start()






