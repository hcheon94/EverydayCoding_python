#%%
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b) :
    return a*b

def div(a,b):
    return a/b

def pow(a,b):
    return a**b

def mod(a,b):
    return a%b

def calc (to_solve) :
    operations = {'+':add,
                  '-':sub,
                  '*':mul,
                  '/':div,
                  '**':pow,
                  '%':mod}
    op,first_s,second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)
    
    return operations[op](first,second) #operations가 함수니까 특정키로 호출하면 그게 함수 리턴값이니까
# %%
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b) :
    return a*b

def div(a,b):
    return a/b

def pow(a,b):
    return a**b

def mod(a,b):
    return a%b

def calc (to_solve) :
    operations = {'+':add,
                  '-':sub,
                  '*':mul,
                  '/':div,
                  '**':pow,
                  '%':mod}
    op,first_s,second_s,third_s = to_solve.split(maxsplit=3)
    first = int(first_s)
    second = int(second_s)
    third = int(third_s)
    return operations[op](third,(operations[op](first,second))) #operations가 함수니까 특정키로 호출하면 그게 함수 리턴값이니까
# %%
