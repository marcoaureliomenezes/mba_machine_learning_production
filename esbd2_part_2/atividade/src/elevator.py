from typing import List
import uuid
from src.interfaces import Subject
from src.movement_states import ElevatorState, StoppedState



class Elevator(Subject):

    elevator_id: str = 0
    current_floor: int = 0
    num_floors: int = 0
    previous_state : ElevatorState = None
    current_state: ElevatorState = None
    velocity_state: int = 1
    weight_sensor: float = 0
    is_emergency: bool = False
    is_maintainance: bool = False
    floor_requests: List = []
    elevator_doors: List = []
    __list_of_observers: List = []

    def __init__(self, numero_andares: int) -> None:
        self.num_floors = numero_andares
        self.current_floor = 0
        self.current_state = StoppedState()
        self.elevator_id = str(uuid.uuid4())[:8]
        #for i in range(numero_andares):

            #self.elevator_doors.append(PortaElevador(i))

    def press_floor_number_button(self, floor: int):
        if floor == self.current_floor: return
        self.floor_requests.append(floor)

    # State methods
    def elevador_step(self):
        self.current_state.elevador_step(self)

    def emergency_button(self):
        self.current_state.emergency_button(self)


    def maintainance_button(self):
        self.current_state.maintainance_button(self)


    # Subject methods
    def attach(self, observer) -> None:
        self.__list_of_observers.append(observer)

    def detach(self, observer) -> None:
        self.__list_of_observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__list_of_observers:
            observer.update(self)