import pygame
import random

class Background:
    def __init__(self):
        self.b_assets={
        "personagem": pygame.image.load("img/personagem_costas0.png"),
        "rua0": pygame.image.load("img/bg_rua_0.png"),
        "grama3": pygame.image.load("img/bg_grama_3.png"),
        "rua1": pygame.image.load("img/bg_rua_1_sentido.png"),
        "grama2": pygame.image.load("img/bg_grama_2.png"),
        "rua2": pygame.image.load("img/bg_rua_2_sentidos.png"),
        "grama1": pygame.image.load("img/bg_grama_1.png"),
        }

        self.c_state={
        #"t":-120,
        "down":False,
        "up":False,
        "cont":0,
        "cont_maior":0,
        "desenha_fundo_1":True,
        "y":830,
        }

        self.o_assets={
        "tree3": pygame.image.load("img/tree31.png"),
        "truck":pygame.image.load("img/firetruck_D.png"),
        "police_W":pygame.image.load("img/police_W.png"),
        "race_W":pygame.image.load("img/race_W.png"),
        "race_D":pygame.image.load("img/raceFuture_D.png"),
        }

        self.o_assets['tree3']=pygame.transform.scale(self.o_assets['tree3'],(141,252))
        

        for obstacle in self.o_assets:
            if obstacle != "tree3":
                self.o_assets[obstacle]=pygame.transform.scale(self.o_assets[obstacle],(300,300))

        self.o_state={
        "personagem": [370,745],
        "truck":[300,620],
        "v_truck":500,
        "race_W":[850,535],
        "v_race_W":700,
        "last_updated": 0,
        }

        self.bground=[]
        self.obstaculos=[]
        self.obstaculos_mov=[]

        for bg in self.b_assets:
            if bg != 'personagem':
                self.b_assets[bg]=pygame.transform.scale(self.b_assets[bg],(852,170))


    #--------- Metodos de colisão -------#
    def pode_mover(self,dx,dy):
        """Recebe a posição futura do personagem, cria uma hitbox e verica se há colisão com alguma árvore"""
        rect1=pygame.Rect(self.o_state['personagem'][0]+30+dx, self.o_state['personagem'][1]+100+dy, 56,50)
        for obstaculo in self.obstaculos:
            rect2 = pygame.Rect(obstaculo[1][0],obstaculo[1][1]+200, 100, 52)
            if pygame.Rect.colliderect(rect1,rect2):
                return False
        return True
    
    def colisão_carro(self,state):
        """Cria uma hitbox para carros e personagem, e verifica se há colisão"""
        rect1=pygame.Rect(self.o_state['personagem'][0]+30, self.o_state['personagem'][1]+100, 56,50)
        for obstaculo in self.obstaculos_mov:
            rect2=pygame.Rect(obstaculo[1][0]+80,obstaculo[1][1]+150, 100, 52)
            if pygame.Rect.colliderect(rect1,rect2): 
                state['tela_atual']='tela_fim'
                return True
        return False


    #-------- Geração de Cenário --------#
    def atualiza_estado(self,state):
        """Desenha_fundo_1 quando True produz a primeira parte do mapa, nos demais momentos a função dá continuidade à geração de cenário"""
        cont=state['cont']
        cont_maior=self.c_state['cont_maior']

        if cont>cont_maior: self.c_state['cont_maior']=cont

        if self.c_state['desenha_fundo_1']:
            y=self.c_state['y']
            self.bground.append([self.b_assets["grama1"],[0,y],'o'])
            self.regista_lista()
            self.c_state['desenha_fundo_1']=False   
        
        elif cont_maior %15==0 and cont_maior>=15:
            ultimo_valor=self.bground[-1]
            self.c_state['y']=ultimo_valor[1][1]
            self.regista_lista()

    def regista_lista(self):
        """Produz uma lista de backgrounds que formarão o mapa. Lista bground recebe imagem, posição, tag(rua ou grama), e limitador da qtd de obstáculos"""
        back=self.b_assets
        y=self.c_state['y']

        for i in range(1,20):
            num=random.randint(1,6)
            y-=170
            if num==1: self.bground.append([back["rua1"],[0,y],"r1",True])
            elif num==2: self.bground.append([back["rua2"],[0,y],"r",True])
            elif num==3: self.bground.append([back["rua0"],[-2,y],"r",True])
            elif num==4: self.bground.append([back["grama1"],[0,y],"g",0])
            elif num==5: self.bground.append([back["grama2"],[0,y],"g",0])
            elif num==6: self.bground.append([back["grama3"],[0,y],"g",0])


    #------ Atualização da posição de carros, background e obstáculos -----#
    def atualiza_mov_bg(self):
        """Atualiza a posição horizontal dos carros e atualiza a posição de todos os obstáculos"""
        tempo= pygame.time.get_ticks()
        delta_t = (tempo - self.o_state['last_updated'])/1000
        self.o_state['last_updated']=tempo

        for mov in self.obstaculos_mov:
            if mov[2]=='d':
                mov[1][0]-=self.o_state['v_race_W']*delta_t
                if mov[1][0]<-300: mov[1][0]=850
            else:
                mov[1][0]+=self.o_state['v_truck']*delta_t
                if mov[1][0]>850: mov[1][0]=-300

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


    #--------- Desenha Objetos ---------#
    def desenha(self,window,state):
        """Desenha todos o backgrounds da lista bground. Gera uma lista de obstáculos que são ordenados pela pos_y e depois desenhados. 
        Registra a lista atual no state do arquivo main para ser desenhada na tela de morte """
        pos=self.o_state
        self.b_assets["personagem"]=pygame.transform.scale(self.b_assets["personagem"],(110,145))

        for bg in self.bground:
            window.blit(bg[0],(bg[1][0],bg[1][1]))
        
        lista_objetos=[]
        for obs in self.obstaculos:
            lista_objetos.append(obs)
        for mov in self.obstaculos_mov:
            lista_objetos.append(mov)

        state['bg_final']=self.bground
        state['obs_final']=lista_objetos
        state['obs_final'].sort(key=pega_y)
        state['perso_final']=[self.b_assets['personagem'],[pos['personagem'][0],pos['personagem'][1]],'p']
        
        lista_objetos.append([self.b_assets['personagem'],[pos['personagem'][0],pos['personagem'][1]],'p'])
        lista_objetos.sort(key=pega_y)

        for obj in lista_objetos:
            window.blit(obj[0],(obj[1][0],obj[1][1]))


    #------ Geração de Obstáculos -------#
    def add_obstaculos(self,state):
        """Navega pela lista de backgrounds, vefica as tags, adiciona aleatóriamente os devidos obstáculos e regista na lista obstáculos"""
        for bg in self.bground:
            if bg[2]=="g":
                tree=self.o_assets['tree3']
                radomizador=random.randint(1,15)
                
                pos_x=radomizador*52
                pos_y=bg[1][1]-170
                if state['cont'] <= 40:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=15 and bg[3]<6:
                        self.obstaculos.append([tree,[pos_x,pos_y],"a"])
                        
                elif state['cont'] <= 80:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=20 and bg[3]<7:
                        self.obstaculos.append([tree,[pos_x,pos_y],"a"])
                        
                elif state['cont'] <= 120:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=25 and bg[3]<8:
                        self.obstaculos.append([tree,[pos_x,pos_y],"a"])
                        
                else:
                    chance_arvore=random.randint(0,100)
                    if chance_arvore <=35 and bg[3]<10:
                        self.obstaculos.append([tree,[pos_x,pos_y],"a"])
                bg[3]+=1
            
            elif bg[2]=="r": #r: rua de dois sentidos
                race_W=self.o_assets['race_W']
                truck=self.o_assets['truck']
                
                pos_x1=random.randint(1,850)
                pos_x2=random.randint(1,850)
                pos_y=bg[1][1]

                if bg[3]:
                    self.obstaculos_mov.append([race_W,[pos_x1,pos_y-125],'d'])
                    self.obstaculos_mov.append([truck,[pos_x2,pos_y-45],'e'])
                    bg[3]=False

            elif bg[2]=="r1":   
                pos_x1=random.randint(1,850)
                pos_x2=random.randint(1,850)
                pos_y=bg[1][1]
                
                sentido=random.randint(1,2)
                if sentido==1: 
                    tag="e"
                    race=self.o_assets['race_D']
                    truck=self.o_assets['truck']
                else: 
                    tag="d"
                    race=self.o_assets['race_W']
                    truck=self.o_assets['police_W']

                if bg[3]:    
                    self.obstaculos_mov.append([race,[pos_x1,pos_y-125],tag])
                    self.obstaculos_mov.append([truck,[pos_x2,pos_y-45],tag])
                    bg[3]=False

def pega_y(lista):
    """Recebe a lista de objetos, extrai a pos_y de todos para fazer o blit na ordem correta de acordo com a profundade"""
    if lista[2]=="a":
        return lista[1][1]+100
    return lista[1][1]
