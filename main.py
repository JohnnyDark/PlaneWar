import pygame

from game import Game, Status

pygame.init()
bg_size = (480, 700)
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Plane War')
clock = pygame.time.Clock()

if __name__ == '__main__':
    game = Game()
    while game.status == Status.RUNNING:
        background = pygame.image.load('image/background.png').convert_alpha()
        screen.blit(background, (0, 0))
        clock.tick(60)
        pygame.display.flip()
