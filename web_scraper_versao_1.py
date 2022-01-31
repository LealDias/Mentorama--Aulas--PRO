from asyncio import ensure_future, gather, get_event_loop
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from time import time

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

async def fetch(session, url):  # Fetch = Busca
    async with session.get(url) as response: # Inserindo o inicio da sessão na variável response
        return await response.text() # Await dá acesso a outra corrotina/se existir e executa quando está estiver pronta


async def run():

    tasks = []

    lista_titulos = []
    lista_preco = []

    nome_pag = []

    async with ClientSession() as session:
        for livros in url_list:
            task = ensure_future(
                fetch(session, livros)
            )

            tasks.append(task) # Colocando os acessos na lista
       
        responses = await gather (*tasks) # Aguarda todas as tasks serem executadas para então prosseguir


        print("Sucesso no Acesso aos Sites...")

    for s in responses:

        tags_inst = BeautifulSoup(s , 'html5lib') # Instânciando o BeautifulSoup

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


        print(f"O livro mais Caro da Sessão {nome_pag} é: {tit_livro} com o Valor de {max(lista_preco)}")
        print("\n")

        lista_titulos.clear() #Limpeza das listas para o novo laço no loop
        lista_preco.clear()

inicio = time() # Iniciando timer 

loop = get_event_loop()
future = ensure_future(run())
loop.run_until_complete(future)

termino = time() # Finalizando Timer

print(f"O tempo de execução foi: {termino - inicio}")
