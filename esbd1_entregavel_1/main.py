from dataset import Dataset
import time
import csv
import os

def search(dataset, search_type):
    # número de buscas, não mexer neste parâmetro
    search_batch = 10_000

    # gerando CPFs aleatórios para busca
    cpf_to_search = [Dataset.generate_cpf() for _ in range(search_batch)]
    
    start = time.time()
    for i in range(search_batch): # buscando
        dataset.search(cpf_to_search[i], search_type)
    
    return time.time() - start

def get_samples(grandeza):
    return [i for i in range(grandeza) for i in range(10**i, 10**(i+1), 10**i)]


def append_row_to_file(row, path):
    with open(path, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(row)


if __name__ == '__main__':

    size_samples = get_samples(6)

    print(size_samples)
    datasets_1 = [Dataset('structure_1', i) for i in size_samples]
    datasets_2 = [Dataset('structure_2', i) for i in size_samples]
    path_output = "./outputs/time_performance.csv"
    
    with open(path_output, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['size', 'struct_1', 'struct_1', 'struct_2'])

    for i in range(len(size_samples)):
        exec = [(datasets_1[i], 'function_1'), (datasets_1[i], 'function_2'), (datasets_2[i], 'function_3')]
        data_performance = [search(dataset, funct) for dataset, funct in exec]
        data = [size_samples[i]]
        _ = [data.append(i) for i in data_performance]
        append_row_to_file(data, path_output)

    
