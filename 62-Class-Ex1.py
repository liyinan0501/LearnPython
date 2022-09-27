class Potato:
    def __init__(self):
        self.cook_time = 0
        self.cook_status = "Raw"
        self.spices = []

    def __str__(self):
        return f"This potat is been cooked {self.cook_time}, and status is {self.cook_status}, and specise included {self.spices if self.spices else ''}"

    def cook(self, time):
        self.cook_time += time

        if 0 <= self.cook_time < 3:
            self.cook_status = "Raw"
        elif 3 <= self.cook_time < 5:
            self.cook_status = "Medium"
        elif 5 <= self.cook_time < 8:
            self.cook_status = "Well"
        elif self.cook_time >= 8:
            self.cook_status = "Over Cook!"

    def add_spice(self, spice):
        self.spices.append(spice)


digua1 = Potato()
print(digua1)
digua1.cook(4)
print(digua1)
digua1.cook(4)
print(digua1)
digua1.add_spice("chili")
print(digua1)
