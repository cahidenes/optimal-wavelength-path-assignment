import random, pyperclip

n = 30
m = 40
k = 600
w = 3

s = ''
s += str(n) + ' ' + str(m) + '\n'

for i in range(n-1):
    s += str(random.randint(0, i)) + ' ' + str(i+1) + '\n'

for i in range(m-n+1):
    u = random.randint(0, n-1)
    v = u
    while v == u:
        v = random.randint(0, n-1)
    s += str(u) + ' ' + str(v) + '\n'

s += str(k) + '\n'
for i in range(k):
    u = random.randint(0, n-1)
    v = u
    while v == u:
        v = random.randint(0, n-1)
    s += str(u) + ' ' + str(v) + '\n'

s += str(w)

pyperclip.copy(s)
print('Copied to clipboard!')