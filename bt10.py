a=int(input("Nhap A: "))
array=[]
for i in range(0,a):
    x=int(input("Nhap X: "))
    array.append(x)
for i in array :
    if i==10:
        array.remove(i)
array.sort()
len(array)
print(array)

