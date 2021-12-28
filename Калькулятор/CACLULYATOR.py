try:
    f_num = float(input("Введите первое число "))
    s_num = float(input("Введите второе число "))
    operation = input("Введите опервацию:'+' или '-' или '*' или '/' ")
    if operation == '+':
        print(f_num+s_num)
    elif operation == "-":
        print(f_num-s_num)
    elif operation == "*":
        print(f_num*s_num)
    elif operation == "/":
        print(f_num/s_num)
    else:
        print("Нет такой операции")
except ValueError:
    print('Проверьте корректность числа')
    exit()
except ZeroDivisionError:
    print("На ноль делить нельзя")