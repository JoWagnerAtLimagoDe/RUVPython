a = 10

def f():
    global a
    a = 100
    

def ober():
    b = 100
    def unter():
        nonlocal b
        b = 1000
        def unterunter():
            nonlocal b
            b = 10000
        unterunter()
        
    unter()
    print(b)


ober()

def xyz(x):
    return x * x

z = lambda x: x * x

print(z(3))

myList = [10,20,30,40,50]

def s(x):
    return -x

myList = sorted(myList,key= lambda x:-x)
print(myList)





