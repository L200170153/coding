#items=[x for x in raw_input().split('\n')]
#items.upper()
#print '\n'.join(items)

lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print sentence
