import pygame
class Menu:
    def __init__(self):
        self.assets= {
        "play": pygame.image.load('img/play3.png'),
        "perso": pygame.image.load('img/caracters.png'),
        "multiplayer": pygame.image.load('img/multiplayer.png'),
        "road_run":pygame.image.load('img/road_run.png'),
        "bg_fundo": pygame.image.load('img/inicio_bg.png')
            }

        self.assets['play']=pygame.transform.scale(self.assets['play'],(254,83))
        self.assets['perso']=pygame.transform.scale(self.assets['perso'],(80,83))
        self.assets['multiplayer']=pygame.transform.scale(self.assets['multiplayer'],(80,83))
        self.assets['road_run']=pygame.transform.scale(self.assets['road_run'],(500,70))

        self.state= {
        'inicio': True,
        'mov_menu': False,
        'restart_menu': False,

        'play': [298,552,800,883],
        'perso': [208, 288 ,800, 883],
        'multiplayer': [562, 642, 800, 883],
        'road_run':[175,675,250,295],    

            }
    

    def atualiza_estado(self,state):
        """ Vefifica qual dos botões foi pressionado e regista proxima tela"""
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                if self.colisão(ev.pos[0],ev.pos[1],self.state['play']):
                    self.state['mov_menu']=True
                    self.state['prox_etapa']='tela_jogo'

                elif self.colisão(ev.pos[0],ev.pos[1],self.state['perso']):
                    self.state['mov_menu']=True
                    self.state['prox_etapa']='tela_personagens'

                elif self.colisão(ev.pos[0],ev.pos[1],self.state['multiplayer']):
                    self.state['mov_menu']=True
                    self.state['prox_etapa']='tela_multiplayer'
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RETURN:
                self.state['mov_menu']=True
                self.state['prox_etapa']='tela_jogo'
        return True


    def colisão(self, mouse_x,mouse_y,rect):
        """Recebe posição do mouse e verifica se há colisão com botão"""
        if mouse_x > rect[0] and mouse_x < rect[1]:
            if mouse_y > rect[2] and mouse_y < rect [3]:
                return True
        return False

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
    def desenha(self,window: pygame.Surface, state):
        """"""   
        window.fill((0,0,0))
        self.blit_img(window)
        pygame.display.update()

        if self.state['mov_menu']:
            loop=True
            while loop:
                window.fill((0,0,0))
                self.state["road_run"][2]-=10
                self.state["play"][2]+=5
                self.state["perso"][2]+=5
                self.state["multiplayer"][2]+=5

                self.blit_img(window)
                
                pygame.display.update()

                if self.state["road_run"][2] + self.state["road_run"][3] < 0: 
                    
                    self.state['mov_menu']=False
                    self.state['restart_menu']=True
                    loop = False

                    if self.state['prox_etapa'] == 'tela_jogo':
                        state['tela_atual']='tela_jogo'
                    elif self.state['prox_etapa'] =='tela_personagens':
                        state['tela_atual']='tela_personagens'
                    elif self.state['prox_etapa'] =='tela_multiplayer':
                        state['tela_atual']='tela_multiplayer'

        elif self.state['restart_menu']:
            self.reset_menu()
            self.state['restart_menu']=False

    #----------------------------------------------------------------#    
    def reset_menu(self):
        """Reseta menu para posição original"""
        self.state['play']=[298,552,800,883]
        self.state['perso']=[208, 288 ,800, 883]
        self.state['multiplayer']=[562, 642, 800, 883]
        self.state['road_run']=[175,675,250,295]

    def blit_img(self,window):
        window.blit(self.assets['bg_fundo'],(0,0))   
        window.blit(self.assets["road_run"], (self.state["road_run"][0], self.state["road_run"][2]))
        window.blit(self.assets["play"], (self.state["play"][0], self.state["play"][2]))
        window.blit(self.assets["perso"], (self.state["perso"][0], self.state["perso"][2]))
        window.blit(self.assets["multiplayer"], (self.state["multiplayer"][0], self.state["multiplayer"][2]))   