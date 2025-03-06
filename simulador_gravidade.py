import pygame
import sys

# Configurações do ambiente
tela_largura = 800
tela_altura = 600
gravity = 9.81  # Gravidade padrão (Terra) em m/s²
impulso = -10  # Força do pulo
velocidade_x = 5  # Velocidade de movimento horizontal
peso = 70.0  # Peso do objeto em kg (corpo humano médio)
densidade_humana = 985  # kg/m³ (aproximado)
forca_aplicada = 0  # Força aplicada ao objeto

# Gravidade nos planetas e sol (m/s²)
planetas = {
    "Mercúrio": 3.7,
    "Vênus": 8.87,
    "Terra": 9.81,
    "Marte": 3.71,
    "Júpiter": 24.79,
    "Saturno": 10.44,
    "Urano": 8.69,
    "Netuno": 11.15,
    "Lua": 1.62,
    "Sol": 274.0
}

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Simulador da Força da Gravidade")

# Definição do objeto (bola)
bola_raio = ((3 * peso) / (4 * 3.1416 * densidade_humana)) ** (1/3) * 100  # Converter para pixels
bola_x = tela_largura // 2
bola_y = 100
bola_velocidade_y = 0
bola_velocidade_x = 0

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# Criar sliders para controle
gravidade_slider = pygame.Rect(50, 50, 300, 10)
peso_slider = pygame.Rect(50, 100, 200, 10)
arrastando_gravidade = False
arrastando_peso = False

# Loop principal
enquanto_rodando = True
while enquanto_rodando:
    tela.fill(branco)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bola_velocidade_x = -velocidade_x
            if event.key == pygame.K_RIGHT:
                bola_velocidade_x = velocidade_x
            if event.key == pygame.K_SPACE and bola_y + bola_raio >= tela_altura:
                bola_velocidade_y = impulso
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                bola_velocidade_x = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if gravidade_slider.collidepoint(event.pos):
                arrastando_gravidade = True
            if peso_slider.collidepoint(event.pos):
                arrastando_peso = True
        if event.type == pygame.MOUSEBUTTONUP:
            arrastando_gravidade = False
            arrastando_peso = False
        if event.type == pygame.MOUSEMOTION:
            if arrastando_gravidade:
                gravity = max(1.0, min(274.0, (event.pos[0] - 50) / 3))
            if arrastando_peso:
                peso = max(1, min(1000, (event.pos[0] - 50) * 5))
                bola_raio = ((3 * peso) / (4 * 3.1416 * densidade_humana)) ** (1/3) * 100
    
    # Identificar planeta mais próximo da gravidade escolhida
    planeta_atual = min(planetas.keys(), key=lambda p: abs(planetas[p] - gravity))
    
    # Aplicação da gravidade
    bola_velocidade_y += gravity / 60  # Dividido por 60 para simulação mais realista
    bola_y += bola_velocidade_y
    bola_x += bola_velocidade_x
    
    # Impede que a bola atravesse o chão
    if bola_y + bola_raio > tela_altura:
        bola_y = tela_altura - bola_raio
        bola_velocidade_y *= -0.7  # Perde energia ao quicar
    
    # Impede que a bola saia das laterais
    if bola_x - bola_raio < 0:
        bola_x = bola_raio
    if bola_x + bola_raio > tela_largura:
        bola_x = tela_largura - bola_raio
    
    # Calcular força aplicada ao objeto (F = m * a)
    forca_aplicada = peso * gravity
    
    # Desenha a bola
    pygame.draw.circle(tela, vermelho, (int(bola_x), int(bola_y)), int(bola_raio))
    
    # Desenha sliders
    pygame.draw.rect(tela, preto, gravidade_slider)
    pygame.draw.rect(tela, preto, peso_slider)
    pygame.draw.circle(tela, vermelho, (int(50 + gravity * 3), 55), 8)
    pygame.draw.circle(tela, vermelho, (int(50 + (peso / 5)), 105), 8)
    
    # Exibir valores
    fonte = pygame.font.Font(None, 24)
    tela.blit(fonte.render(f"Gravidade: {gravity:.2f} m/s² ({planeta_atual})", True, preto), (370, 45))
    tela.blit(fonte.render(f"Peso: {peso:.0f} kg", True, preto), (270, 95))
    tela.blit(fonte.render(f"Força aplicada: {forca_aplicada:.2f} N", True, preto), (270, 145))
    
    pygame.display.flip()
    pygame.time.delay(20)
