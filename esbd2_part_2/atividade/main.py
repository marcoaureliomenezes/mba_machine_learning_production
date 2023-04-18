import random
from src.elevator_system import ElevadorSystemFactory, GenericElevator, ElevadorFactory


if __name__ == "__main__":

    num_floors = 10
    #sistema_elevador = ElevatorSystem(num_floors)

    elevator_system_factory: ElevadorFactory = ElevadorSystemFactory()
    elevator_system_1: GenericElevator = elevator_system_factory.factory_method(num_floors)

    counter = 0
    while True:
        requested_floor = random.sample(range(0, num_floors), random.randint(1, 3))
        elevator_system_1.run(requested_floor)
        counter += 1
        if counter == 10:
            break
    


    # elevador.maintainance_button()
    # elevador.emergency_button()