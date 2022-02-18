# Mentorama--Aulas--PRO
Aulas do Curso de Python PRO - Projeto Final

## WEB CRAWLER MENTORAMA

### FUNÇÃO

    Crawler sincrono que busca através de uma url de origem, outras urls válidas dentro das páginas e repete o processo algumas vezes,
    retornando o resultado para uma view em html clone do google serach. 
    
    Nota: Por ser sincrono, o mesmo leva um certo tempo e foi construído em 3 camadas de busca, devido a problemas de compatibilidade,
    encontrados durante a execução do django e asyncio. 
    
    Como utilizar: Na página inicial que é a porta http://127.0.0.1:8000/ insira a url de origem para a busca. Em alguns segundos o site
    retorna os 10 sites mais revelantes a partir da engine de classificação de importência.
    
    Sugestão de Sites para utilizar (pois possuem menor tempo de execução relativa) : https://docs.python.org/3/library/asyncio-task.html
    https://www.fluentu.com/blog/english-por-br/melhores-sites-interativos-para-aprender-ingles-para-adultos/
                                     
    
### ENGINE DE CLASSIFICAÇÂO

    A engine de classificação (craw.py), trabalha de forma sincrona coletando os links para armazenamento. Após o armazenamento, uma comparação
    entre os sites repetidos e o total de sites é feita, sendo realizando assim uma contagem de freqência destes sites. Após a contagem um rankeamento
    é executado. Esse sistema de classificação foi escolhido pois parece ser o mais coerente e justo no ponto de vista de acessos. 
    
### PERFORMANCE

    A performance sincrona deixa a desejar no aspecto de tempo porém se torna mais segura em retorno. Melhorias no ponto de vista de tempo de execução
    podem ser feitas futuramente.
    
    Nota: O sistema vai demorar um pouco até retornar o resultado....
    
### APARÊNCIA

    A interface HTML/CSS deixa o site com um visual moderno e atrativo, tal como o google search. O uso da logo da mentorama foi aplicado de forma a 
    deixar o site com uma aparência mais profissional.
    
### TESTES

    Os testes se encontram no aquivo tests.py e todos passaram com sucesso.
    
### CONCLUSÂO

    A tarefa final foi bem desafiadora e trouxe muitos conhecimentos aprendidos até aqui. Muitas melhorias são aplicáveis no site, bem como a adição de
    interação nos botões de menu e novas páginas, além de engine de classificação dinâmicas. Não fiz o uso do banco de dados mas seria um ponto interressante
    a adição de dados dos sites no sqlite para posterior consulta. 
    
    Vou enviar junto aos arquivos, algumas fotos com o sistema funcionando.




