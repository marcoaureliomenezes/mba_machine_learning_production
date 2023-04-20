from queue import Queue
import random
import uuid


class Person(object):

    def __init__(self, uid, s_type):
        self._uid = uid
        self._s_type = s_type

    def get_uid(self):
        return self._uid
    
    def get_s_type(self):
        return self._s_type


class FriendNetwork(object):

    def __init__(self, people_num, connections_num):
        self._people_num = people_num
        self._connections_num = connections_num
        self._graph = self._generate_graph()


    def _generate_graph(self):
        people = []
        for person_index in range(self._people_num):
            uid = str(uuid.uuid4())
            s_type = 'female' if person_index < (self._people_num // 2)  else 'male'
            people.append(Person(uid, s_type))
        conn_num = 0
        graph = {}
        graph_aux = {} # criando um grafo auxiliar para agilizar algumas buscas
        while conn_num < self._connections_num:
            person, friend = random.sample(people, 2)
            person_uid = person.get_uid()
            friend_uid = friend.get_uid()
            if person_uid not in graph:
                graph[person_uid] = {
                    'this': person,
                    'friends': []
                }
                # criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo
                graph_aux[person_uid] = {}
            if friend_uid not in graph:
                graph[friend_uid] = {
                    'this': friend,
                    'friends': []
                }
                # criando um índice auxiliar para os vizinhos de cada vértice inserido no grafo
                graph_aux[friend_uid] = {} 

            if person_uid == friend_uid or \
                friend_uid in graph_aux[person_uid]: # fazer essa verificação em um índice auxiliar
                continue

            graph[person_uid]['friends'].append(friend)
            graph[friend_uid]['friends'].append(person)
            # adicionar vizinho também nos índices do grafo auxiliar
            graph_aux[person_uid][friend_uid] = True
            graph_aux[friend_uid][person_uid] = True
            conn_num += 1

        people_to_remove = []
        for person_uid in graph:
            friends_types = [*map(lambda p: p.get_s_type(), graph[person_uid]['friends'])]
            person_type = graph[person_uid]['this'].get_s_type()
            if ('male' not in friends_types or 'female' not in friends_types) and person_type in friends_types:
                people_to_remove.append({'person_uid': person_uid, 'remove_from': graph[person_uid]['friends']})

        for person_props in people_to_remove:
            for friend in person_props['remove_from']:
                person_index = [*map(lambda friend: friend.get_uid(),
                    graph[friend.get_uid()]['friends'])].index(person_props['person_uid'])
                del graph[friend.get_uid()]['friends'][person_index]
            del graph[person_props['person_uid']]
        return graph
    

    def get_person_by_uid(self, uid):
        return self._graph[uid]['this']

        

    def _search(self, person_uid, friend_uid):
        graph = self._graph
        fila = Queue()
        initial_distances = { i: None if i != person_uid else 0 for i in graph.keys()}
        fila, path_list =  Queue(), []

        person = graph[person_uid]['this']
        
        fila.put(person)

        while not fila.empty():
            vertex_uid = fila.get().get_uid()
            if vertex_uid == friend_uid: break
            for neighbor in graph[vertex_uid]['friends']:  
                neighbor_id = neighbor.get_uid()
                if initial_distances[neighbor_id] is None:
                    initial_distances[neighbor_id] = initial_distances[vertex_uid] + 1
                    path_list.append((vertex_uid, neighbor_id))
                    fila.put(neighbor)
        return self.__generate_path(path_list, person_uid, friend_uid)

    def _alternate_search(self, person_uid, friend_uid):
        graph = self._graph
        fila = Queue()
        initial_distances = { i: None if i != person_uid else 0 for i in graph.keys()}
        fila, path_list =  Queue(), []

        fila.put(graph[person_uid]['this'])
        vertex_sex = graph[person_uid]['this'].get_s_type()
        while not fila.empty():
            vertex_uid = fila.get().get_uid()
            if vertex_uid == friend_uid: break
            for neighbor in graph[vertex_uid]['friends']:  
                neighbor_id = neighbor.get_uid()
                neighbor_sex = neighbor.get_s_type()
                if vertex_sex == neighbor_sex: continue
                #print(vertex_sex, neighbor_sex)
                if initial_distances[neighbor_id] is None:
                    initial_distances[neighbor_id] = initial_distances[vertex_uid] + 1
                    path_list.append((vertex_uid, neighbor_id))
                    fila.put(neighbor)
        return self.__generate_path(path_list, person_uid, friend_uid) if initial_distances[friend_uid] != None else None
         

    
    # Método privado para gerar o caminho a partir da lista de arestas. Usa recursão para gerar o caminho de forma reversa
    def __generate_path(self, path_list, source, target):
        if target == source: return [source]
        last_index = [i for i in path_list if i[1] == target]
        if last_index == []: return None
        return self.__generate_path(path_list, source, last_index[0][0]) + [target]

    

    def get_separation_degree(self, alternate=False):
        total_paths_len = 0
        counter = 0
        while counter < 100:
            person_uid, friend_uid = random.sample([*self._graph.keys()], 2)
            if alternate == False:
                path = self._search(person_uid, friend_uid)
            else:
                path = self._alternate_search(person_uid, friend_uid)
            if path == None: continue
            counter += 1
            total_paths_len += len(path) - 1
        return total_paths_len / 100

    def get_graph(self):
        return self._graph