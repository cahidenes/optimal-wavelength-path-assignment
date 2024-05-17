from pulp import *

def read_file(filename):
    global n, m, out, inv, D, w
    with open(filename) as file:
        n, m = file.readline().split()
        n = int(n)
        m = int(m)
        out = [[] for i in range(n)]
        inv = [[] for i in range(n)]
        for i in range(m):
            u, v = file.readline().split()
            u = int(u)
            v = int(v)
            out[u].append(2*i)
            out[v].append(2*i+1)
            inv[u].append(2*i+1)
            inv[v].append(2*i)
        m = 2*m
        D = []
        s = int(file.readline())
        for i in range(s):
            a, b = file.readline().split()
            a = int(a)
            b = int(b)
            D.append((a, b))
        w = int(file.readline())


def integer_problem():
    x = [[[LpVariable("x_{}_{}_{}".format(d, e, l), 0, 1, LpBinary) for l in range(w)] for e in range(m)] for d in range(len(D))]
    y = [[LpVariable("y_{}_{}".format(d, l), 0, 1, LpBinary) for l in range(w)] for d in range(len(D))]

    prob = LpProblem("problem", LpMaximize)

    for d in range(len(D)):
        prob += lpSum(y[d][l] for l in range(w)) <= 1

    for e in range(0, m, 2):
        for l in range(w):
            prob += lpSum(x[d][e][l] for d in range(len(D))) + lpSum(x[d][e+1][l] for d in range(len(D))) <= 1

    for d in range(len(D)):
        for l in range(w):
            prob += lpSum(x[d][e][l] for e in inv[D[d][0]]) == 0
            prob += lpSum(x[d][e][l] for e in out[D[d][0]]) == y[d][l]

            prob += lpSum(x[d][e][l] for e in out[D[d][1]]) == 0
            prob += lpSum(x[d][e][l] for e in inv[D[d][1]]) == y[d][l]

    for d in range(len(D)):
        for l in range(w):
            for nn in range(n):
                if nn == D[d][0] or nn == D[d][1]:
                    continue
                prob += lpSum(x[d][e][l] for e in out[nn]) == lpSum(x[d][e][l] for e in inv[nn])

    prob += lpSum(y[d][l] for d in range(len(D)) for l in range(w))

    prob.solve()

    return int(value(prob.objective))


def relaxation():
    x = [[[LpVariable("x_{}_{}_{}".format(d, e, l), 0, 1) for l in range(w)] for e in range(m)] for d in range(len(D))]
    y = [[LpVariable("y_{}_{}".format(d, l), 0, 1) for l in range(w)] for d in range(len(D))]

    prob = LpProblem("problem", LpMaximize)

    for d in range(len(D)):
        prob += lpSum(y[d][l] for l in range(w)) <= 1

    for e in range(0, m, 2):
        for l in range(w):
            prob += lpSum(x[d][e][l] for d in range(len(D))) + lpSum(x[d][e+1][l] for d in range(len(D))) <= 1

    for d in range(len(D)):
        for l in range(w):
            prob += lpSum(x[d][e][l] for e in inv[D[d][0]]) == 0
            prob += lpSum(x[d][e][l] for e in out[D[d][0]]) == y[d][l]

            prob += lpSum(x[d][e][l] for e in out[D[d][1]]) == 0
            prob += lpSum(x[d][e][l] for e in inv[D[d][1]]) == y[d][l]

    for d in range(len(D)):
        for l in range(w):
            for nn in range(n):
                if nn == D[d][0] or nn == D[d][1]:
                    continue
                prob += lpSum(x[d][e][l] for e in out[nn]) == lpSum(x[d][e][l] for e in inv[nn])

    prob += lpSum(y[d][l] for d in range(len(D)) for l in range(w))

    prob.solve()

    return value(prob.objective)

