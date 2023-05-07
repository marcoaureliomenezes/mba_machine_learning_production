import os, time
import zmq
from math import sqrt


class Worker:

    def __init__(self):
        self.context = zmq.Context()
        self.configure_receiver()
        self.configure_sender()

    def configure_receiver(self):
        self.socket_receiver = self.context.socket(zmq.PULL)
        self.socket_receiver.connect("tcp://ventilator:5555")

    def configure_sender(self):
        self.socket_sender = self.context.socket(zmq.PUSH)
        self.socket_sender.connect("tcp://sink:5556")


    def __task_pesada(self, num: int):
        time.sleep(2)
        return {"num": num, "sqrt": sqrt(num)}


    def work(self):
        _id = str(os.getpid())
        while True:
            workload = self.socket_receiver.recv_json()
            result = self.__task_pesada(workload["num"])
            print({"worker_id": _id, "result": result})
            self.socket_sender.send_json({"worker_id": _id, "result": result})
  


if __name__ == "__main__":

    print("starting worker...")
    worker = Worker()
    worker.work()