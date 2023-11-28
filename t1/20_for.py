temperature_dict = {"111":36.4,"112":36.6,"113":38.5}

for temperature_tupel in temperature_dict.items():
    staff_id = temperature_tupel[0]
    temperature = temperature_tupel[1]
    if temperature >= 38:
        print(staff_id)