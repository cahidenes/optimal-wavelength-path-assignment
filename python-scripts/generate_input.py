import random, pyperclip


def generate_problem(size, type='sparse'):
    n = size
    m = int(size*1.5)
    k = size*15
    w = 5
    if type == 'sparse':
        m = size*3
        k = size

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

    return s

def copy_problem(size, type='sparse'):
    s = generate_problem(size, type)
    pyperclip.copy(s)
    print('Copied')

def write_problem(size, filename, type='sparse'):
    s = generate_problem(size, type)
    with open(filename, 'w') as f:
        f.write(s)


