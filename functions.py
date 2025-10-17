def welcome():
    print('Good Morning')

def add(a=0,b=0):
    total = a+b
    print('a:%d b:%d'%(a,b))
    print('the sum is ',total)

def add(a,b):
    a=2
    b=3
    total = a+b
    print('a:%d b:%d'%(a,b))
    print('the sum is ',total)

def addMul(*a):
    total =0
    for i in a:
        total = total + i
    print('the sum is ',total)

def lis(lst):
    lst[2]=3

def addr(a,b):
    total = a+b
    return total

reasult = addr(2,3)
print(reasult)





x=10
y=20
add(x,y)
print('x:%d y:%d'%(x,y))


l = [1,2,5,4]
lis(l)
print(l)



addMul(10,20,40,23,10,11)
add(b=10,a=20)
add(1,2)
welcome()

