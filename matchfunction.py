import re
p = re.compile('ell')
print(p.match('hello world'))
print(p.match('hello world',2))
print(p.search('hello world'))

st = "Hello world is awesome"

res = re.search(r'(.*) world is (.*)', st, re.M|re.I)

if (res):
    print(res.group())
    print(res.group(1))
    print(res.group(1))
else:
    print('no')

asd = 'sadasdsatd6sa56astcygs6ta6srcs232rfc4v;[][a]d[]s[d[sc[w[2'

result = re.sub(r'\D', 'A', asd)

print(result)
