from tkinter.simpledialog import askinteger
import controller
import view

first = 0
second = 0
ops = ''
total = 0
list = ''
asking = ''
result = ''
stop = False
# example=''
opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}

def ask():
    global asking
    asking = controller.input_ask('Хотите ввести полностью выражение? Да/Нет: ')


def init_list():
    global list
    
    global result
    global opSelect
    # global example
    list = controller.input_list('Введите ваше выражение: ')

def result_list(list):
    global result
    result = controller.totalOperation(list)
    if stop == True:
        return True
def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True

    

