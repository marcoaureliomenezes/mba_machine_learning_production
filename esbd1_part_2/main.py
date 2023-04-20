import time
from friend_network import FriendNetwork
import math
import csv



def create_graph(num_vertex, num_edges):
    start_time = time.time()
    friend_network = FriendNetwork(num_vertex, num_edges)
    elapsed_time = time.time() - start_time
    return friend_network, elapsed_time


def get_separation_degree(friend_network, alternate=False):
    start_time = time.time()
    separation_degree = friend_network.get_separation_degree(alternate=alternate)
    elapsed_time = time.time() - start_time
    return separation_degree, elapsed_time


# MEthod that appends or write to a csv. Receive as parameter a list of lists
def write_to_csv(list_rows, file_name, append=False):
    
    if append:
        with open(file_name, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(list_rows)
    else:
        with open(file_name, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(list_rows)


if __name__ == '__main__':

    calcula_parms = lambda n: [10**(i) for i in range(2, n+1)]

    num_vertex = calcula_parms(5)

    num_edges_const = [(i, 5*i) for i in num_vertex]
    num_edges_sqrt = [(i, int(i * math.sqrt(i))) for i in num_vertex]
    num_edges_quinto = [(i, int(i * i / 5)) for i in num_vertex]
    
    filename = "output/output_teste.csv"
    header = ["num_vertices;num_connections;time_generate_graph;simple_separation_degree;time_compute_simple_separation_degree;alternate_separation_degree;time_compute_alternate_separation_degree"]

    write_to_csv([header], filename, append=False)
    
    for teste_methodology in [num_edges_const, num_edges_sqrt, num_edges_quinto]:

        for i in range(len(teste_methodology)):
            friend_network, time_spend_create = create_graph(*teste_methodology[i])
            separation_degree1, time_spend_compute_1 = get_separation_degree(friend_network)
            separation_degree2, time_spend_compute_2 = get_separation_degree(friend_network, alternate=True)
            row = [teste_methodology[i][0], teste_methodology[i][1], time_spend_create, separation_degree1, time_spend_compute_1,separation_degree2, time_spend_compute_2]
            write_to_csv([row], filename, append=True)

