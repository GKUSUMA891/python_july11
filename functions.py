#user-defined functions
x=2;
y=3;
def add(x,y):
    add=x+y
    print("sum:",add)
    return add
add(x,y)
def average(x,y):
    average=(x+y)/2
    print("average:",average)
    return
average(x,y)
def power(x,y):
    power=(x**y)
    print("power:",power)
    return
power(x,y)

name="kusuma"; #globally create one string 
def string_name():  #fun defination 
    n=len(name); # to find length of the str
    return
print(name+ " is my friend")
print(len(name))   #print str length
print(name[2:])    # print from second index
print(name[:2])     #print the str upto second index
string_name()     #fun call

#defdault arguments function
def defaultArgs(a,b,c,d=50):
    print("a=",a,"b=",b,"c=",c)
    return
defaultArgs(10,20,30)
defaultArgs("java","python","c+")
defaultArgs(10,20,30,40)
defaultArgs(10,20,"jijju","booju")
 #required argument function
def requiredArgs(l,m,n):
    print("l=",l,"m=",m,"n=",n)
    return
requiredArgs(10,20,30)
requiredArgs("string","tuple","list")
requiredArgs(10,20,"juice")
#keyword arguments
def keywordArgs(emp,exp):
    print(emp,"exp= ",exp)
    return
keywordArgs(emp="rqr",exp=10)#keys must and should to accept it values
keywordArgs(emp="sddh",exp=32)
keywordArgs(emp="gfsad",exp=12)
#variable argument function
def variableArgs(*a):
    print("list:",a)
    return
variableArgs(10)#it accepts no of arguments
variableArgs(10,20,30,40)
variableArgs(10,300,"python")
variableArgs(100,"list","python","jijju","july")
#lambda function
#lambda function
a = 40
b = 60
x = lambda a,b: a+b
print("sum = ", x(a,b))
aa=20
bb=30
xy=lambda aa,bb: aa*bb
print("multiplication:",xy(aa,bb))

#filter
bannysha=[1,5,4,6,8,11,3,12]
even=filter(lambda x:x%2==0,bannysha)
print(list(even))

odd=filter(lambda x:x%2!=0,bannysha)
print(list(odd))

prema=[10,13,21,40,15,3,224,560,34]
even1=filter(lambda xx:xx%2==0,prema)
print("even numbers:",list(even1))
odd1=filter(lambda xx:xx%2!=0,prema)
print("odd numbers:",list(odd1))
#map
thiru=[1,3,2,4,5,6,7,8,9]
var=map(lambda x:x*2,thiru)
print(list(var))
var1=map(lambda y:y%2==0,thiru)
print(tuple(var1))
















    

