import data
from operation import summa as summ
from operation import divis as divis
from operation import substraction as subs
from operation import multi as mult

print('Вас приветсвтует калькулятор!')
numberA = data.InputValues1('Введите число А: ')
oper = data.InputValues2('+,-,*,/ :','Try again: ')
numberB = data.InputValues1('Введите число B: ')
if oper == '+':
    print(summ.summ(numberA,numberB))
elif oper == '-':
    print(subs.subs(numberA,numberB))
elif oper == '*':
    print(mult.mult(numberA,numberB))
elif oper == '/':
    print(divis.divis(numberA,numberB))
