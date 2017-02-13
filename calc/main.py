#이파일은 최초 테스트용 입니다.
from printer import printer
from calc import calc

print("hello, welcome to python world.")
'''
#반복문을 위한 구구단 연습
name = "jay2"
if (name == "jay") :
    print("welcome jay!!")
else :
    print("wow")

temp1 = 1
while(temp1 < 10) :
    temp2 = 1
    while(temp2 <10 ) :
        print(temp1,"+",temp2,"=",temp1*temp2)
        temp2 +=1
    temp1 += 1
'''
#클래스 생성 및 메소드 호출, 생성자 확인.
printer().do(calc().do(3,4));



print ("Good bye!")
