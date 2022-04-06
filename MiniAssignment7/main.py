while True:
    input_string = input("Enter the formula : ")
    user_list = input_string.split()

    try:
        if input_string == 'quit':
            break

        float_num1 = float(user_list[0])
        float_num2 = float(user_list[2])
        operator = user_list[1]
        if len(user_list) == 3 and type(float_num1) == float and type(float_num2) == float:

            if operator == '+':
                res = float_num1 + float_num2
                print(res)


            elif operator == '-':
                diff = float_num1 - float_num2
                print(diff)

            else :
                raise Exception


        elif len(user_list) != 3:
            raise Exception

        elif input(float_num1) != float or input(float_num2) != float:
            raise ValueError

    except Exception:
        print("FormulaError")

    except ValueError:
        print("Operation cannot be performed")


