# Napisz program pozwalający zapamiętać wybrane dane samochodu osobowego:
# markę
# model
# rok produkcji
# cenę
# numer rejestracyjny
# Zapewnij możliwość wprowadzenia danych z klawiatury oraz ich modyfikowania.
# Dane mają być wyświetlane na ekranie monitora

class Car:
    def __init__(self):
        self.brand = input("Insert brand: ")
        self.model = input("Insert model: ")
        self.year = input("Insert year of production: ")
        self.price = input("Insert price: ")
        self.registration_number = input("Insert registration number: ")

    def edit(self):
        self.brand = input("Insert brand: ")
        self.model = input("Insert model: ")
        self.year = input("Insert year of production: ")
        self.price = input("Insert price: ")
        self.registration_number = input("Insert registration number: ")

    def about(self):
        print(f"\n\nBrand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year of production: {self.year}")
        print(f"Price: {self.price}")
        print(f"Registration number: {self.registration_number}")



car1 = Car()
while True:
    x = int(input("\n\n1. Edit info\n2. Show data bout car\nInsert number: "))
    if x==1:
        car1.edit()
    if x==2:
        car1.about()