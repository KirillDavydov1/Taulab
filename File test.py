import matplotlib.pyplot as mplplt
import control.matlab as mlab
import numpy
import math
import colorama as color

def choice():
    inertialessUnitName = 'Безынерционное звено'
    aperiodUnitName = 'Апериодическое звено'
    integralUnitName = 'Интегральное звено'
    idealdiffUnitName = 'Идеальное дифференцирующее звено'
    realdiffUnitName = 'Реальное дифференцирующее звено'
    

    needNewChoice = True

    while needNewChoice:
        print(color.Style.RESET_ALL)
        userInput = input('Введите номер команды: \n'
                          '1 - ' + inertialessUnitName + ';\n'
                          '2 - ' + aperiodUnitName + '.\n')
        if userInput.isdigit():
            needNewChoice = False
            userInput = int(userInput)
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            elif userInput == 3:
                name = 'Интегральное звено'
            elif userInput == 4:
                name = 'Идеальное дифференцирующее звено'
            elif userInput == 5:
                name = 'Реальное дифференцирующее звено'    
            else:
                print(color.Fore.RED + '\nНедоступное значение')
                needNewChoice = True
        else:
            print(color.Fore.RED + '\nПожалуйста, введите корректное числовое значение.\n')
            needNewChoice = True
    return name

def getUnit(name):
    needNewChoice = True
    while needNewChoice:
        needNewChoice = False
        k = input('Пожалуйста, введите коэффициент "k": ')
        T = input('Пожалуйста, введите коэффициент "T": ')

        if k.isdigit() and T.isdigit():
            k = int(k)
            T = int(T)
            if name == 'Безынерционное звено':
                unit = mlab.tf([k], [1])
            elif name == 'Апериодическое звено':
                unit = mlab.tf([k], [T, 1])
        else:
            print(color.Fore.RED + '\nПожалуйста, введите числовое значение.\n')
            needNewChoice = True
    return unit

def graph(num, title, y, x):
    mplplt.subplot(2, 1, num)
    mplplt.grid(True)
    if title == 'Переходная характеристика':
        mplplt.plot(x, y, 'purple')
    elif title == 'Импульсная характеристика':
        mplplt.plot(x, y, 'green')
    mplplt.title(title)
    mplplt.ylabel('Амплитуда')
    mplplt.xlabel('Время (c)')

unitName = choice()
unit = getUnit(unitName)

timeLine = []
for i in range(0, 10000):
    timeLine.append(i/1000)
[y, x] = mlab.step(unit, timeLine)
graph(1, 'Переходная характеристика', y, x)
[y, x] = mlab.impulse(unit, timeLine)
graph(2, 'Импульсная характеристика', y, x)
mplplt.show()
