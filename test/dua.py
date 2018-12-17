#program factorial

a=int(input('Masukkan angka :'))
c=1
for i in range(1,a+1):
    c*=i
print c

#caralain
def fact(a):
    if a == 0:
        return 1
    return a * fact(a - 1)

print fact(a)

import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)
