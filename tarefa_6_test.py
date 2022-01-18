import pytest #  Importação das Bibliotecas necessárias
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIvivo(self): #  1 - Identifica se o acesso a url está ativa/viva
        resp = get(self.url)
        assert resp.ok #Como o retorno é True não é necessário comparar

    def test_APIresponde(self): #  2 - Teste para verificar a resposta inicial da aplicação
        resp = get(self.url)
        mensagem = loads(resp.text)
        assert mensagem['Mensagem Inicial'] == "API Mentorama está online!!!!"

    def test_APImult(self): #  3 - Teste da Função de Multiplicação
        resp = post(self.url + "/operacoes" , json={"valor_1" : 2, "valor_2": 2, "operacao" : "multiplicação"})
        mensagem = loads(resp.text)
        assert mensagem == {"valor_1":2,"valor_2":2,"operacao":"multiplicação","Multiplicação":4}
    
    def test_APIsoma(self): #  4 - Teste da Função de Soma
        resp = post(self.url + "/operacoes" , json={"valor_1" : 2, "valor_2": 2, "operacao" : "soma"})
        mensagem = loads(resp.text)
        assert mensagem == {"valor_1":2,"valor_2":2,"operacao":"soma","Soma":4}
    
    def test_APIsubtr(self): #  5 - Teste da Função de Subtração
        resp = post(self.url + "/operacoes" , json={"valor_1" : 2, "valor_2": 2, "operacao" : "subtracao"})
        mensagem = loads(resp.text)
        assert mensagem == {"valor_1":2,"valor_2":2,"operacao":"subtracao","Subtração":0}

    def test_APIdiv(self): #  6 - Teste da Função de Divisão
        resp = post(self.url + "/operacoes" , json={"valor_1" : 2, "valor_2": 2, "operacao" : "divisão"})
        mensagem = loads(resp.text)
        assert mensagem == {"valor_1":2,"valor_2":2,"operacao":"divisão","Divisão":1.0}    











