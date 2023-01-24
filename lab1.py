
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# dt = 0.00001#
# v0 = 10#
# g = 9.81#
# alfa = 30 *np.pi/180#
# y0 = 5#
# x0 = 11#
x = []
y = []
tim = 0
H = 0
L = 0
def Debug():
    global dt, v0, g, alfa, y0, x0, x, y, tim
    dt = 0.00001#
    v0 = 10#
    g = 9.81#
    alfa = 30 *np.pi/180#
    y0 = 5#
    x0 = 11#
    x = []
    y = []
    tim = 0
def input_data():
    global v0, y0, x0, alfa, g, dt
    print('Если вы хотите оставить значение по умолчанию, введите "!0", иначе оставте строку пустой')
    start = input()
    print('\n\n')
    if start == '!0':
        Debug()
    else:
        print('Введите значение начальной скорости(V0): ', end = '')
        v0 = float(input())
        print('Введите значение y0: ', end='')
        y0 = float(input())
        print('Введите значение x0: ', end='')
        x0 = float(input())
        print('Введите значение угла альфа: ', end='')
        alfa = float(input())*np.pi/180
        print('Введите значение ускорения свободного падения g: ', end='')
        g = float(input())
        dt = 1/100000

def add_data(y0, x0, v0, alfa, dt, g, t=0 ):

    while True:

        data_y = y0 + v0*np.sin(alfa)*t - g*t*t/2
        data_x = x0 + v0*np.cos(alfa)*t


        y.append(data_y)
        x.append(data_x)
        if data_y < 0:
            break
        t += dt


def show_graph():
    plt.figure(figsize=(8, 6))
    plt.grid()
    plt.plot(x, y)
    plt.title('Модель двумерного движения материальной точки\n в однородном поле тяготения', fontsize=12)
    plt.xlabel('X', fontsize=15, color='black')
    plt.ylabel('Y', fontsize=15, color='black')
    plt.show()



if __name__ == '__main__':
    input_data()
    #Debug()
    add_data(y0, x0, v0, alfa, dt, g, tim)
    show_graph()






