from kivy.app import App # Biblioteca Construtora da Aplicação
from kivy.uix.image import Image # Biblioteca para Trabalhar com Imagens
from kivy.uix.behaviors import ButtonBehavior # Biblioteca que Trabalha Interações com os Botões
from sympy import source # Para buscar arquivos no Computador/No Caso as Imagens
from kivy.uix.video import Video # Biblioteca para Trabalhar com Imagens
from kivy.core.audio import SoundLoader # Biblioteca para Carga e Execução de Sons


# Criação da Classe 

class Botao(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(Botao, self).__init__(**kwargs)
        self.source = 'C:/Users/Diego Leal/Desktop/MENTORAMA/MENTORAMA PRO/M10/mentorama_1.jpg' # Estado Inicial do Botão/Imagem

  
    def on_press(self):
        self.source = 'C:/Users/Diego Leal/Desktop/MENTORAMA/MENTORAMA PRO/M10/mentorama_2.png' # Estado quando Pressionado

        sound = SoundLoader.load('som_1.mp3') # Emissão de som quando o botão é pressionado
        sound.play()


    def on_release(self):
        self.source = 'C:/Users/Diego Leal/Desktop/MENTORAMA/MENTORAMA PRO/M10/mentorama_1.jpg' # Estado quando Liberado


class BotaoMentorama(App):  # Classe Construtora da Aplicação
    def build(self):
        return Botao()


BotaoMentorama().run()