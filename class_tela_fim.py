import pygame
from class_background import Background

class Tela_fim:
    def __init__(self):
        self.background=Background()
        self.assets={
            'death': pygame.image.load("img/morreu.png"),
            'enter': pygame.image.load("img/enter_menu.png"),
            'quadrado': pygame.image.load("img/quadrado.png"),
            'font': pygame.font.Font(None, 50),
        }

        self.assets['death']=pygame.transform.scale(self.assets['death'],(672,91))
        self.assets['enter']=pygame.transform.scale(self.assets['enter'],(672,58))
        self.assets['quadrado']=pygame.transform.scale(self.assets['quadrado'],(70,50))

        self.state={
            "rect": [0,500,850,5],
            "last_updated":0,
            "death":[88,340],
            "enter":[88,440],
            "quadrado":[380,280]
            }
    
    def atualiza_estado(self,state):
        """Recebe eventos, direciona para o menu e zera o contador de posição"""
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_SPACE: 
                state['tela_atual']='menu'
                state['cont']=0
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RETURN:
                state['tela_atual']='menu'
                state['cont']=0
        return True
            
    def desenha(self, window: pygame.Surface,state):
        """Redesenha o background congelado, desenha as imagens da tela morte e o contador de posição(pontuação)"""
        window.fill(("Black"))
        for img in state['bg_final']:
            window.blit(img[0],(img[1][0],img[1][1]))
        for img in state['obs_final']:
            window.blit(img[0],(img[1][0],img[1][1]))
        num = self.assets['font'].render((str(state['cont'])), True, ("White"))
        
        window.blit(self.assets['death'],(self.state['death'][0],self.state['death'][1]))
        window.blit(self.assets['enter'],(self.state['enter'][0],self.state['enter'][1]))
        window.blit(self.assets['quadrado'],(self.state['quadrado'][0],self.state['quadrado'][1]))

        window.blit(num,(400,290))
        pygame.display.update()
            


