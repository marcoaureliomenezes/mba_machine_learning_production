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