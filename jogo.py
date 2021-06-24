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


def jogo():
    pygame.mixer.music.load('imagens/music.mp3')
    pygame.mixer.music.play(-1)
    movimentoX = 0
    lixopapellargura = 151
    lixopapelX = 420
    lixopapelY = 410
    papelPosicaoX = largura*0.45
    papelPosicaoY = 0
    papelLargura = 116
    papelAltura = 119
    papelVelociade = 1

    lixoplasticolargura = 152
    lixoplasticoX = 250
    lixoplasticoY = 400
    plasticoPosicaoX = largura*0.45
    plasticoPosicaoY = -15
    plasticoLargura = 67
    plasticoAltura = 160
    plasticoVelocidade = 1

    lixovidrolargura = 152
    lixovidroX = 580
    lixovidroY = 400
    vidroPosicaoX = largura*0.45
    vidroPosicaoY = -15
    vidroLargura = 144
    vidroAltura = 126
    vidroVelocidade = 1

    movimentoX = 0
    lataPosicaoX = largura * 0.45
    lataPosicaoY = -10
    lataLargura = 66
    lataAltura = 103
    lataVelocidade = 1
    lixolatalargura = 157
    lixolataX = 70
    lixolataY = 400
    item = 1
    habilitaNovoItem = False
    acertos = 0
    erros = 0
    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -5
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 5
            if evento.type == pygame.KEYUP:
                movimentoX = 0
        tela.fill(branco)
        tela.blit(background, (0, 0))
        tela.blit(lixolata, (70, 400))
        tela.blit(lixoplastico, (250, 400))
        tela.blit(lixopapel, (420, 410))
        tela.blit(lixovidro, (580, 400))

        if habilitaNovoItem == True:
            item = random.randrange(1, 5)
            habilitaNovoItem = False

        if item == 1:
            tela.blit(lata, (lataPosicaoX, lataPosicaoY))
            lataPosicaoY = lataPosicaoY+lataVelocidade
            lataPosicaoX = lataPosicaoX + movimentoX

        if lixolataY < lataPosicaoY + lataAltura:
            if lixolataX < lataPosicaoX and lixolataX+lixolatalargura > lataPosicaoX or lataPosicaoX+lataAltura > lixolataX and lataPosicaoX+lataLargura < lixolataX+lixolatalargura:
                habilitaNovoItem = True
                lataPosicaoY = -10
                lataPosicaoX = random.randrange(0, largura)
                acertos = acertos + 1
                escrevendoPlacar(acertos)

        if lataPosicaoY > altura:
            erros = erros + 1
            escrevendoErros(erros)
            habilitaNovoItem = True
            lataPosicaoY = -10
            lataPosicaoX = random.randrange(0, largura)
            lataVelocidade += 1

        if item == 2:
            tela.blit(plastico, (plasticoPosicaoX, plasticoPosicaoY))
            plasticoPosicaoY = plasticoPosicaoY+plasticoVelocidade
            plasticoPosicaoX = plasticoPosicaoX + movimentoX

        if lixoplasticoY < plasticoPosicaoY + plasticoAltura:
            if lixoplasticoX < plasticoPosicaoX and lixoplasticoX+lixoplasticolargura > plasticoPosicaoX or plasticoPosicaoX+plasticoAltura > lixoplasticoX and plasticoPosicaoX+plasticoLargura < lixoplasticoX+lixoplasticolargura:
                habilitaNovoItem = True
                plasticoPosicaoY = -15
                plasticoPosicaoX = random.randrange(0, largura)
                acertos = acertos + 1
                escrevendoPlacar(acertos)

        if plasticoPosicaoY > altura:
            erros = erros + 1
            escrevendoErros(erros)
            habilitaNovoItem = True
            plasticoPosicaoY = -15
            plasticoPosicaoX = random.randrange(0, largura)
            plasticoVelocidade += 1

        if item == 3:
            tela.blit(papel, (papelPosicaoX, papelPosicaoY))
            papelPosicaoY = papelPosicaoY+papelVelociade
            papelPosicaoX = papelPosicaoX + movimentoX

        if lixopapelY < papelPosicaoY + papelAltura:
            if lixopapelX < papelPosicaoX and lixopapelX+lixoplasticolargura > papelPosicaoX or papelPosicaoX+papelAltura > lixopapelX and papelPosicaoX+papelLargura < lixopapelX+lixopapellargura:
                habilitaNovoItem = True
                papelPosicaoY = 0
                papelPosicaoX = random.randrange(0, largura)
                acertos = acertos + 1
                escrevendoPlacar(acertos)

        if papelPosicaoY > altura:
            erros = erros + 1
            escrevendoErros(erros)
            habilitaNovoItem = True
            papelPosicaoY = 0
            papelPosicaoX = random.randrange(0, largura)
            papelVelociade += 1

        if item == 4:
            tela.blit(vidro, (vidroPosicaoX, vidroPosicaoY))
            vidroPosicaoY = vidroPosicaoY+vidroVelocidade
            vidroPosicaoX = vidroPosicaoX + movimentoX

        if lixovidroY < vidroPosicaoY + vidroAltura:
            if lixovidroX < vidroPosicaoX and lixovidroX+lixovidrolargura > vidroPosicaoX or vidroPosicaoX+vidroAltura > lixovidroX and vidroPosicaoX+vidroLargura < lixovidroX+lixovidrolargura:
                habilitaNovoItem = True
                vidroPosicaoY = 0
                vidroPosicaoX = random.randrange(0, largura)
                acertos = acertos + 1
                escrevendoPlacar(acertos)

        if vidroPosicaoY > altura:
            erros = erros + 1
            escrevendoErros(erros)
            habilitaNovoItem = True
            vidroPosicaoY = 0
            vidroVelocidade += 1
            vidroPosicaoX = random.randrange(0, largura)
            acertos = acertos + 1
            escrevendoPlacar(acertos)
        escrevendoPlacar(acertos)
        escrevendoErros(erros)
        pygame.display.update()
        fps.tick(60)


jogo()
