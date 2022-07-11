#sequential
day=input()
print("today is " ,day)
day1=input()
print("today is " ,day1)

day2=input()
print("today is " ,day2)

day3=input()
print("today is " ,day3)

print("days in weeks are: ",day ," ",  day1 ," ", day2 ," ", day3)

#selection
      #if -statement
age=26
id=34
if age!=id:
    print(" johny age is above 26")
if age==26:
    print("age is equal to 26")
    
    #if-else statement
if age<=id:
    print(" age is lessthan id")
else:
    print("age is greaterthan id")
if age!=30 and id !=34:
    print("age is equal")
else:
    print("age is not equal")

     #if-elif-else statement
amount=int(input())
if amount==500:
    print("amount is equal to 500")
elif amount!=500:
    print("amount is not equal to 500")
elif amount>=500:
    print("money is greaterthan equal to 500")
elif amount<=500:
      print("money is lessthan equal to 500")
else:
    print("zero money")
    #nested-if-else statement
place=input()
n=len(place)
print(n)
proper=10
if n>proper:
    if proper==n:
        print("proper and place are same length")
    else:
        print("proper and place are different length")
else:
    print("proper and length are not equal")
#iterations
    #for
x="banana"
for i in x:
    print(i)
xx=("mango","orrange","grapes","pappaya")
mystr=iter(xx)
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
for i in xx:
    print(xx)
for i in range(0,30):
    print(i)
    if i==25:
        break
    i+=1
#while
a=20
while a>10:
    print("a is:",a)
    a=a-2
i=1
while i<=10:
    print(i)
    i+=1
k=20
while k<30:
    print(k)
    if k==25:
        break
    k+=1
i=0
while i<6:
    i+=1
    if i==4:
        continue
    print(i)
i=1
while i<6:
    print("i is:",i)
    i+=1
else:
    print(" i is not smaller")

#nested loops
for a in[1,10]:
    for b in[1,10]:
        print(a,b)

for i in [10,20]:
    for j in [10,20]:
        print(i,j)
    #pass,break,continue
#pass
manju="thundersoft"
for i in manju:
    if i=='d':
        pass
        print(i)
    print(i)
sanju="qualcom" 
for j in sanju:
    if j=='c':
        pass
        print(j)
    print(j)
#break
maxi="wonderla"
for ij in maxi:
    if ij=='e':
        print(ij)
        break
    else:
        print(ij)
#continue
for i in "python":
    if i=='t':
        print(i)
        continue
    else:
        print(i)
#range
for i in range(10):
    print(i,end=",")

for i in range(0,15):
    print(i,end=",")
for i in range(0,10,2):
    print(i,end=",")





        





















