"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, load):
        if self.cargo + load <= self.max_cargo:
            self.cargo += load
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
