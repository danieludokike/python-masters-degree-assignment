def get_mode(num_list):
    num_occur = {}
    mode_val = {}

    for i in num_list:
        if i in num_occur.keys():
            num_occur[i] += 1
        else:
            num_occur[i] = 1

    mode = num_occur[1]
    for key in num_occur:
        if num_occur[key] > mode:
            mode = num_occur[key]
            mode_val[key] = mode

    for key in mode_val:
        print(f"{key} Occurs {mode_val[key]} time(s)")


# MAIN FUNCTION OF THE PROGRAM
def main():
    numbers = [3, 3, 2, 1, 3, 0, 6, 1, 1, 2, 0, 2, 0, 2, 3]
    get_mode(numbers)


if __name__ == "__main__":
    main()

[print(i) for i in range(20) if i % 2 == 0]