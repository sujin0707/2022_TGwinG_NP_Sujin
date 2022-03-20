# 문제 1번
def sum(a,b):
    s=a+b
    return s

# 문제 2번
def sub(a,b):
    s=a-b
    return s

# 문제 3번
def mul(a,b):
    s=a*b
    return s

# 문제 4번
def div(a,b):
    s=a/b
    return s

# 문제 5번
def distance(x1,y1,x2,y2):
    s=((x1-x2)**2+(y1-y2)**2)**(1/2)
    return s

# 문제 6번
def short():
    lylic = "life is short art is long"
    s=print(lylic[8:13])
    return s

# 문제 7번
def myReverse(string):
    string = "Hello"
    s=print(string[::-1])
    return s


# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오: ")
    hobby = input("취미를 입력하시오: ")
    university = input("재학 중인 대학을 입력하시오: ")
    birthday = input("생일을 입력하시오(예시: 981128): ")
    introduce = "제 이름은 {이름}입니다. 제 취미는 {취미}이구요. 저는 {재학_중인_대학}를 다니고 있습니다. 제 생일은 {월}월 {일}일 입니다.".format(이름=name, 취미=hobby, 재학_중인_대학=university, 월=birthday[2:4], 일=birthday[4:])
    print(introduce)
    return introduce

# 문제 9번
def calcAI():
    first = int(input("첫 번째 숫자를 입력하시오: "))
    second = int(input("두 번째 숫자를 입력하시오: "))
    sum = "두 수의 합은 {계산결과}입니다".format(계산결과=first+second)
    print(sum)
    return sum

