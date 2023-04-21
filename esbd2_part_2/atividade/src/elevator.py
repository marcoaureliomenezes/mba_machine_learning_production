from random import randint
import time
from typing import List
import uuid
from src.interfaces import Subject
from src.movement_states import ElevatorState, StoppedState



class Elevator(Subject):

    elevator_id: str
    current_floor: int
    num_floors: int
    previous_state : ElevatorState
    current_state: ElevatorState
    elevador_velocity: float
    weight_sensor: float
    is_emergency: bool = False
    is_maintainance: bool = False
    requested_floors: List = []
    called_floors: List = []
    elevator_doors: List = []
    __list_of_observers: List = []

    def __init__(self, numero_andares: int) -> None:
        self.num_floors = numero_andares
        self.current_floor = 0
        self.current_state = StoppedState()
        self.previous_state = None
        self.elevator_id = str(uuid.uuid4())[:8]
        self.weight_dict = {}
        self.weight_sensor = 0
        self.elevador_velocity = 1
        #for i in range(numero_andares):

            #self.elevator_doors.append(PortaElevador(i))

    def press_floor_number_button(self, floor: int):
        if floor == self.current_floor: return
        self.requested_floors.append(floor)
        print(floor)
        self.weight_dict[floor] = 50 + randint(0, 70)
        self.weight_sensor = sum(self.weight_dict.values())


    def press_call_button(self, floor: int):
        if floor == self.current_floor: return
        self.requested_floors.append(floor)

    # State methods
    def elevador_step(self):
        self.__set_velocity()
        time.sleep(self.elevador_velocity)
        self.current_state.elevador_step(self)

    def __set_velocity(self):
        if self.weight_sensor > 100:
            self.elevador_velocity = 1
        elif self.weight_sensor >= 50:
            self.elevador_velocity = 0.3
        else:
            self.elevador_velocity = 0.15

    def emergency_button(self):
        self.current_state.emergency_button(self)

    
    # Subject methods
    def attach(self, observer) -> None:
        self.__list_of_observers.append(observer)

    def detach(self, observer) -> None:
        self.__list_of_observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__list_of_observers:
            observer.update(self)
