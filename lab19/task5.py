class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"      Year: {self.year}")

# Example usage:
car = Car("Toyota", "Corolla", 2020)
car.display_details()
