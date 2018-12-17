def combostring(a,b):
    if len(a)>len(b):
        print(b+a+b)
    else:
        print(a+b+a)
a = input('pls input a: ')
b = input('pls input b: ')
print(len(a))
print(len(b))
combostring(a,b)
