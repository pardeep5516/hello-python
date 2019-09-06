#try except
while True:
    try:
        age = int(input("enter your age "))
    except ValueError:
        print("Please type integer ")
    except:
        print("unexpected error")
    else:
        print(f"user input = {age} ")
        break
    finally:
        print('i\'m here')

