from friend_network import FriendNetwork
import math

if __name__ == '__main__':

    friend_network = FriendNetwork(10, 8)

    num_vertex = [100, 1000, 10000, 100000]
    num_edges_const = [(i, 5*i) for i in num_vertex]
    num_edges_sqrt = [(i, int(i * math.sqrt(i))) for i in num_vertex]
    num_edges_quinto = [(i, int(i * i / 5)) for i in num_vertex]
    graph = friend_network.get_graph()
    for i in graph: print(i, graph[i])


    for node in graph:
        print(f"Node: {graph[node]['this'].get_uid()[:8]}, sex {graph[node]['this'].get_s_type()}")
        print(f"\tFriends: {[f'Person: {i.get_uid()[:8]}, sex: {i.get_s_type()}' for i in graph[node]['friends']]}")
    # separation_degree = friend_network.get_separation_degree()
    # print(separation_degree)