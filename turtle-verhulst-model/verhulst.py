import turtle
import math
import numpy as np

# ENABLE_ANIMATION = True
ENABLE_ANIMATION = False



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
        t.fd(h[i] if i == 0 else h[i] - h[i - 1])
        t.pd()
        t.fd(1)
        t.pu()
        t.bk(1)
        t.rt(90)
        t.fd(1)
        t.lt(90)
        if ENABLE_ANIMATION and i % 15 == 0:
            turtle.update()

    t.bk(h[-1])
    t.lt(90)
    t.fd(len(h))
    t.rt(90)
    t.seth(heading)

    if ENABLE_ANIMATION:
        turtle.update()
        turtle.tracer(True)



def draw_function(t, f, x_max, width, height):
    x = [(i * x_max / width) for i in range(width)]
    y = [f(x[i]) for i in range(width)]
    h = [(y[i] * height / max(y)) for i in range(width)]

    draw_curve(t, h)



def draw_arrow(t, length, degree):
    t.rt(degree)
    t.bk(length)
    t.fd(length)
    t.lt(degree * 2)
    t.bk(length)
    t.fd(length)
    t.rt(degree)



def demo(id):
    if id == 0:
        a = [174, 179, 183, 189, 207, 234, 220.5, 256, 270, 285]
        f = verhulst(a, 0)
    else:
        a = [0.025, 0.023, 0.029, 0.044, 0.084, 0.164, 0.332, 0.521, 0.97, 1.6, 2.45, 3.11, 3.57, 3.76, 3.96, 4, 4.46, 4.4, 4.49, 4.76, 5.01]
        f = verhulst(a, 1)

    t = turtle.Turtle()
    w = turtle.Screen()

    t.reset()
    turtle.tracer(ENABLE_ANIMATION)

    width = turtle.window_width() * 9 // 10
    height = turtle.window_height() * 9 // 10
    origin_x = -width // 2
    origin_y = -height // 2
    f_width = width * 9 // 10
    f_height = height * 9 // 10

    t.speed(0)
    t.ht()
    t.pu()
    t.goto(origin_x, origin_y)
    
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

    t.color("blue")
    draw_function(t, f, len(a) * 2, f_width, f_height)
    t.color("black")

    turtle.update()
    w.exitonclick()



if __name__ == "__main__":
    # demo(0)
    demo(1)