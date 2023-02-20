import pygame
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1000, 1200), flags=pygame.SCALED)
    pygame.key.set_repeat(50)

    default_font_name = pygame.font.get_default_font()
    def_font = pygame.font.Font(default_font_name, 30)


    assets= {
        "fonte": def_font,
        "play": pygame.image.load('play3.png'),
        "perso": pygame.image.load('caracters.png'),
        "multiplayer": pygame.image.load('multiplayer.png'),
        "crossy": pygame.image.load('crossy_road.png'),

        "personagem": pygame.image.load('personagem_costas0.png')
        }

    assets["personagem"]=pygame.transform.scale(assets["personagem"],(128,170))

    state= {
        'inicio': True,
        'mov_menu': False,

        'play': [340,640,900,1000],
        'perso': [240, 334 ,901, 1002],
        'multiplayer': [648, 742, 901, 1002],
        'crossy': [300,700,250,479],       
        
        'azul': (0,0,255),
        'cinza': (10,10,10),

        'tela_jogo': False,
        'tela_personagens': False,
        'tela_multiplayer': False,

        'personagem': [384,576,850,1056]
        }

    return window,assets,state



def finaliza():
    pygame.quit()

def blit_img(window,assets,state):    
    window.blit(assets["crossy"], (state["crossy"][0], state["crossy"][2]))
    window.blit(assets["play"], (state["play"][0], state["play"][2]))
    window.blit(assets["perso"], (state["perso"][0], state["perso"][2]))
    window.blit(assets["multiplayer"], (state["multiplayer"][0], state["multiplayer"][2]))

def desenha(window: pygame.Surface, assets, state):
    window.fill((0,0,0))
    if state['inicio']:
        blit_img(window,assets,state)
    elif state['tela_jogo']:
        window.blit(assets["personagem"], (state["personagem"][0], state["personagem"][2]))
    pygame.display.update()

def colisão(mouse_x,mouse_y,rect):
    if mouse_x > rect[0] and mouse_x < rect[1]:
        if mouse_y > rect[2] and mouse_y < rect [3]:
            return True
    return False

def atualiza_estado(state):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        elif ev.type == pygame.MOUSEBUTTONUP:
            if colisão(ev.pos[0],ev.pos[1],state['play']):
                print("colisao")
                state['mov_menu']=True
                state['tela_jogo']=True
            elif colisão(ev.pos[0],ev.pos[1],state['perso']):
                print("colisao personagens")
                state['mov_menu']=True
                state['tela_personagens']=True
            elif colisão(ev.pos[0],ev.pos[1],state['multiplayer']):
                print("colisao multiplayer")
                state['mov_menu']=True
                state['tela_multiplayer']=True
        
        if state['tela_jogo']:
            if ev.type == pygame.KEYUP and ev.key == pygame.K_LEFT:
                state['personagem'][0]-=50
            elif ev.type == pygame.KEYUP and ev.key == pygame.K_RIGHT:
                state['personagem'][0]+=50
            # elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP:
            #     state['personagem'][2]-=20
            # elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN:
            #     state['personagem'][2]+=20


    return True

def movimenta_menu(window: pygame.Surface,state,assets):
    loop=True
    while loop:
        window.fill((0,0,0))
        state["crossy"][2]-=10
        state["play"][2]+=5
        state["perso"][2]+=5
        state["multiplayer"][2]+=5

        blit_img(window,assets,state)
        
        pygame.display.update()

        if state["crossy"][2] + state["crossy"][3] + 30 < 0: 
            state['inicio']=False
            state['mov_menu']=False
            loop = False

def reset_menu(state):
    state['play']=[340,640,900,1000]
    state['perso']=[240, 334 ,901, 1002]
    state['multiplayer']=[648, 742, 901, 1002]
    state['crossy']=[300,700,250,479]


def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)
        if state['mov_menu']:
            movimenta_menu(window,state,assets)
            reset_menu(state)
        # elif state['tela_jogo']:
        #     game(window, assets, state)

if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()
