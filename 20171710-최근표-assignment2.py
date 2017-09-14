# 모듈 이용
#import math
#n = int(input('Enter a number : '))
#while True:
#    if n > -1 :
#        print(n,'! = ',math.factorial(n))
#        n = int(input('Enter a number : '))
#    else:
#        break
# 계산
while True:
    n = int(input('Enter a number : '))
    m = 1
    if n <= -1 :
        break
    for i in range(1,n+1):
        m = m * i
    print(m)
