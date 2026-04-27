def divide(a, b):
    try:
        a/ b
    except ZeroDivisionError:
        print(" Error: Cannot Divide by Zero")
    else:
        print(a/ b)
divide(10,5)