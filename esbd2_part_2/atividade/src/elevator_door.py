import time
from src.interfaces import Observer



from src.interfaces import Subject


class ButtonCallElevator(Subject):

    __list_of_observers = []
    is_pressed = False

    def __init__(self, floor):
        self.floor = floor

    def attach(self, observer) -> None:
        self.__list_of_observers.append(observer)

    def detach(self, observer) -> None:
        self.__list_of_observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__list_of_observers:
            observer.update(self)

    def press_button(self):
        self.is_pressed = True
        self.notify()

    

class DoorElevator(Observer):

    previous_len_requests = 0
    button: ButtonCallElevator = None

    def __init__(self, floor, button):
        self.floor: int = floor
        self.is_open: bool = False
        self.button: ButtonCallElevator = button

    def open_door(self):
        print(f'PORTA {self.floor} -> ABRINDO...')
        time.sleep(0.5)
        print(f'PORTA {self.floor} == ABERTA!')
        self.is_open = True

    def close_door(self):
        print(f'PORTA {self.floor} -> FECHANDO...')
        self.is_open = False
        time.sleep(0.5)
        print(f'PORTA {self.floor} == FECHADA!')

    def get_is_open(self):
        return self.is_open


    def update(self, subject):
        actual_state_stopped = subject.current_state.__class__.__name__ == 'StoppedState'
        right_floor = subject.current_floor == self.floor
        reach_a_target_floor = self.previous_len_requests  > len(subject.requested_floors)
    
        #print(actual_state_stopped, right_floor, reach_a_target_floor)

       
        if right_floor and actual_state_stopped  and len(subject.requested_floors) == 0:
            self.open_door(); time.sleep(3)
            return

        if right_floor and actual_state_stopped  and len(subject.requested_floors) > 0 and self.is_open:
            
            self.close_door(); time.sleep(3)
            return

        if right_floor and actual_state_stopped  and reach_a_target_floor:
            self.open_door(); time.sleep(3); self.close_door()
            return
 
        if right_floor and actual_state_stopped and subject.previous_state == None:
            self.close_door()
            return
            
        self.previous_len_requests = len(subject.requested_floors)

