import pygame
from State import StateManager, GameState

def main():
    pygame.init()

    background_colour = (0, 0, 0)
    (width, height) = (800, 600)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tic Tac Toe")

    stateManager = StateManager(GameState())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            stateManager.processEvent(event)

        stateManager.update()

        screen.fill(background_colour)
        stateManager.render(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()