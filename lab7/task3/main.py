from models import Vehicle, Car, Motorcycle, save_vehicles, load_vehicles


def main():
    vehicles = [
        Vehicle("Toyota", "Camry", 2020),
        Car("BMW", "X5", 2023, 4),
        Motorcycle("Yamaha", "MT-07", 2022, 689),
    ]

    for v in vehicles:
        print(v)
        print(v.info())
        print("honk:", v.honk())
        v.drive(150)
        print("after drive:", v.info())
        print("-" * 40)

    for v in vehicles:
        if isinstance(v, Car):
            print(v.open_trunk())
        elif isinstance(v, Motorcycle):
            print(v.wheelie())

    print("\n" + "=" * 40)

    print("\n Saving vehicles to data.json")
    save_vehicles(vehicles)

    print("\n Loading vehicles from data.json")
    loaded = load_vehicles()

    print("\n Loaded vehicles")
    for v in loaded:
        print(v.info())

    print("\n Vehicles with mileage > 0 (list comprehension)")
    driven = [v.info() for v in loaded if v.mileage > 0]
    for info in driven:
        print(info)
    
    print("\n Attempting to load a missing file")
    load_vehicles("missing_file.json")


if __name__ == "__main__":
    main()