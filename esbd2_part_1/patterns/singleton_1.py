def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MinhaClasse:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


if __name__ == "__main__":
    obj1 = MinhaClasse(1, 2)
    obj2 = MinhaClasse(3, 4)
    print(obj1.arg1, obj1.arg2)
    print(obj2.arg1, obj2.arg2)
    print(obj1 is obj2)