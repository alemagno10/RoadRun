from curses import savetty
import pygame
class Tela_jogo:
    def __init__(self):
        self.background=Background()
        self.obstacles=Obstacles()

        self.assets={
        "personagem": pygame.image.load("img/personagem_costas0.png")}
        self.assets["personagem"]=pygame.transform.scale(self.assets["personagem"],(110,145))
            
        self.state={
        "personagem": [370,515,830,958],
        }

    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_DOWN:
                self.background.c_state['up']=True
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_UP:
                self.background.c_state['down']=True
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
                self.state['personagem'][0]-=50   
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
                self.state['personagem'][0]+=50
        self.background.mov_bg()
        return True

    def colisão(mouse_x,mouse_y,rect):
        if mouse_x > rect[0] and mouse_x < rect[1]:
            if mouse_y > rect[2] and mouse_y < rect [3]:
                return True
        return False

    def mov_jump(self):
        pass

    def desenha(self, window: pygame.Surface, state):
        window.fill((0,0,0))
        self.background.desenha(window)
        self.obstacles.atualiza_e_desenha(window)    
        window.blit(self.assets['personagem'],(self.state['personagem'][0],self.state['personagem'][2]))
        pygame.display.update()


class Background:
    def __init__(self):
        self.obstacles=Obstacles()
        self.b_assets={
        "rua0": pygame.image.load("img/bg_rua_0.png"),
        "grama3": pygame.image.load("img/bg_grama_3.png"),
        "rua1": pygame.image.load("img/bg_rua_1_sentido.png"),
        "grama2": pygame.image.load("img/bg_grama_2.png"),
        "rua2": pygame.image.load("img/bg_rua_2_sentidos.png"),
        "grama1": pygame.image.load("img/bg_grama_1.png"),
        }

        self.b_state={
        "bg0":[0,830],
        "bg1":[0,660],
        "bg2":[0,490],
        "bg3":[0,320],
        "bg4":[0,150],
        "bg5":[0,-20],
        
        }
        
        self.c_state={
        "t":-120,
        "down":False,
        "up":False,
        }

        for bg in self.b_assets:
            self.b_assets[bg]=pygame.transform.scale(self.b_assets[bg],(851,170))

    def desenha(self,window):
        i=5
        for bg in self.b_assets:
            window.blit(self.b_assets[bg],(self.b_state[f'bg{i}'][0],self.b_state[f'bg{i}'][1]))
            i-=1

    def mov_bg(self):
        if self.c_state['down']:
            for bg in self.b_state:
                self.b_state[bg][1]+=85
                self.obstacles.c_state['truck'][1]+=85
                self.obstacles.c_state['race_W'][1]-=85
                self.c_state['down']=False

        elif self.c_state['up']:
            for bg in self.b_state:
                self.b_state[bg][1]-=85
                self.obstacles.c_state['truck'][1]-=85
                self.obstacles.c_state['race_W'][1]+=85
                self.c_state['up']=False


class Obstacles:
    def __init__(self):
        self.c_assets={
        "truck":pygame.image.load("img/firetruck_E.png"),
        "race_W":pygame.image.load("img/race_W.png")
        }
    
        self.c_assets['truck']=pygame.transform.scale(self.c_assets['truck'],(300,300))
        self.c_assets['race_W']=pygame.transform.scale(self.c_assets['race_W'],(300,300))

        self.c_state={
        "truck":[-300,620],
        "v_truck":500,
        "race_W":[850,535],
        "v_race_W":700,
        "last_updated": 0
        }

    def atualiza_e_desenha(self,window):
        tempo= pygame.time.get_ticks()
        delta_t = (tempo - self.c_state['last_updated'])/1000
        self.c_state['last_updated']=tempo

        self.c_state['truck'][0]+=self.c_state['v_truck']*delta_t 
        self.c_state['race_W'][0]-=self.c_state['v_race_W']*delta_t

        if self.c_state['truck'][0]>900:
            self.c_state['truck'][0]=-300

        elif self.c_state['race_W'][0]<-350:
            self.c_state['race_W'][0]=850

        window.blit(self.c_assets['truck'],(self.c_state['truck'][0],self.c_state['truck'][1]))
        window.blit(self.c_assets['race_W'],(self.c_state['race_W'][0],self.c_state['race_W'][1]))
    




