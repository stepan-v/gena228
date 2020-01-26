a=int(input("введите первое число"))
b=int(input("введите второе число"))
c=int(input("введите третье число"))
s=0.5*a*b
print("выводим площадь треугольника",s)
if a==b==c:
    print ("выводим число 3")
elif a==b:
    print ("выводим число 2")
elif c==b:
    print ("выводим число 2")
elif a==c:
    print ("выводим число 2")
else :
    print ("выводим число 0")
x=a*a+b*b
x=x**0.5
print("выводим гипотенузу треугольника",x)
D=b*b-4*a*c
print("выводим D",D)
if D>0:
    x1=(-b-D**0.5)/(2*a)
    x2=(-b+D**0.5)/(2*a)
    print (x1)
    print (x2)
elif D==0:
    x=-b/2*a
    print(x)
else:
    print("выводим корней нет")
    
