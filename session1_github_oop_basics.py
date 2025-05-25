# Session 1 

# In this session, I started exploring object-oriented programming in Python.
# My goal was to understand class creation, how inheritance works, and how we encapsulate data using getters/setters.

# --- 1. Defining a Base Class ---
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model} engine started.")

    def stop_engine(self):
        print(f"{self.make} {self.model} engine stopped.")

# --- 2. Subclasses that Inherit Vehicle ---
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def open_doors(self):
        print(f"Opening {self.num_doors} doors on the {self.make} {self.model}.")

class Motorcycle(Vehicle):
    def __init__(self, make, model, cc):
        super().__init__(make, model)
        self.cc = cc

    def rev_engine(self):
        print(f"{self.make} {self.model} revving at {self.cc}cc!")

# --- 3. Example of Encapsulation ---
class ColoredPoint:
    COLORS = ["red", "green", "blue"]

    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self.color = color  # setter will validate this

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value not in ColoredPoint.COLORS:
            raise ValueError(f"Invalid color. Choose from {ColoredPoint.COLORS}")
        self._color = value

# --- 4. Putting It All Together ---
if __name__ == "__main__":
    my_car = Car("Tesla", "Model 3", 4)
    my_bike = Motorcycle("Ducati", "Monster", 1200)

    my_car.start_engine()
    my_car.open_doors()
    my_car.stop_engine()

    my_bike.start_engine()
    my_bike.rev_engine()
    my_bike.stop_engine()

    pt = ColoredPoint(5, 10, "red")
    print(f"Point is at ({pt.x}, {pt.y}) with color {pt.color}")
    pt.color = "green"