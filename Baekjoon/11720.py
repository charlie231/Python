'''
문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
'''

T = int(input())
nums = input()
#print(sum(map(int,input()))) sum을 이용한 풀이방ㅅ기

total = 0
for i in nums:
    total += int(i)
print(total)
