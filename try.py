def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print(" Error: Cannot divide by Zero")
    else:
        print(result)
divide(10, 5)