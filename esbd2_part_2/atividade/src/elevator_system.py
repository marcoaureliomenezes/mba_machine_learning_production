from functools import reduce
import time
from typing import List
from src.elevator import Elevator
from src.observers import ControlCenter, MultimidiaElevator, DoorElevator
from abc import ABC, abstractmethod


# Classe abstrata que define o contrato para os clientes
class GenericElevator(ABC):

    @abstractmethod
    def print_information(self) -> str:
        raise NotImplementedError()


# Classe abstrata que define o contrato para as fábricas
class ElevadorFactory(ABC):
    def factory_method(self) -> GenericElevator:
        raise NotImplementedError()


# Fábrica concreta que cria clientes físicos    
class ElevadorSystemFactory(ElevadorFactory):
    def factory_method(self, num_floors) -> GenericElevator:
        return ElevatorSystem(num_floors)


class ElevatorSystem:

    floor_doors: List[DoorElevator] = []
    multimidia_device: MultimidiaElevator = None
    central: ControlCenter = None
    elevator = None

    def __init__(self, floors_num: int):
        self.elevator = Elevator(floors_num)
        self.central = ControlCenter()
        self.central_multimidia = MultimidiaElevator()
        for i in range(floors_num):
            self.floor_doors.append(DoorElevator(i))
        self.configure_elevator()

    def configure_elevator(self):
        # self.elevator.attach(self.central)
        # self.elevator.attach(self.central_multimidia)
        for door in self.floor_doors:
            self.elevator.attach(door)

    def run(self, requested_floor: List[int]):

        print("#"*50)
        print(f'\tANDARES SOLICITADOS: {reduce(lambda a, b: f"{a}, {b}", requested_floor)}')
        print("#"*50, "\n")
        _ = [self.elevator.press_floor_number_button(floor) for floor in requested_floor]

        cond_1, cond_2 = True, True
        while cond_1 and cond_2:
            current_state = self.elevator.current_state.__class__.__name__ == "StoppedState"
            previous_state = self.elevator.previous_state.__class__.__name__ == "StoppedState"
            cond_1 = not (current_state and previous_state)
            cond_2 = len(self.elevator.floor_requests) > 0
            time.sleep(0.5)
            self.elevator.elevador_step()
    