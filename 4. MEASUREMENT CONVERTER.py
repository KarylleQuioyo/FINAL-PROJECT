def mm_to_cm(mm):
    return mm / 10

def cm_to_mm(cm):
    return cm * 10

def ft_to_m(ft):
    return ft * 0.3048

def m_to_ft(m):
    return m / 0.3048

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons * 3.78541

def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

def cm_to_inch(cm):
    return cm / 2.54

def inch_to_cm(inch):
    return inch * 2.54

def cubic_ft_to_cubic_meter(cubic_ft):
    return cubic_ft * 0.0283168

def cubic_meter_to_cubic_ft(cubic_meter):
    return cubic_meter / 0.0283168

def display_menu():
    print("Measurement Converter Menu:")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Millimeters")
    print("3. Feet to Meters")
    print("4. Meters to Feet")
    print("5. Liters to Gallons")
    print("6. Gallons to Liters")
    print("7. Pounds to Kilograms")
    print("8. Kilograms to Pounds")
    print("9. Centimeters to Inches")
    print("10. Inches to Centimeters")
    print("11. Cubic Feet to Cubic Meters")
    print("12. Cubic Meters to Cubic Feet")

def measurement_converter():
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        
        if choice == '1':
            mm = float(input("Enter length in millimeters: "))
            print("Length in centimeters:", mm_to_cm(mm))
        elif choice == '2':
            cm = float(input("Enter length in centimeters: "))
            print("Length in millimeters:", cm_to_mm(cm))
        elif choice == '3':
            ft = float(input("Enter length in feet: "))
            print("Length in meters:", ft_to_m(ft))
        elif choice == '4':
            m = float(input("Enter length in meters: "))
            print("Length in feet:", m_to_ft(m))
        elif choice == '5':
            liters = float(input("Enter volume in liters: "))
            print("Volume in gallons:", liters_to_gallons(liters))
        elif choice == '6':
            gallons = float(input("Enter volume in gallons: "))
            print("Volume in liters:", gallons_to_liters(gallons))
        elif choice == '7':
            pounds = float(input("Enter weight in pounds: "))
            print("Weight in kilograms:", pounds_to_kilograms(pounds))
        elif choice == '8':
            kilograms = float(input("Enter weight in kilograms: "))
            print("Weight in pounds:", kilograms_to_pounds(kilograms))
        elif choice == '9':
            cm = float(input("Enter length in centimeters: "))
            print("Length in inches:", cm_to_inch(cm))
        elif choice == '10':
            inch = float(input("Enter length in inches: "))
            print("Length in centimeters:", inch_to_cm(inch))
        elif choice == '11':
            cubic_ft = float(input("Enter volume in cubic feet: "))
            print("Volume in cubic meters:", cubic_ft_to_cubic_meter(cubic_ft))
        elif choice == '12':
            cubic_meter = float(input("Enter volume in cubic meters: "))
            print("Volume in cubic feet:", cubic_meter_to_cubic_ft(cubic_meter))

        else:
            print("Invalid choice. Please enter a number from 0 to 12.")

        convert_again = input("Do you want to convert again? (yes/no): ")
        if convert_again.lower() != 'yes':
            print("Exiting the program...")
            break

measurement_converter()
