h1=3
m1=25
s1=32
h2=4
m2=27
s2=21
x=h2*3600+m2*60+s2-h1*3600-m1*60-s1
s=x%60
m=x/60%60
h=x/3600
print(h,m,s)
