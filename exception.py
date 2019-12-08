def inversal():
    try:
        num=input("enter a number : ")
        num=float(num)
        inverse = 1.0/num
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("divide by zero error")
    except TypeError:
        print("Type error")
    except:
        print("any other error")
    finally:
        print("function inverse completed")

inversal()
