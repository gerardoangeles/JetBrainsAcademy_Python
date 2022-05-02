memory = 0
result = ""
msg_0 = 'Enter an equation'
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_ = [
    msg_0,
    msg_1,
    msg_2,
    msg_3,
    msg_4,
    msg_5,
    msg_6,
    msg_7,
    msg_8,
    msg_9,
    msg_10,
    msg_11,
    msg_12
]
msg_index = 0


def main_play():
    global msg_index
    while True:
        print(msg_[0])  # Enter an equation
        calc = input().split()  # read calc
        x, oper, y = calc[0], calc[1], calc[2]  # split
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            x, y = float(x), float(y)  # is number?
            if oper == '+' or oper == '-' or oper == '*' or oper == '/':  # oper?
                check(x, y, oper)  # check
                operation(x, oper, y)  # operations
                break
        except ValueError:
            print(msg_[1])  # Do you even know what numbers are? Stay focused!
        except ZeroDivisionError:
            print(msg_[3])  # Yeah... division by zero. Smart move...
        else:
            print(msg_[2])  # Yes ... an interesting math operation. You've slept through all classes, haven't you?


def check(x, y, operator):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and operator == "*":
        msg += msg_7
    if (x == 0 or y == 0) and (operator == "*" or operator == "+" or operator == "-"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def operation(x, oper, y):
    global result
    if oper == '+':
        result = x + y
    if oper == '-':
        result = x - y
    if oper == '*':
        result = x * y
    if oper == '/' and y != 0:
        result = x / y

    print(result)


def one_digit(result_main):
    global msg_index
    global memory
    if is_one_digit(result_main):  # is_one_digit
        msg_index = 10  # 10
        are_you_sure_answer = ""
        while are_you_sure_answer not in ("y", "n"):  # Are you sure? It is only one digit! (y / n)
            are_you_sure_answer = input(msg_[msg_index] + "\n")
            # equal to 11 : Don't be silly! It's just one number! Add to the memory? (y / n)
            # equal to 12 : Last chance! Do you really want to embarrass yourself? (y / n)
            if are_you_sure_answer == "y":
                if msg_index < 12:
                    msg_index = msg_index + 1 # 11, 12 ( no more increments! )
                    are_you_sure_answer = ""  # continue
                else:
                    memory = result  # store result
                    # (5) Do you want to continue calculations? (y / n):
                    step5()
            elif are_you_sure_answer == "n":
                # is "n"
                # (5) Do you want to continue calculations? (y / n):
                step5()
                #break
            else:
                # is not "n"
                #continue  # Are you sure? It is only one digit! (y / n)
                store_answer = "n"
    else:
        memory = result
        step5()


def step5():
    while True:
        # Do you want to continue calculations? (y / n):
        continue_calculations = input(msg_5 + "\n")  # read continue calculations

        if continue_calculations == 'y':
            main_play()  # Enter an equation
            calc_play(result)  # Do you want to store the result? (y / n):

        if continue_calculations == 'n':
            quit("")  # END
        else:
            continue


def calc_play(r_main):
    global msg_index
    store_answer = ""
    while True:
        global memory
        # Do you want to store the result? (y / n):
        store_answer = input(msg_4 + "\n")  # read store answer

        if store_answer == "y":
            one_digit(r_main)
        elif store_answer == 'n':
            step5()
        else:
            continue  # Do you want to store the result? (y / n):



def is_one_digit(v):
    return -10 < v < 10 and int(v) == float(v)


if __name__ == '__main__':
    try:
        main_play()  # Enter an equation
        calc_play(result)  # Do you want to store the result? (y / n):
    except Exception as e:
        print(str(e))
