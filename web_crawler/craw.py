from bs4 import BeautifulSoup
from time import time
from collections import Counter , OrderedDict
from requests import get




def fetch(session, url):  # Fetch = Busca

    try:    

        response =  session(url) # Inserindo o inicio da sessão na variável response
      
        return  response.text # Retorna o texto em HTML

    except Exception: # Caso haja algum erro de conexão retorne vazio

        return ""


def find_local_anchors(soup , start_anchor = "https://"): # Função para Extrair os Links

    anchors = [] # Lista para armazenar os links

    for link in soup.find_all('a'): # Tags a

        anchor = link.attrs['href'] if 'href' in link.attrs else '' # Pegar todos os links através da href tag

        if anchor.startswith(start_anchor): # Caso o link comece com http. Processo de limpeza das tags

                anchors.append(anchor) # colocando os links na lista

    return anchors # Retorna lista com os links        



def get_raw_html(url_origem): # Função para processar as requests acessando os links. O retorno é uma lista com as páginas rankeadas

    tasks = [] # Lista com URLS/LINKS

    General = []
        
    session = get
    task = fetch(session, url_origem) # Função para buscar das urls (fetch)
            
    tasks.append(task)
            
    responses = tasks # Armazena Textos Inteiros Tipo HTML / 1 itens

        #--------------------------------------------------------------------------------------------------------------------------------------#
    for s in responses:

        soup = BeautifulSoup(s , 'html5lib') # Instânciando o BeautifulSoup

        url_inicial = find_local_anchors(soup , "https://") # Extraindo Links Tratados

        General.append(url_inicial) # Inserindo as URLs na Lista Geral

        tasks_1 = []

            
        session = get # Conecta com o Site
        for i in url_inicial:
            task = fetch(session, i)
                        
            tasks_1.append(task)

        responses_1 = tasks_1 # Armazena Textos Inteiros Tipo HTML / Vários itens

                #--------------------------------------------------------------------------------------------------------------------------------------#
        print("Estagio 1....")
        for j in responses_1:

            soup = BeautifulSoup(j , 'html5lib') # Instânciando o BeautifulSoup

            url_1 = find_local_anchors(soup , "https://") # Lista com os Links

            General.append(url_1)

            tasks_2 = []
                            
                      
            session = get # Conecta com o Site
            print("Estagio 2....")
            for l in url_1:
                task = fetch(session, l)
                               
                tasks_2.append(task)
                    
            responses_2 =  tasks_2 # Armazena Textos Inteiros Tipo HTML / Vários itens

                #--------------------------------------------------------------------------------------------------------------------------------------#
            print("Estagio 3....")
            for m in responses_2:

                soup = BeautifulSoup(m , 'html5lib') # Instânciando o BeautifulSoup

                url_2 = find_local_anchors(soup , "https://")

                General.append(url_2)    # Lista geral com as listas das urls tratadas

    print("Lista Geral" ,len(General))

    links_compilados = []
        
    print("Analisando os + Relevantes....")
    for lists in General: # Processo de compilação dos itens da lista em uma unica lista

        for link in lists:

            links_compilados.append(link)


    print("Links Compilados" , len(links_compilados))

    unique_urls = [*Counter(links_compilados)] # Contados e retornando links únicos

    count = 0
    dict_rank = {}

    print("Unique" , len(unique_urls))

    for b in unique_urls:

        for c in links_compilados:

            if b == c:

                count = count + 1

        dict_rank.update({b: count}) # Rankeando os sites pela frequência de ocorrências

        count = 0

    print("DICT RANK" , len(dict_rank))     

    sorted_rank = sorted(dict_rank.items(), key = lambda x: x[1], reverse = True) # Ordenando o dicionário do maior para o menor
        

    #print("Sorted_Rank" , sorted_rank)

    contar = 0


    print("Os dez sites mais revelantes: ")
    print("\n")

    dez_mais =[]

    for sit in range(0,10): # Pegando os 10 primeiros links da lista sem a frequência
        dez_mais.append(sorted_rank[sit][0])


    return dez_mais # Retorno dos sites mais relevantes de acordo com o critério de frequência

# Função Principal

def main(a):

    print("Searching...")
        
    s = get_raw_html(a)
                  
    return s
