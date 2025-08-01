#-----------------------------abstraction---------------------------
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def honk(self):
        print("Beep beep!")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with a key.")

class bike(Vehicle):
    def start_engine(self):
        print("bike engine started with a kick.")


# v = Vehicle()  # Error
c = Car()
b=bike()
b.start_engine()
c.start_engine()  
c.honk()          
b.start_engine()