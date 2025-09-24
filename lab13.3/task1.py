def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_circle(radius):
    return 3.14 * radius * radius


# Dictionary-based dispatch
area_functions = {
    "rectangle": lambda: area_rectangle(
        float(input("Enter length: ")),
        float(input("Enter width: "))
    ),
    "square": lambda: area_square(
        float(input("Enter side: "))
    ),
    "circle": lambda: area_circle(
        float(input("Enter radius: "))
    )
}


def calculate_area():
    shape = input("Enter shape (rectangle/square/circle): ").lower()
    if shape in area_functions:
        result = area_functions[shape]()
        print(f"Area of {shape} = {result}")
    else:
        print("Invalid shape entered!")


# Run
if __name__ == "__main__":
    calculate_area()
