from abc import ABC, abstractmethod
import math

# TODO: Write code for Shape3D with concrete and abstract methods.
class Shape3D(ABC):
    # TODO: Write code for volume method.
    @abstractmethod
    def volume(self): pass
    # TODO: Write code for surface_area method.
    @abstractmethod
    def surface_area(self): pass
    # TODO: Write code for describe method. You can simply print out the instance\'92s class name and its parameter(s).
    def describe(self):
        print(self.__class__.__name__)

# TODO: Write code for subclass Cube.
class Cube(Shape3D):
    # TODO: Complete the initializer method.
    def __init__(self, side):
        self.__side = side
    # TODO: Write code for volume method.
    def volume(self):
        return self.__side ** 3
    # TODO: Write code for surface_area method.
    def surface_area(self):
        return ((self.__side ** 2) * 6)

# TODO: Implement subclass Sphere
class Sphere(Shape3D):
    # TODO: Complete the initializer method.
    def __init__(self, radius):
        self.__radius = radius
    # TODO: Write code for volume method.
    def volume(self):
        return ((self.__radius ** 3) * (4/3))
    # TODO: Write code for surface_area method.
    def surface_area(self):
        return ((self.__radius ** 2) * 4)

# TODO: Implement subclass Cylinder
class Cylinder(Shape3D):
    # TODO: Complete the initializer method.
    def __init__(self, radius, height):
        self.__radius = radius
        self.__height = height
    # TODO: Write code for volume method.
    def volume(self):
        return ((self.__radius ** 2) * math.pi * self.__height)
    # TODO: Write code for surface_area method.
    def surface_area(self):
        return ((math.pi * 2 * self.__radius) * self.__height) + (2 * math.pi * (self.__radius ** 2))

# TODO: Instantiate three different objects.
cube = Cube(2)
sphere = Sphere(3)
cylinder = Cylinder(2, 5)
shapes = [cube, sphere, cylinder]

for s in shapes:
    s.describe()
    print("Volume:", s.volume())
    print("Surface area:", s.surface_area())
    print("---")

