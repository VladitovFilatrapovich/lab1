class Printer:
    def __init__(self, name, pages_per_minute, price_in_hryvnias, paper_format, color, print_type):
        self.name = name
        self.pages_per_minute = pages_per_minute
        self.price_in_hryvnias = price_in_hryvnias
        self.paper_format = paper_format
        self.color = color
        self.print_type = print_type

    def __str__(self):
        return f"Name - {self.name} Speed - {self.pages_per_minute} Cost - {self.price_in_hryvnias} Paper_format - {self.paper_format} Color - {self.color} Print_method - {self.print_type}"

    def __del__(self):
         print("deleted")

    @staticmethod
    def printing_time(self, pages_quantity):
        return pages_quantity / self.pages_per_minute

def main():
    printer1 = Printer("Jombo", 5, 140, "A4", "Black and White", "Laser")
    print(printer1)
    printer2 = Printer("Jimbo", 3, 105, "A3 and A5", "Coloured", "Laser")
    print(printer2)
    printer3 = Printer("Jambo", 4, 175, "A4", "Coloured", "Laser")
    print(printer3)
    print(printer1.printing_time(printer1, 10))

if __name__ == '__main__':
    main()