import turtle
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
    print([f(i) for i in range(len(arr) * 2)])
    return f

def draw_curve(t, y):
    h = list(map(round, y))

    turtle.tracer(False)
    heading = t.heading()

    t.pu()
    t.seth(90)
    for i in range(len(y)):
        print(h[i])
        t.fd(h[i] if i == 0 else h[i] - h[i - 1])
        t.pd()
        t.fd(1)
        t.pu()
        t.bk(1)
        t.rt(90)
        t.fd(1)
        t.lt(90)
        if i % 20 == 0:
            turtle.update()

    t.bk(h[-1])
    t.lt(90)
    t.fd(len(h))
    t.rt(90)
    t.seth(heading)

    turtle.update()
    turtle.tracer(True)

def draw_arrow(t, length, degree):
    t.rt(degree)
    t.bk(length)
    t.fd(length)
    t.lt(degree * 2)
    t.bk(length)
    t.fd(length)
    t.rt(degree)

def draw_function(t, f, x_max):
    t.speed(0)
    t.home
    t.ht()
    t.pu()
    t.bk(turtle.window_width() * 2 // 5)
    t.rt(90)
    t.fd(turtle.window_height() * 2 // 5)

    height = turtle.window_height() * 4 // 5
    width = turtle.window_width() * 4 // 5

    # 绘制坐标轴
    t.seth(0)
    t.pu()
    t.bk(8)
    t.rt(90)
    t.fd(12)
    t.write("O", False)
    t.bk(12)
    t.lt(90)
    t.fd(8)
    t.pd()
    t.fd(width)
    draw_arrow(t, 8, 24)
    t.pu()
    t.rt(90)
    t.fd(16)
    t.write("x", False)
    t.bk(16)
    t.lt(90)
    t.pd()
    t.bk(width)
    t.lt(90)
    t.fd(height)
    draw_arrow(t, 8, 24)
    t.pu()
    t.bk(8)
    t.lt(90)
    t.fd(12)
    t.write("y", False)
    t.bk(12)
    t.rt(90)
    t.fd(8)
    t.pd()
    t.bk(height)

    # 绘制函数图像
    f_height = height * 17 // 20
    f_width = width * 17 // 20
    x = [(i * x_max / f_width) for i in range(f_width)]
    y = [f(x[i]) for i in range(f_width)]
    h = [(y[i] * f_height / max(y)) for i in range(f_width)]

    draw_curve(t, h)

def demo(id):
    if id == 0:
        a = [174, 179, 183, 189, 207, 234, 220.5, 256, 270, 285]
        f = verhulst(a, 0)
    else:
        a = [0.025, 0.023, 0.029, 0.044, 0.084, 0.164, 0.332, 0.521, 0.97, 1.6, 2.45, 3.11, 3.57, 3.76, 3.96, 4, 4.46, 4.4, 4.49, 4.76, 5.01]
        f = verhulst(a, 1)
    t = turtle.Turtle()
    t.reset()
    w = turtle.Screen()
    draw_function(t, f, len(a) * 2)
    w.exitonclick()

if __name__ == "__main__":
    demo(0)
    # demo(1)