class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f"The house address is {self.address}, and {self.area} square meters, available {self.free_area} square meters. The furnitures: {'NO furniture' if len(self.furniture) == 0 else self.furniture }"

    def move_in(self, item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print("This furniture is so big, can not move into the house")


bed = Furniture("bed", 6)
sofa = Furniture("sofa", 10)
field = Furniture("field", 1000)

house1 = House("Kaarina", 100)
print(house1)

house1.move_in(bed)
print(house1)

house1.move_in(sofa)
print(house1)

house1.move_in(field)
print(house1)
