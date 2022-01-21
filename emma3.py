# Third Assignment
_30_days_months = {4: "April", 6: "June", 11: "November", 9: "September"}
_31_days_months = {1: "January", 3: "March", 5: "May", 7: "July", 8: "August", 10: "October", 12: "December"}
_28_days_month = {2: "February"}

while 1:
    month_num = input("Enter the number of a month or word 'done': ")
    if month_num.replace(" ", "").strip().lower() == "done":
        break
    else:
        try:
            month_num = int(month_num)
        except ValueError as val_err:
            print("Please enter a number\n")
        else:
            if month_num < 0 or month_num > 12 or month_num == 0:
                print("The number of a month must be in the range [1-12]\n")
            else:
                if month_num in _30_days_months:
                    print(f"{_30_days_months[month_num]} has 30 days in it\n")
                elif month_num in _31_days_months:
                    print(f"{_31_days_months[month_num]} has 31 days in\n")
                else:
                    print(f"{_28_days_month[month_num]} has 28 days in it\n")
