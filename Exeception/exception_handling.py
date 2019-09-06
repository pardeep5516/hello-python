#try except
while True:
    try:
        age = int(input("enter your age "))
        break
    except ValueError:
        print("enter valid age")

if age > 18:
        print("you can play")
else:
    print("you can't play")