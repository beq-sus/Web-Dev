import json


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, km):
        self.mileage += km
        return f"{self.brand} {self.model} drove {km} km."

    def info(self):
        return f"{self.year} {self.brand} {self.model}, mileage: {self.mileage} km"

    def honk(self):
        return "Beep!"

    def to_dict(self):
        return {
            "type": "Vehicle",
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
        }

    def __str__(self):
        return f"Vehicle({self.brand}, {self.model}, {self.year})"


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def honk(self):
        return f"{self.brand} {self.model}: Honk honk!"

    def open_trunk(self):
        return f"{self.brand} {self.model}: trunk is open"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Car"
        data["num_doors"] = self.num_doors
        return data

    def __str__(self):
        return f"Car({self.brand}, {self.model}, {self.year}, doors={self.num_doors})"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc

    def honk(self):
        return f"{self.brand} {self.model}: Beeeep! ({self.engine_cc}cc)"

    def wheelie(self):
        return f"{self.brand} {self.model} pulls a wheelie!"

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "Motorcycle"
        data["engine_cc"] = self.engine_cc
        return data

    def __str__(self):
        return f"Motorcycle({self.brand}, {self.model}, {self.year}, cc={self.engine_cc})"



def save_vehicles(vehicles, filename="data.json"):
    try:
        data = [v.to_dict() for v in vehicles]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Saved {len(data)} vehicle to '{filename}'.")
    except TypeError as e:
        print(f"[Error] Could not serialise vehicles – invalid data type: {e}")
    except OSError as e:
        print(f"[Error] Could not write to '{filename}': {e}")
    finally:
        print("save_vehicles() finished.")


def load_vehicles(filename="data.json"):
    vehicles = []
    try:
        with open(filename, "r") as f:
            data = json.load(f)

        for entry in data:
            vehicle_type = entry.get("type")
            try:
                if vehicle_type == "Car":
                    obj = Car(
                        entry["brand"],
                        entry["model"],
                        int(entry["year"]),   # 
                        int(entry["num_doors"]),
                    )
                elif vehicle_type == "Motorcycle":
                    obj = Motorcycle(
                        entry["brand"],
                        entry["model"],
                        int(entry["year"]),
                        int(entry["engine_cc"]),
                    )
                elif vehicle_type == "Vehicle":
                    obj = Vehicle(
                        entry["brand"],
                        entry["model"],
                        int(entry["year"]),
                    )
                else:
                    print(f"[Warning] Unknown vehicle type '{vehicle_type}' – skipped.")
                    continue

                obj.mileage = int(entry.get("mileage", 0))
                vehicles.append(obj)

            except (ValueError, KeyError) as e:
                print(f"[Error] Could not recreate vehicle from entry {entry}: {e}")

    except FileNotFoundError:
        print(f"[Error] File '{filename}' not found. No vehicles loaded.")
    except json.JSONDecodeError as e:
        print(f"[Error] '{filename}' contains invalid JSON: {e}")
    finally:
        print("load_vehicles() finished.")

    return vehicles
