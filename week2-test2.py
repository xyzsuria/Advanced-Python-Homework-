#2.将可打印的ascii码全部放入一个数组中，并以每行20个的格式打印出来 
x=''
for i in range(32,127):
    x+=chr(i)
a=len(x)//20
for i in range(a+1):
    print(x[i*20:(i+1)*20])

