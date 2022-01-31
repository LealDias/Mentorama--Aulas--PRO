# Importando as Bibliotecas Necessárias

from bs4 import BeautifulSoup
import grequests # grequests para acessos asíncronos
import requests
from time import time

inicio = time() 

url_list = [
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
    "https://books.toscrape.com/catalogue/category/books/classics_6/index.html",
    "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
    "https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
    "https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
    "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
    "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
    "https://books.toscrape.com/catalogue/category/books/religion_12/index.html"

]

requisicao = (grequests.get(url) for url in url_list) # Armazena as URLS na variável requisição

resposta = grequests.imap(requisicao , grequests.Pool(10)) # Colocar as requisições na variável resposta de forma asíncrona

# Listas para Armezenamento das Requisições em Texto

lista_titulos = []
lista_preco = []

for s in resposta:

        tags_inst = BeautifulSoup(s.text , 'html5lib') # Instânciando o BeautifulSoup

        nome_pag = tags_inst.find('title').text # Busca da Tag Titulo da Página

        titulo = tags_inst.find_all('h3') # Busca da Tag onde se encontram os nomes dos livros

        preco = tags_inst.find_all('p' , attrs={"class": "price_color"}) # Busca dos Preços dos Livros

        

        for t in titulo: # Gerando uma lista com os nomes dos livros
            lista_titulos.append(t.text)

        for p in preco: # Gerando uma lista com os preços dos livros
            lista_preco.append(p.text)
            max_p = max(lista_preco) # Salvei o Valor Máximo Na Variável
            pos_max = lista_preco.index(max_p) # Local no index onde se encontra o maior valor do livro
            tit_livro = lista_titulos[pos_max] # Acessando a lista de livros na posição coincidente a de maior valor


        print(f"O livro mais Caro da Sessão: {nome_pag} é: {tit_livro} com o Valor de: {max(lista_preco)}")
        print('\n')

        lista_titulos.clear() #Limpeza das listas para o novo laço no loop
        lista_preco.clear()

final = time()   

print(f"Tempo de Execução: {final - inicio}")





