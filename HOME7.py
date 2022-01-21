def convert_to_fah(temp_list):
    fah_temp = [float(temp.strip().replace("\n", "")) * 1.8 + 32 for temp in temp_list]

    return fah_temp


with open("temps.txt", "r") as f:
    temperatures = f.readlines()


fah_temperatures = convert_to_fah(temperatures)
total_temp = sum(fah_temperatures)
print(f"AVERAGE = {round(total_temp/len(fah_temperatures), 5)}")
print(f"MAXIMUM TEMPERATURE = {max(fah_temperatures)}")
print(f"MINIMUM TEMPERATURE = {min(fah_temperatures)}")
