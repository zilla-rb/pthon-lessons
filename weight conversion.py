weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounda? ( K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f" your weight is : {round(weight)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = 'kgs.'
    print(f" your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")

    