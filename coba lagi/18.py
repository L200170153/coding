import re
pw = []
a = [x for x in input().split(',')]
for i in a:
    if 6<=len(i)<=12:
        for j in i:
            if not re.search("[a-z]",j):
                continue
            elif re.search("[0-9]",j):
                continue
            elif re.search("[A-Z]",j):
                continue
            elif re.search("[$#@]",j):
                continue
        pw.append(i)
    
print(','.join(pw))
