# Base class: Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        """
        Initialize a Vehicle object.
        
        :param brand: The brand of the vehicle.
        :param model: The model of the vehicle.
        :param year: The year the vehicle was made.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        """
        Display the details of the vehicle.
        """
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Derived class: Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        """
        Initialize a Car object.
        
        :param brand: The brand of the car.
        :param model: The model of the car.
        :param year: The year the car was made.
        :param doors: The number of doors the car has.
        """
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self):
        """
        Describe how the car moves.
        """
        print("Driving")

# Derived class: Plane
class Plane(Vehicle):
    def __init__(self, brand, model, year, wingspan):
        """
        Initialize a Plane object.
        
        :param brand: The brand of the plane.
        :param model: The model of the plane.
        :param year: The year the plane was made.
        :param wingspan: The wingspan of the plane.
        """
        super().__init__(brand, model, year)
        self.wingspan = wingspan

    def move(self):
        """
        Describe how the plane moves.
        """
        print("Flying")

# Derived class: Boat
class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        """     Initialize a Boat object.
                The brand of the boat.
                The model of the boat.
                The year the boat was made.
                The length of the boat.
        """
        super().__init__(brand, model, year)
        self.length = length

    def move(self):
        """
        Describe how the boat moves.
        """
        print("Sailing")

# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 4)
    plane = Plane("Boeing", "737", 2015, "35 meters")
    boat = Boat("SeaRay", "Sundancer", 2018, "30 feet")

    print("Car Details:")
    car.display_details()
    car.move()

    print("\nPlane Details:")
    plane.display_details()
    plane.move()

    print("\nBoat Details:")
    boat.display_details()
    boat.move()
