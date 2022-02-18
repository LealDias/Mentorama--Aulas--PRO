from pathlib import Path
import queue
from requests import get
from bs4 import BeautifulSoup


def crawl(base_url , start_anchor): # Criando a Função Crawler

    search_anchors = queue.Queue() # Instanciando o Objeto queue que coloca as requisições em fila (FIFO)

    urls = [] # Lista para receber as URLS

    while True: 

        if not start_anchor: # Caso o Parâmetro start_anchor não for passado...

            start_anchor = "/"

        response = get(base_url) # Acessa a URL 

        soup = BeautifulSoup(response.text , 'html5lib') # Instância bs4 para as tags

        anchors = find_local_anchors(soup , start_anchor) # Chamada Função que Recolhe os Links através de uma lista


        if anchors:

            for a in anchors:

                url =  a

                if url in urls: # Caso a URL esteja na lista ele não executa e passa o comando para o laço.

                    continue

                if not Path(a).suffix: # Caso não haja sufixo
                    search_anchors.put(a)

                    urls.append(url)
                    #print(url)

        if search_anchors.empty():

            break

        start_anchor = search_anchors.get() # Remove e Retorna o Item da Fila

    return urls    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- FUNÇÃO EXTRAI LINK

def find_local_anchors(soup , start_anchor): # Função para Extrair os Links

    anchors = [] # Lista para armazenar os links

    for link in soup.find_all('a'): # Tags a

        anchor = link.attrs['href'] if 'href' in link.attrs else '' # Pegar todos os links através da href tag


        if anchor.startswith("https"):

            anchors.append(anchor)

    return anchors # Retorna lista com os links


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- FUNÇÃO PRINCIPAL


# Main Code Execute:    

def main():

    lista_inicial = []

    lista_reservatorio = []

    url =  "https://www.fluentu.com/blog/english-por-br/melhores-sites-interativos-para-aprender-ingles-para-adultos"

    start_anchor = "/"

    urls = crawl(url, start_anchor)

    print("Lista Inicial" , urls)


    lista_inicial.append(urls)

    l1 = []

    l2 = []

    l3 = []

    l4 = []

    l5 = []

    for i in lista_inicial:
        
        l1.clear()

        urls = crawl(i, start_anchor)
        l1.append(urls)

        lista_reservatorio.append(urls)

        for j in l1:

            l2.clear()

            urls = crawl(j, start_anchor)
            l2.append(urls)

            lista_reservatorio.append(urls)

            for k in l2:

                l3.clear()

                urls = crawl(k, start_anchor)
                l3.append(urls)

                lista_reservatorio.append(urls)

                for l in l3:

                    l4.clear()

                    urls = crawl(l, start_anchor)
                    l4.append(urls)

                    lista_reservatorio.append(urls)

                    for m in l4:

                        l5.clear()

                        urls = crawl(m, start_anchor)
                        l5.append(urls)

                        lista_reservatorio.append(urls)

                        for n in l5:

                            urls = crawl(j, start_anchor)
                            lista_reservatorio.append(urls)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------- FIM


if "__main__" == __name__:

    main()