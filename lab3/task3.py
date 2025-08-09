def calculate_power_bill(previous_reading, current_reading):
    units_consumed = current_reading - previous_reading
    match units_consumed:
        case units if units <= 100:
            rate = 5
        case units if units <= 200:
            rate = 7
        case units if units > 200:
            rate = 10
        case _:
            rate = 0
    final_bill = units_consumed * rate
    return final_bill

try:
    previous = int(input("Enter previous meter reading: "))
    current = int(input("Enter current meter reading: "))
    if current < previous:
        print("Current reading should be greater than or equal to previous reading.")
    else:
        bill = calculate_power_bill(previous, current)
        print(f"Total units consumed: {current - previous}")
        print(f"Final power bill: {bill}")
except ValueError:
    print("Invalid input. Please enter valid integer readings.")
