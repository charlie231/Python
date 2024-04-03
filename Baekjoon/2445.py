'''
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
'''

T = int(input())

for i in range(1,T):
    print("*"*i+" "*2*((T-i))+"*"*i)
print("*"*(T*2))

for i in range(1,T):
    print("*"*(T-i)+" "*(i*2)+"*"*(T-i))