import pygame  # Game Desenvolvido por: Lucas Wesendonck
import random
import time
file = open('registro.txt', 'w+')
file.write(input('Digite seu Nome: '))
file.write('\n ')
file.write(input('Digite seu e-mail: '))
file.close()

pygame.init()
largura = 800
altura = 660
icone = pygame.image.load("imagens/lixoicone.png")
pygame.display.set_caption("Reciclagem do Alemão")
pygame.display.set_icon(icone)
tela = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()

background = pygame.image.load('imagens/01.jpg')  # plano de fundo
lixolata = pygame.image.load('imagens/lixolata.png')
lixovidro = pygame.image.load('imagens/lixovidro.png')
lixoplastico = pygame.image.load('imagens/lixoplastico.png')
lixopapel = pygame.image.load('imagens/lixopapel.png')
lata = pygame.image.load('imagens/lata.png')
plastico = pygame.image.load('imagens/plastico.png')
papel = pygame.image.load('imagens/papel.png')
vidro = pygame.image.load('imagens/vidro.png')
branco = (255, 255, 255)
preto = (0, 0, 0)


def escrevendoErros(erros):
    font = pygame.font.SysFont(None, 37)
    texto = font.render("Erros: "+str(erros), True, branco)
    tela.blit(texto, (0, 37))


def escrevendoPlacar(acertos):
    font = pygame.font.SysFont(None, 37)
    texto = font.render("Acertos: "+str(acertos), True, branco)
    tela.blit(texto, (0, 0))
