import math
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
min=a
if min>b :
  min=b
if min>c :
  min=c
print(min)
max =a
if max<b :
  max=b
if max<c :
  max=c
print(max)


import math
a=float(input("a:"))
b=float(input("b:"))
if a==0 :
  if b==0:
    print("PT vo so nghiem")
  print("PT vo nghiem")
x=-b/a
print('X=', x)


n=int(input("Nhap n: "))
s=0.0
for i in range(1,n):
  s=s+1/i
print('S=',s)





# Tinh n!
n=int(input("Nhap n: "))
s=1.0
for i in range(1,n+1  ):
  s=s*i;
print('n!=',s)



#Tinh 1+1/2!+..+1/n!
n=int(input("Nhap n: "))
s=0
tam=1
for i in range(1,n+1  ):
  tam*=i
  s+=1/tam
print('S=',s)




#Kiem tra so hoan hao


import math
n=int(input("Nhap n: "))
s=1;
tam=1
for i in range(2,int(math.sqrt(n))+1):
  if n%i==0:
    s+=n/i+i;
if s==n :
  print("La so hoan thien ")
else :
print ("Khong la so hoan thien")




#