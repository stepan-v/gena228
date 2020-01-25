a=input("введите первое число")
a=int (a)
b=input("введите второе число")
b=int (b)
c=input("введите знак")
answ=0
if c=="-":
    answ=a-b
    print(answ)
if c=="*":
    answ=a*b
    print(answ)
if c=="//":
    answ=a//b
    print(answ)
if c=="//":
    answ=a//0
    print("на 0 делить нельзя")
if c=="+":
    answ=a+b
    print(answ)
