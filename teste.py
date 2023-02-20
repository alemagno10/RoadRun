import pygame

class Tela_jogo:
    def __init__(self):
        self.assets={
        "personagem": pygame.image.load('personagem_costas0.png')
            }

        self.assets["personagem"]=pygame.transform.scale(self.assets["personagem"],(128,170))
        
        self.state={
        "personagem": [384,512,850,1020],
        "gravity":2,
        "jump_size":30,
        "ground": 1200*4/6,

        "still":0,
        "jumping":1,
        "falling":2
            }

        self.speedy=0
    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONUP:
                pass
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
                self.state['personagem'][0]-=50
                self.jump()    
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
                self.state['personagem'][0]+=50
        return True

    def colisão(mouse_x,mouse_y,rect):
        if mouse_x > rect[0] and mouse_x < rect[1]:
            if mouse_y > rect[2] and mouse_y < rect [3]:
                return True
        return False

    def mov_jump(self):
        pass

    def update(self):
        self.speedy += self.state['gravity']

        if self.speedy > 0:
            self.state = self.state['falling']
        self.rect.y += self.speedy
        # Se bater no chão, para de cair
        if self.rect.bottom > self.state['personagem'][2]:
            # Reposiciona para a posição do chão
            self.rect.bottom = self.state['personagem'][2]
            # Para de cair
            self.speedy = 0
            # Atualiza o estado para parado
            self.state = self.state['still']

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == self.state['still']:
            self.speedy -= self.state['jump_size']
            self.state = self.state['jumping']

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#    
    def desenha(self, window: pygame.Surface, state):
        window.fill((0,0,0))    
        self.blit_img(window)
        pygame.display.update()

    def blit_img(self,window):
        window.blit(self.assets['personagem'],(self.state['personagem'][0],self.state['personagem'][2]))
