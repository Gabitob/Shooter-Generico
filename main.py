import pygame
from pygame.locals import *
from Player import Player
from Explosoes import Explosao
from Inimigos import Inimigos
#from Saudavel import Saudavel
from Tiro import Tiro
import random
from sys import exit

#Iniciar o pygame e criar janela
pygame.init()
#Resolução da janela
largura = 840
altura = 480
display = pygame.display.set_mode((largura, altura))
#Nome do jogo
pygame.display.set_caption("Shooter Genérico 2")

#Groups
objectGroup = pygame.sprite.Group()
inimigosGroup = pygame.sprite.Group()
tiroGroup = pygame.sprite.Group()
saudavelGroup = pygame.sprite.Group()
explosaoGroup = pygame.sprite.Group()

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)


# Background
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("./data/space.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

Player = Player(objectGroup)
morreu = False

#Music
pygame.mixer.music.load("data/theme.ogg")
pygame.mixer.music.play(-1)

#Sounds
shoot = pygame.mixer.Sound("data/laser_shooting_sfx.wav")

#Loop para a tela não fechar depois de abrir
gameLoop = True
timer = 20
clock = pygame.time.Clock()

def reiniciar_jogo():
    global pontos, morreu
    pontos = 0
    morreu = False


if __name__ == '__main__':
    while True:
        clock.tick(60)
        mensagem = f'Pontos:{pontos}'
        texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not morreu:
                    shoot.play()
                    newTiro = Tiro(objectGroup, tiroGroup)
                    newTiro.rect.center = Player.rect.center

        #Update Logic:
        if not morreu:
            objectGroup.update()
            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newDepression = Inimigos(objectGroup, inimigosGroup)
                    #newSaudavel = Saudavel(objectGroup, saudavelGroup)

            colisoes = collisions = pygame.sprite.spritecollide(Player, inimigosGroup, False, pygame.sprite.collide_mask)
            #colisoes = collisions1 = pygame.sprite.spritecollide(Player, saudavelGroup, False, pygame.sprite.collide_mask)

            if colisoes:
                morreu = True
                while morreu:
                    display.fill((255, 255, 255))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                reiniciar_jogo()



            tiro = hits = pygame.sprite.groupcollide(tiroGroup, inimigosGroup, True, True, pygame.sprite.collide_mask)
            #tiro = hits1 = pygame.sprite.groupcollide(tiroGroup, saudavelGroup, True, True, pygame.sprite.collide_mask)

            if tiro:
                pontos += 1
                Explosao


        #Draw:
        display.fill([0, 231, 235])
        objectGroup.draw(display)
        display.blit(texto_formatado, (350, 10))
        pygame.display.update()
