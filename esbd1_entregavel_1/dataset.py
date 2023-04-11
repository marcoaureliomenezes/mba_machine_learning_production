import random


class Dataset(object):


    def __init__(self, struct_type, size):
        self.struct_type = struct_type
        self.size = size
        self.items = self._generate_dataset()


    @staticmethod
    def generate_cpf():
        cpf = [random.randint(0, 9) for x in range(11)]                                                       
        # for _ in range(2):                                                          
        #     val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11                                                                  
        #     cpf.append(11 - val if val > 1 else 0)                                                                                                      
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)


    def get_dataset(self):
        return self.items


    def _generate_dataset(self):

        if self.struct_type == 'structure_1':
            return sorted([Dataset.generate_cpf() for n in range(self.size)])

        elif self.struct_type == 'structure_2':
            return {Dataset.generate_cpf(): i for i, _ in enumerate(range(self.size))}
        else:
            raise Exception('struct_type must be "structure_1" or "structure_2"')


    def _function_1(self, value):
        found = False
        for item in self.items:

            if item == value:
                found = True
                break
        return found


    def _function_2(self, value):
        start, end = 0, len(self.items) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if value > self.items[mid]:
                start = mid + 1
            elif value < self.items[mid]:
                end = mid - 1
            else:
                return mid
        return -1

    def _function_3(self, value):
        return self.items.get(value)


    def search(self, value, search_type):

        struct_1, struct_2 = self.struct_type == 'structure_1', self.struct_type == 'structure_2'
        func_1, func_2, func_3 = search_type == 'function_1', search_type == 'function_2', search_type == 'function_3'
        if struct_1 and func_1: self._function_1(value)
        elif struct_1 and func_2: self._function_2(value)
        elif struct_2 and func_3: self._function_3(value)
        elif struct_1: raise Exception('search_type of Structure1Dataset must be "function_1" or "function_2"')
        elif struct_2: raise Exception('search_type of Structure2Dataset must be "function_3"')
        else: pass

       