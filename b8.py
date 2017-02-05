s=0.0
for i in range(10) :
	a=int(input("Nhap :"))
	if a in range(10,101) :
		print(a,'\n')
		s+=a;
print('tong la ',s)
