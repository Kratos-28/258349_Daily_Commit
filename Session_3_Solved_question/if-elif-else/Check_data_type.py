number=input()
if number.isalpha():
    print("Type is String.")
elif number=="0":
    print("Type is Zero()0.")
elif number.isnumeric():
    print("Type is Integer or real number.")
else:
    try:
        number=float(number)
        print("Type is float number.")
    except:
        try:
            number=complex(number)
            print("Type is complex number.")
        except:
            print("Invalid type.")    