'''
문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
'''

T = int(input())
sum = 0

for i in range(1,T+1):
    sum += i
print(sum)