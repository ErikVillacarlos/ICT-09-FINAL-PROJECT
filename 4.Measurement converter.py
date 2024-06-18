
def measurement_converter():
    while True:
        conversions = {
            "1": ("mm to cm", 0.1),
            "2": ("cm to mm", 10),
            "3": ("ft to m", 0.3048),
            "4": ("m to ft", 3.28084),
            "5": ("in to cm", 2.54),
            "6": ("km to m", 1000),
            "7": ("cm to m", 0.01)  # Fixed the conversion factor for cm to m
        }

        print("Choose a conversion:")
        for key, (name, _) in conversions.items():
            print(f"{key}. {name}")

        choice = input("Enter the number of your choice: ")

        if choice in conversions:
            value = float(input("Enter the value to convert: "))
            conversion = conversions[choice]
            result = value * conversion[1]
            print(f"{value} {conversion[0].split()[0]} is {result:.2f} {conversion[0].split()[2]}")
        else:
            print("Invalid choice!")
            

        continue_typing = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_typing != "yes":
            print("Thanks for using the Measurement Converter!")
            break

measurement_converter()
