from abc import ABC, abstractmethod
import datetime
import math

# Applying Single Responsibility Principle (SRP)
# Each class has a single responsibility and is not overloaded with multiple concerns.

class Vehicle(ABC):  # Applying Liskov Substitution Principle (LSP)
    """Abstract class representing a vehicle."""
    
    @abstractmethod
    def get_spot_size(self):
        pass

# Applying Open/Closed Principle (OCP)
# The Vehicle class is open for extension but closed for modification.

class Car(Vehicle):
    def get_spot_size(self):
        return 1

class Limo(Vehicle):
    def get_spot_size(self):
        return 2

class SemiTruck(Vehicle):
    def get_spot_size(self):
        return 3

class Driver:
    """Represents a driver and their associated vehicle."""
    
    def __init__(self, driver_id, vehicle: Vehicle):
        self._id = driver_id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_vehicle(self):
        return self._vehicle

    def get_id(self):
        return self._id

    def charge(self, amount):
        self._payment_due += amount

# ParkingFloor manages parking spots independently - SRP
class ParkingFloor:
    def __init__(self, spot_count):
        self._spots = [0] * spot_count
        self._vehicle_map = {}

    def park_vehicle(self, vehicle: Vehicle):
        size = vehicle.get_spot_size()
        l, r = 0, 0
        while r < len(self._spots):
            if self._spots[r] != 0:
                l = r + 1
            if r - l + 1 == size:
                for k in range(l, r + 1):
                    self._spots[k] = 1
                self._vehicle_map[vehicle] = (l, r)
                return True
            r += 1
        return False

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle in self._vehicle_map:
            start, end = self._vehicle_map[vehicle]
            for i in range(start, end + 1):
                self._spots[i] = 0
            del self._vehicle_map[vehicle]
            return True
        return False

class ParkingGarage:
    """Manages multiple parking floors."""
    
    def __init__(self, floor_count, spots_per_floor):
        self._parking_floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle: Vehicle):
        for floor in self._parking_floors:
            if floor.remove_vehicle(vehicle):
                return True
        return False

# Applying Dependency Inversion Principle (DIP)
# ParkingSystem depends on abstractions (ParkingGarage) rather than low-level details.
class ParkingSystem:
    def __init__(self, parking_garage: ParkingGarage, hourly_rate: float):
        self._parking_garage = parking_garage
        self._hourly_rate = hourly_rate
        self._time_parked = {}  # Map driverId to time of parking

    def park_vehicle(self, driver: Driver):
        current_hour = datetime.datetime.now().hour
        if self._parking_garage.park_vehicle(driver.get_vehicle()):
            self._time_parked[driver.get_id()] = current_hour
            return True
        return False
    
    def remove_vehicle(self, driver: Driver):
        if driver.get_id() not in self._time_parked:
            return False
        current_hour = datetime.datetime.now().hour
        time_parked = math.ceil(current_hour - self._time_parked[driver.get_id()])
        driver.charge(time_parked * self._hourly_rate)
        del self._time_parked[driver.get_id()]
        return self._parking_garage.remove_vehicle(driver.get_vehicle())

# Usage Example
parking_garage = ParkingGarage(3, 2)
parking_system = ParkingSystem(parking_garage, 5)

driver1 = Driver(1, Car())
driver2 = Driver(2, Limo())
driver3 = Driver(3, SemiTruck())

print(parking_system.park_vehicle(driver1))  # True
print(parking_system.park_vehicle(driver2))  # True
print(parking_system.park_vehicle(driver3))  # False

print(parking_system.remove_vehicle(driver1))  # True
print(parking_system.remove_vehicle(driver2))  # True
print(parking_system.remove_vehicle(driver3))  # False
