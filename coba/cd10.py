def sama(a,b):
    if a[0]==b[0] or a[-1]==b[-1]:
        print('True')
    else:
        print('False')
a = [x for x in input().split(',')]
b = [x for x in input().split(',')]
sama(a,b)
