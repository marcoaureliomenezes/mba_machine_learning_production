import random
from src.elevator_system import ElevadorSystemFactory, GenericElevadorSystem, GenericElevadorSystemFactory

if __name__ == "__main__":

    num_floors = 20
    elevator_system_factory: GenericElevadorSystemFactory = ElevadorSystemFactory()
    elevator_system_1: GenericElevadorSystem = elevator_system_factory.factory_method(num_floors)

 
    requested_floors = random.sample(range(0, num_floors), random.randint(1, 3))
        
    #elevator_system_1.run(requested_floors)


    for i in range(2):
        elevator_system_1.call(random.randint(10, num_floors + 1), 0)
        elevator_system_1.run(random.sample(range(0, num_floors), random.randint(1, 3)))
        elevator_system_1.call(random.randint(1, num_floors + 1), 0)

        
    elevator_system_1.elevator.emergency_button()
