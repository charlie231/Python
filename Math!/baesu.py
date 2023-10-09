#자연수를 입력받고 두개의 숫자를 입력받아 두 개의 숫자의 배수를 입력받은 자연수 내에 구하는 프로그램.

def baesu():
    a = int(input("자연수의 범위 입력"))
    b = []
    x = int(input("배수1 입력"))
    y = int(input("배수2 입력"))

    for i in range(1,a+1,1):
        if i%x ==0 and i%y==0:
            b.append(i)

    print(b)
baesu()


