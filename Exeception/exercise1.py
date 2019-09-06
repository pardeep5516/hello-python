def divide(a,b):
    try:
        return a/b 
    except ZeroDivisionError:
        print("error........")
    except TypeError as e:
        print(f"{e}error ")
    except:
        print("unknown")
print(divide(2,0))