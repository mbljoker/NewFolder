import math
a=int(input("Nhap N : "))
if a<2 :
    print('ko la so nguyen to')
elif a>2 and a%2==0 :
    print ('ko la so nguyen to ')
elif  math.sqrt(a)< 3:
    print ('la so nguyen to')
else :
    print (range(3,int(math.sqrt(a))+2+2,2))
    for i in range(3,int(math.sqrt(a))+2,2):
        print(a,' ',i,' ',a%i,'\n')
        if a%i==0 :
            break
    print(i,' ',math.sqrt(a))
    if i > math.sqrt(a):
        print('La so nguyen to')
    else :
        print ('ko la so nguyen to ')
        
