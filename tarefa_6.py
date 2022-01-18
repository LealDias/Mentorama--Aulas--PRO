from fastapi import FastAPI  # Biblioteca para integração da API
from pydantic import BaseModel #  Biblioteca para os Modelos de Dados

program = FastAPI() #  Fast API para interface com o programa Web

@program.get("/") # Decorator
async def root(): # Função para retornar a mensagem principal
    return {"Mensagem Inicial" : "API Mentorama está online!!!!"}
   
class Resposta(BaseModel): #  Criação dos Modelos de Dados
    valor_1: int
    valor_2: int
    operacao: str
    
@program.post("/operacoes") #  Função post para acesso ao programa 
async def op_math(op: Resposta): # async = asincrono
    op_dic = op.dict() #Dicionário para receber as operações matemáticas

    if op.operacao == 'soma': 
        soma_res = op.valor_1 + op.valor_2
        op_dic.update({"Soma" : soma_res})

    elif op.operacao == 'subtracao':
        sub_res = op.valor_1 - op.valor_2
        op_dic.update({"Subtração" : sub_res})

    elif op.operacao == 'multiplicação':
        mult_res = op.valor_1 * op.valor_2
        op_dic.update({"Multiplicação" : mult_res})

    elif op.operacao == 'divisão':
        div_res = op.valor_1 / op.valor_2
        op_dic.update({"Divisão" : div_res})

    return op_dic    
    
