s=''
for i in range(2,10):
    for j in range(2,6):
        s1=''+string(i)
        s=s+(i)+' x '+(j)+'='+(j*i)
    s=s+"\n"
    for j in range(6,10):
        s=s+i+" x "+j+"="+j*i
    s=s+"\n"
print(s)
        
