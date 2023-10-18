#사용자로부터 100이하의 정수5개를 입력받아 리스트로 저장 후
#컴퓨터가 무작위로 100이하의 정수 5개를 생성하여 리스트로 저장하고
#각각 사용자와 컴퓨터가 입력 받은값의 총합,평균,분산, 표준편차를 계산하여 화면에 출력

import random
import numpy as np

def num_put():
    a = []
    print("100이하의 숫자를 5개 입력하세요.")

    for i in range(5):

        b = int(input())
        if b>=0 and b<=100:
            a.append(b)
        else:
            print("0~100 범위 안의 숫자가 아닙니다.")
            print("프로그램 종료")
            break
    print("입력하신 숫자는 {}입니다.".format(a))

    c = []

    for k in range(5):
        d = random.randint(0,100)
        c.append(d)
    print("컴퓨터가 생성한 정수는 {}입니다".format(c))

    sum1 = np.sum(a)   #사용자의 정수 합
    sum2 = np.sum(c)   #컴퓨터의 정수 합
    avg1 = np.average(a)  #사용자의 평균
    avg2 = np.average(c)   #컴퓨터의 평균
    var1 = np.var(a)   #사용자의 분산
    var2 = np.var(c)    #컴퓨터의 분산
    std1 = np.std(a)   #사용자의 표준편차
    std2 = np.std(c)    #컴퓨터의 표준편차차

    print("사용자의 정수 합은 {}, 평균은 {}, 분산은 {}, 표준편차는 {}입니다.".format(sum1,avg1,var1,std1))
    print("컴퓨터의 정수 합은 {}, 평균은 {}, 분산은 {}, 표준편차는 {}입니다.".format(sum2, avg2, var2, std2))
num_put()