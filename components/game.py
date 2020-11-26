import pygame

from utils.constants import(
        SCREEN_HEIGHT,
        SCREEN_WIDTH,
        TITLE
    )

class Game:

    def __init__(self):
        pygame.init() # aca se inicia el "juego"
        pygame.display.set_caption(TITLE) # se muestra el titulo del juego
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # se configura el alto y ancho del juego

    def run(self):
        self.create_components()
        # Game loop:
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def create_components(self):
        pass
    def update(self):
        pass
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def draw(self):
        pass

