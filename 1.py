# реализация через остаток от деления
def isEven(value):
    return value % 2 == 0
# реализация через целочисленное деление на 2 и умножение на 2
def isEven2(value):
    return value // 2 * 2 == value