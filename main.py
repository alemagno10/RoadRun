import pygame
from class_menu import Menu
from class_tela_jogo import Tela_jogo
from class_tela_fim import Tela_fim

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((850, 1000), flags=pygame.SCALED)
    pygame.key.set_repeat(50)
    
    assets={}

    state={
        'menu': Menu(),
        'tela_jogo': Tela_jogo(),
        'tela_fim': Tela_fim(),
        'tela_atual': "menu",
        'cont': 0,
    }
    return window,assets,state

def atualiza_estado(state):
    """Recebe atualiza estado da tela atual"""    
    return state[state['tela_atual']].atualiza_estado(state)  
            
def desenha(window: pygame.Surface, assets, state):
    """Recebe atualiza estado da tela atual"""
    state[state['tela_atual']].desenha(window,state)
    
def finaliza():
    pygame.quit()

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window,assets, state)

if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()