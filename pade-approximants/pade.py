import numpy
import scipy.optimize as opt
from sympy import *
from sympy.abc import x
from scipy.interpolate import pade

eph = 0.00001
lim = 1000


def shaped(*args):
    if len(args) == 1:
        return [None for _ in range(args[0])]
    return [shaped(*args[:-1]) for _ in range(args[-1])]


def symize(f, abc=None):
    global x
    if abc is None:
        abc = [x]

    if type(f) is numpy.poly1d:
        x = abc[0]
        g = 0
        for i in range(f.order + 1):
            g += f[i] * x**i
        return g

    raise Exception('Not supported.')


def strize(f, abc=None):
    if abc is None:
        abc = ['x']

    if type(f) is numpy.poly1d:
        x = abc[0]
        s = ''
        for i in range(f.order, -1, -1):
            if f[i] > eph or f[i] < -eph:
                if s != '' and f[i] > eph:
                    s += '+'
                if i == 0 or (f[i] > 1 + eph or f[i] < -eph):
                    if f[i] < -eph and f[i] > -1 - eph:
                        s += '-'
                    else:
                        s += str(int(f[i]))
                if i == 1:
                    s += x
                elif i > 1:
                    s += x + '^' + str(i)
        if s == '':
            s = '0'
        return s

    raise Exception('Not supported.')


def integerize(p, q):
    for k in range(1, 1000):
        fl = True
        tp, tq = p * k, q * k
        for f in [tp, tq]:
            for i in range(f.order + 1):
                if f[i] > 0 and (f[i] < 1 - eph or f[i] - round(f[i]) > eph):
                    # print(k, i, p[i] if f[i] == tp[i] else tq[i], f[i])
                    fl = False
                    break
        if fl:
            for f in [tp, tq]:
                for i in range(f.order + 1):
                    f[i] = int(round(f[i]))
            return tp, tq
    raise Exception('(' + str(p) + ', ' + str(q) + ') integerize failed.')


class Analyzer:
    x0 = 0

    def __init__(self, f, n, m, xmin, xmax):
        global x
        self.n, self.m = n, m
        self.T, self.dT, self.taylor = (shaped(n + 1) for _ in range(3))
        self.R, self.dR, self.pade, self.ipade, self.spade = (shaped(n + 1, m + 1) for _ in range(5))
        self.f = [diff(f, x, i) for i in range(n + m + 1)]
        self.v = [float(self.f[i].subs(x, self.x0) / factorial(i)) for i in range(n + m + 1)]

        for n in range(self.n + 1):
            self.T[n] = numpy.poly1d(self.v[:n + 1])
            # self.dT[n] = self.T[n] - f
            self.taylor[n] = symize(self.T[n])

            for m in range(self.m + 1):
                try:
                    p = pade(self.v, n, m)
                except numpy.linalg.LinAlgError:
                    continue

                ip = integerize(p[0], p[1])
                self.pade[n][m] = tuple(map(symize, p))
                self.ipade[n][m] = tuple(map(symize, ip))
                self.spade[n][m] = f'$\\dfrac{{{strize(ip[0])}}}{{{strize(ip[1])}}}$'
                # self.spade[n][m] = f'({strize(ip[0])})/({strize(ip[1])})'
                self.R[n][m] = lambdify(x, self.ipade[n][m][0] / self.ipade[n][m][1], 'numpy')
                self.dR[n][m] = lambdify(x, self.ipade[n][m][0] / self.ipade[n][m][1] - f, 'numpy')
                print(f'[{n},{m}]_{f}', self.spade[n][m])

                # ymin=opt.minimize(self.dR[n][m],x0=[100],bounds=[(xmin,xmax)])
                # print(ymin)

        # print(self.f, self.v, self.pade, sep='\n')


Analyzer(exp(x), 3, 3, -lim, lim)
Analyzer(ln(x + 1), 3, 3, -1, lim)
