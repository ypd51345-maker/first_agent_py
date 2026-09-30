def calculator(expression):

    try:

        result = eval(expression)

        return str(result)


    except:

        return "计算失败"