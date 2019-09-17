m=ord('a')
m1=ord('A')
n=ord('z')
x=[]
for i in range(m,n+1):
    x.append((chr(i),chr(i+m1-m)))
print(x)
for i in range(len(x)):
    print('{} - {}'.format(x[i][1],x[i][0]))
