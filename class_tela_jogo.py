import pygame
from class_background import Background

class Tela_jogo:
    def __init__(self):
        self.background=Background()

        self.assets={
        'font': pygame.font.Font(None, 50),
        'grass_sound': pygame.mixer.Sound("sound/grass_steps.wav"),
        'ouch_sound': pygame.mixer.Sound("sound/ouch!.wav")
        }

        self.state={}

    def atualiza_estado(self,state):
        """Recebe eventos, verifica se há colisões com árvores, movimenta posição do personagem/mapa e adiciona som de passos"""
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False

            elif ev.type == pygame.KEYUP and ev.key == pygame.K_UP and self.background.pode_mover(0,-85):
                    self.background.c_state['down']=True
                    state['cont']+=1
                    self.assets['grass_sound'].play()
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_DOWN and self.background.pode_mover(0,+85) and state['cont']>0:
                    self.background.c_state['up']=True
                    state['cont']-=1
                    self.assets['grass_sound'].play()

            elif ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT and self.background.pode_mover(-50,0):
                    if not self.background.o_state['personagem'][0]<30:
                        self.background.o_state['personagem'][0]-=50
                        self.assets['grass_sound'].play()

            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT and self.background.pode_mover(+50,0):  
                if not self.background.o_state['personagem'][0]>710:
                    self.background.o_state['personagem'][0]+=50
                    self.assets['grass_sound'].play()

        self.background.atualiza_mov_bg()
        self.background.atualiza_estado(state)
        self.background.add_obstaculos(state)   
        
        if self.background.colisão_carro(state):
            self.assets['ouch_sound'].play()
            self.background=Background()

        return True

    def desenha(self, window: pygame.Surface, state):
        """Blit da função background.desenha, desenha o contador da posição do personagem"""
        window.fill((0,255,0))
        self.background.desenha(window,state)
        num = self.assets['font'].render((str(state['cont'])), True, (255,255,255))
        window.blit(num,(5,5))
        pygame.display.update()




            