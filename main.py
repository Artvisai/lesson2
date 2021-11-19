import math


def func1():
    print('Введите 2 числа через ввод:\n')
    a = float(input())
    b = float(input())
    print('\nСложение: {}'.format(a + b))
    print('\nВычитание: {}'.format(a - b))
    print('\nУмножение: {}'.format(a * b))
    print('\nДеление: {}'.format(a / b))
    print('\nСтепень: {}'.format(a ** b))
    print('\nЦелочисленное деление: {}'.format(a // b))
    print('\nДеление по модулю: {}'.format(a % b))


def func2():
    a = input('Введи свое имя: ')
    print(f'Hi, {a}!')


def func3():
    print(input()[:-3:-1])


def func4():
    print(float(input())**2*math.pi)


func1()
func2()
func3()
func4()
