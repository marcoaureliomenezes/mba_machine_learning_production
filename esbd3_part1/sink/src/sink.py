import zmq


class Sink:

    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind("tcp://0.0.0.0:5556")


    def receive(self):
        count = 0
        while True:
            result = self.socket.recv_json()
            count += 1
            # pprint(result)
            print(f"COUNT: {count}")

   
if __name__ == "__main__":

    sink = Sink()
    sink.receive()