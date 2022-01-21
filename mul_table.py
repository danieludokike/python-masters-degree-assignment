# PROGRAM TO FORM A MULTIPLICATION TABLE WITH A GIVEN NUMBER PROVIDED TO NINE (9)
try:
    number = int(input("Please enter a number: "))
except ValueError:
    print("Please enter a number")
else:
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")