save 

class Tela_jogo:
    def __init__(self):
        self.background=Background()

        self.assets={
        "personagem": pygame.image.load("img/personagem_costas0.png"),
        'font': pygame.font.Font(None, 50),
        }

        self.assets["personagem"]=pygame.transform.scale(self.assets["personagem"],(110,145))
            
        self.state={
        "personagem": [370,515,830,958],
        }

    def atualiza_estado(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_UP:
                self.background.c_state['down']=True
                self.background.c_state['cont']+=1
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_DOWN:
                self.background.c_state['up']=True
                self.background.c_state['cont']-=1
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
                if not self.state['personagem'][0]<30:
                    self.state['personagem'][0]-=50   
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
                if not self.state['personagem'][0]>710:
                    self.state['personagem'][0]+=50

        self.background.atualiza_mov_bg()
        self.background.atualiza_estado()
        return True

    def colisão(mouse_x,mouse_y,rect):
        if mouse_x > rect[0] and mouse_x < rect[1]:
            if mouse_y > rect[2] and mouse_y < rect [3]:
                return True
        return False

    def mov_jump(self):
        pass

    def desenha(self, window: pygame.Surface, state):
        window.fill((0,0,0))
        self.background.desenha(window)
        self.background.add_obstaculos()
        self.background.atualiza_e_desenha(window)    
        window.blit(self.assets['personagem'],(self.state['personagem'][0],self.state['personagem'][2]))
        num = self.assets['font'].render((str(self.background.c_state['cont'])), True, (255,255,255))
        window.blit(num,(5,5))
        pygame.display.update()


class Background:
    def __init__(self):
        self.b_assets={
        "rua0": pygame.image.load("img/bg_rua_0.png"),
        "grama3": pygame.image.load("img/bg_grama_3.png"),
        "rua1": pygame.image.load("img/bg_rua_1_sentido.png"),
        "grama2": pygame.image.load("img/bg_grama_2.png"),
        "rua2": pygame.image.load("img/bg_rua_2_sentidos.png"),
        "grama1": pygame.image.load("img/bg_grama_1.png"),
        }

        self.c_state={
        "t":-120,
        "down":False,
        "up":False,
        "cont":0,
        "cont_maior":0,
        "desenha_fundo_1":True,
        "y":830,
        }

        self.o_assets={
        "tree3": pygame.image.load("img/tree31.png"),
        "truck":pygame.image.load("img/firetruck_E.png"),
        "race_W":pygame.image.load("img/race_W.png"),
        }

        self.o_assets['tree3']=pygame.transform.scale(self.o_assets['tree3'],(141,252))
        self.o_assets['truck']=pygame.transform.scale(self.o_assets['truck'],(300,300))
        self.o_assets['race_W']=pygame.transform.scale(self.o_assets['race_W'],(300,300))

        self.o_state={
        "truck":[-300,620],
        "v_truck":500,
        "race_W":[850,535],
        "v_race_W":700,
        "last_updated": 0
        }

        self.bground=[]
        self.obstaculos=[]
        self.obstaculos_mov=[]

        for bg in self.b_assets:
            self.b_assets[bg]=pygame.transform.scale(self.b_assets[bg],(851,170))
    
    def atualiza_estado(self):
        cont=self.c_state['cont']
        cont_maior=self.c_state['cont_maior']

        if cont>cont_maior: self.c_state['cont_maior']=cont

        if self.c_state['desenha_fundo_1']:
            y=self.c_state['y']
            self.bground.append([self.b_assets["grama1"],[0,y],'o'])
            self.regista_lista()
            print(self.bground)
            self.c_state['desenha_fundo_1']=False   
        
        elif cont_maior %5==0 and cont_maior>=10:
            ultimo_valor=self.bground[-1]
            self.c_state['y']=ultimo_valor[1][1]
            self.regista_lista()

    def regista_lista(self):
        back=self.b_assets
        y=self.c_state['y']
        for i in range(1,10):
            num=random.randint(1,6)
            y-=170
            if num==1: self.bground.append([back["rua1"],[0,y],"r",0])
            elif num==2: self.bground.append([back["rua2"],[0,y],"r",0])
            elif num==3: self.bground.append([back["rua0"],[0,y],"r",0])
            elif num==4: self.bground.append([back["grama1"],[0,y],"g",0])
            elif num==5: self.bground.append([back["grama2"],[0,y],"g",0])
            elif num==6: self.bground.append([back["grama3"],[0,y],"g",0])

    def desenha(self,window):
        for bg in self.bground:
            window.blit(bg[0],(bg[1][0],bg[1][1]))
        for obs in self.obstaculos:
            window.blit(obs[0],(obs[1][0],obs[1][1]))
        for mov in self.obstaculos_mov:
            window.blit(mov[0],(mov[1][0],mov[1][1]))


    def atualiza_mov_bg(self):
        if self.c_state['down']:
            for bg in self.bground:
                bg[1][1]+=85
            for obs in self.obstaculos:
                obs[1][1]+=85
            for mov in self.obstaculos_mov:
                mov[1][1]+=85
            self.c_state['down']=False
        
        elif self.c_state['up']:
            for bg in self.bground:
                bg[1][1]-=85
            for obs in self.obstaculos:
                obs[1][1]-=85
            for mov in self.obstaculos_mov:
                mov[1][1]-=85
            self.c_state['up']=False


    def add_obstaculos(self):
        tempo= pygame.time.get_ticks()
        delta_t = (tempo - self.o_state['last_updated'])/1000
        self.o_state['last_updated']=tempo

        for bg in self.bground:
            if bg[2]=="g":
                tree=self.o_assets['tree3']
                radomizador=random.randint(1,15)
                
                pos_x=radomizador*52
                pos_y=bg[1][1]-170
                if self.c_state['cont'] <= 40:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=15 and bg[3]<6:
                        self.obstaculos.append([tree,[pos_x,pos_y]])
                        
                elif self.c_state['cont'] <= 80:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=20 and bg[3]<7:
                        self.obstaculos.append([tree,[pos_x,pos_y]])
                        
                elif self.c_state['cont'] <= 120:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=25 and bg[3]<8:
                        self.obstaculos.append([tree,[pos_x,pos_y]])
                        
                else:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=35 and bg[3]<10:
                        self.obstaculos.append([tree,[pos_x,pos_y]])
                bg[3]+=1
            
            elif bg[2]=="r":
                race_W=self.o_assets['race_W']
                truck=self.o_assets['truck']

                left_pos_x=self.o_state['v_truck']*delta_t
                left_pos_y=bg[1][1]

                right_pos_x=self.o_state['v_race_W']*delta_t
                right_pos_y=bg[1][1]

                self.obstaculos_mov.append([race_W,[right_pos_x, right_pos_y]])
                self.obstaculos_mov.append([truck,[left_pos_x,left_pos_y]])
            
                
    def atualiza_e_desenha(self,window):
        pass

        # if self.o_state['truck'][0]>900:
        #     self.o_state['truck'][0]=-300

        # elif self.o_state['race_W'][0]<-350:
        #     self.o_state['race_W'][0]=850

        # window.blit(self.c_assets['truck'],(self.o_state['truck'][0],self.o_state['truck'][1]))
        # window.blit(self.c_assets['race_W'],(self.o_state['race_W'][0],self.o_state['race_W'][1]))