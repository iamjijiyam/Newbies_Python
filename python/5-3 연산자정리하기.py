#연산자 정리 파일
#증감 (a++,--b) - python에는 증감연산자가 없어서 구현을 다르게 해야된다....
#산술 ((),*,%,/,+,-)
#시프트 (<<,>>)
#관계 (>=,<=)
#비트 (&,^,I)
#논리 (&&,II)
#삼항 ?  true : flase
#대입 +=,/=

a = 3
b = 9

plus = a + b
minus = a - b
multiply = a * b
divide = a / b
remainder = a % b
bit = a << 3 >> 1
logic1 = a > 1 or b > 10
logic2 = a > 1 and b > 10
logic3 = a > 1 and b > 1

print("합 = ",plus," 차 = ",minus,"곱 = ",multiply," 나누기 = ",divide," 나머지",remainder)
print("비트 연산자 사용 = ",bit,"or 연산자 사용 = ",logic1,"and 연산자 사용 시 조건 둘 다 만족 필요",logic2,logic3)






