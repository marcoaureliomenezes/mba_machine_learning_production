import time
from src.interfaces import Observer

class MultimidiaElevator(Observer):

    def play_music(self, elevador):
        print('Multimidia: Tocando música para distrair passageiros.')
        print(f'Elevador {elevador.elevator_id} está em manutenção no andar {elevador.current_floor}.')

    def play_voice(self, elevador):
        print('Multimidia: Tocando voz para avisar passageiros.')
        print(f'Elevador {elevador.elevator_id} está em manutenção no andar {elevador.current_floor}.')

    def update(self, subject):
        if subject.is_emergency:
            print('Multimidia: Elevador em emergencia')
            self.play_music(subject)
            self.play_voice(subject)
        elif subject.is_maintainance:
            print('Multimidia: Elevador em manutenção')
            self.play_music(subject)
            self.play_voice(subject)


class DoorElevator(Observer):

    previous_len_requests = 0

    def __init__(self, numero):
        self.numero = numero
        self.is_open = False

    def open_door(self):
        print(f'PORTA {self.numero} -> ABRINDO...')
        time.sleep(0.5)
        print(f'PORTA {self.numero} == ABERTA!')
        self.is_open = True

    def cloose_door(self):
        print(f'PORTA {self.numero} -> FECHANDO...')
        self.is_open = False
        time.sleep(0.5)
        print(f'PORTA {self.numero} == FECHADA!')

    def get_is_open(self):
        return self.is_open


    def update(self, subject):

        actual_state_stopped = subject.current_state.__class__.__name__ == 'StoppedState'
        right_floor = subject.current_floor == self.numero

        if right_floor and actual_state_stopped  and self.previous_len_requests > len(subject.floor_requests):
            self.open_door(); time.sleep(3); self.cloose_door()

        if right_floor and actual_state_stopped and subject.previous_state == None:
            self.cloose_door()
        self.previous_len_requests = len(subject.floor_requests)

        # if subject.is_emergency:
        #     print(f'Porta {self.numero}: Elevador em emergencia')
        #     print(f'Porta {self.numero}: Fechando porta')
        #     self.fechar()
        # elif subject.is_maintainance:
        #     print(f'Porta {self.numero}: Elevador em manutenção')
        #     print(f'Porta {self.numero}: Fechando porta')
        #     self.fechar()

        
class ControlCenter(Observer):

    def __init__(self):
        self.is_emergency = False
        self.is_maintainance = False

    def update(self, subject):
        print(subject.is_emergency)
        print(subject.is_maintainance)
        if subject.is_emergency:
            print('Central de Inteligencia: Elevador em emergencia')
            print('Acionar sistema de voz para avisar passageiros e musica para distrair')
            print('Acionar sistema de comunicação para avisar equipe de manutenção')
        elif subject.is_maintainance:
            print('Central de Inteligencia: Elevador em manutenção')
            print('Acionar sistema de portas para fechar')
