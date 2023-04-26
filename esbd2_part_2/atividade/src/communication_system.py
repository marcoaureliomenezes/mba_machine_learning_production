from src.interfaces import Observer


class CommunicationSytem(Observer):

    def __init__(self):
        self.is_emergency = False
        self.is_maintainance = False

    def update(self, subject):
        if subject.is_emergency:
            print('Central de Inteligencia: Elevador em emergencia')
            self.__send_emergency_call()
        elif subject.is_maintainance:
            print('Central de Inteligencia: Elevador em manutenção')
            print('Acionar sistema de portas para fechar')

    def __send_emergency_call(self):
        print("Enviando chamado de emergencia para equipe de manutenção")