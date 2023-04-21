import random
from src.elevator_system import ElevadorSystemFactory, GenericElevator, ElevadorFactory

if __name__ == "__main__":

    num_floors = 20
    #sistema_elevador = ElevatorSystem(num_floors)

    elevator_system_factory: ElevadorFactory = ElevadorSystemFactory()
    elevator_system_1: GenericElevator = elevator_system_factory.factory_method(num_floors)

    counter = 0
    peso = round(60 + 80 * random.random(), 2)

    print(peso)
 
    requested_floors = random.sample(range(0, num_floors), random.randint(1, 3))
        
    #elevator_system_1.run(requested_floors)

    for i in range(5):
        elevator_system_1.call(random.randint(10, num_floors + 1), 0)
        elevator_system_1.run(random.sample(range(0, num_floors), random.randint(1, 3)))
        elevator_system_1.call(random.randint(1, num_floors + 1), 0)

        
