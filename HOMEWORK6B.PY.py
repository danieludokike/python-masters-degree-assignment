file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as f:
        file_content = f.readlines()
except FileNotFoundError as err:
    print(err)
else:
    for index in range(len(file_content)):
        print(f"{index}: {file_content[index]}")
