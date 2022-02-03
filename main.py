# Importação das Bibliotecas

import pygame
import os
pygame.font.init() # Para escolha das fontes usadas nas letras dentro do jogo
pygame.mixer.init() # para execução dos sons do jogo

# Criando a Tela do Jogo

WIDTH, HEIGHT = 1080, 800 # Estabelecendo as dimensões da tela
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Criando a Tela através do Método display.set_mode
pygame.display.set_caption("Mentorama Starship Fight!") # Parte superior da tela

# Estabelecendo as Cores

WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT) # Definindo os limites do jogo através das coordenadas

# Sons do Jogo

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

# Fonte do Jogo

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Definindo algumas configurações

FPS = 75
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 # Dimensões das Naves - Pode ser alterada

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Carregando as Imagens das Naves dentro do Jogo

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Imagem de Fundo 

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# Criando função que vai inserir na tela as imagens dos jogos

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0)) # Colocando a imagem de fundo
    pygame.draw.rect(WIN, BLACK, BORDER) # Desenhando a linha que separa os dois jogadores

    # Inserindo/Criando/Instânciando as informações de vida dos dois Jogares

    red_health_text = HEALTH_FONT.render(  # Jogador 1/Vermelho
        "Vida Jogador 2: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render( # Jogador 2/Amarelo
        "Vida Jogador 1: " + str(yellow_health), 1, WHITE)

    # Inserindo na Tela as Informações Criadas    

    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10)) # Informações da Vida
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) # Naves nas coordenadas passadas na função
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Interação com as Balas Atiradas

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

# Função para movimentação da Nave Amarela

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # Esquerda
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # Direita
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # Cima
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # Baixo
        yellow.y += VEL

# Função para movimentação da Nave Amarela

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL

# Função para movimentação das Balas

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet): # Caso a bala colida com a nave
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet) # Faz a bala desaparecer caso ela saia dos limites

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet): # Caso a bala colida com a nave
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet) # Faz a bala desaparecer caso ela saia dos limites

# Função para Anunciar o Ganhador

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2)) # Para Centralizar o texto, temos que dividir por 2
    pygame.display.update()
    pygame.time.delay(5000) # Delay de 5 mili segundos


# Função Principal para Rodar o Jogo/////

def main():
    red = pygame.Rect(940, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # Localização Inical no Plano das Duas Naves
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = [] # Listas para armazenamento da quantidade das balas
    yellow_bullets = []

    red_health = 10  # Vida Incial dos Jogadores
    yellow_health = 10

    clock = pygame.time.Clock() # Relógio interno do jogo
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): # Caso o X seja elecionado
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN: # Evento de Atirar
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT: # Quando a nave vermelha é atingida 
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT: # Quando a nave amarela é atingida 
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Jogador 1 Ganhou!"

        if yellow_health <= 0:
            winner_text = "Jogador 2 Ganhou!"

        if winner_text != "":
            draw_winner(winner_text) # Chamando a função que lança na tela o ganhador
            break

        keys_pressed = pygame.key.get_pressed() # Instância da função key.get que lê o que é digitado no teclado

        yellow_handle_movement(keys_pressed, yellow) # Chamando as funções de movimentação das naves passando os parametros
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red) # Chamando a função que movimenta as balas

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main() #Chamando a main


if __name__ == "__main__": #Usando o dunder método para chamar a função.
    main()
