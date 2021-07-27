# import turtle
import math
import numpy as np

def verhulst(arr, mode):
    if mode == 0:
        x0 = arr
        x1 = [x0[0]]
        for i in range(1, len(x0)):
            x1.append(x1[-1] + x0[i])
    else:
        x1 = arr
        x0 = [x1[0]]
        for i in range(1, len(x1)):
            x0.append(x1[i] - x1[i - 1])
    # print(x0)
    # print(x1)
    
    z = [(x1[i + 1] + x1[i]) / 2 for i in range(0, len(x1) - 1)]
    # print(z)
    
    Y = np.array([[x0[i]] for i in range(1, len(x0))])
    # print(Y)
    
    if mode == 0:
        B = np.array([[-z[i], 1] for i in range(len(z))])
    else:
        B = np.array([[-z[i], z[i] ** 2] for i in range(len(z))])
    # print(B)

    the = np.matmul(np.matmul(np.linalg.inv(np.matmul(B.transpose(), B)), B.transpose()), Y)
    a = the[0][0]
    b = the[1][0]
    # print(a, b)

    if mode == 0:
        f1 = lambda x : x1[0] if x == 0 else ((x1[0] - b / a) / math.exp(a * x) + b / a)
        f0 = lambda x : x0[0] if x == 0 else (f1(x) - f1(x - 1))
    else:
        f1 = lambda x : x1[0] if x == 0 else a * x1[0] / (b * x1[0] + (a - b * x1[0]) * math.exp(a * x))
    
    f = f0 if mode == 0 else f1
    # print([f(i) for i in range(len(arr) * 2)])
    return f

def draw_points(X, Y):
    pass

def draw_function(f, xm):
    xl = 320
    yl = 240

    val = [f(xl * i / xl) for i in range(xl)]
    ym = max(val)

    for i in range(xl):
        draw_points([])

def demo(id):
    if id == 0:
        a = [174, 179, 183, 189, 207, 234, 220.5, 256, 270, 285]
        f = verhulst(a, 0)
        draw_function(f, len(a) * 2)
    else:
        a = [0.025, 0.023, 0.029, 0.044, 0.084, 0.164, 0.332, 0.521, 0.97, 1.6, 2.45, 3.11, 3.57, 3.76, 3.96, 4, 4.46, 4.4, 4.49, 4.76, 5.01]
        f = verhulst(a, 1)
        draw_function(f, len(a) * 2)

if __name__ == "__main__":
    # demo(0)
    # demo(1)