
from src.interfaces import Observer
import os
  

class MultimidiaSystem(Observer):

    def __play_music(self):
        print('Multimidia: Iniciando música para distrair passageiros.')

        url = "mpv https://www.youtube.com/watch?v=etAIpkdhU9Q"
       
        os.system(url)

    def __play_voice(self):
        print('Multimidia: Tocando voz para avisar passageiros.')

    def update(self, subject):
        if subject.is_emergency:
            print('Multimidia: Elevador em emergencia')
            self.__play_voice()
            self.__play_music()
