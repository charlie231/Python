print("택배를 받기 위한 정보를 입력하세요")

personName = input("받는 사람 :")
personAddr = input("주소 :")
weight = int(input("무게(g) : "))

print("** 받는 사람 ==>", personName)
print("** 주소 =>", personAddr)

print("** 배송비 ==>", weight*5, "원")


