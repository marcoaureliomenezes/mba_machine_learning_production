import random
import time
import zmq

class Ventilator:

    def __init__(self):
        self.context = zmq.Context()
        self.zmq_socket = self.context.socket(zmq.PUSH)
        self.zmq_socket.bind("tcp://0.0.0.0:5555")

    def produce(self):
        count = 0
        while True:
            count += 1
            workload = {"num": random.randint(0, 999)}
            print(count, workload)
            self.zmq_socket.send_json(workload)
            time.sleep(0.5)


if __name__ == "__main__":
    
    ventilator = Ventilator()
    ventilator.produce()