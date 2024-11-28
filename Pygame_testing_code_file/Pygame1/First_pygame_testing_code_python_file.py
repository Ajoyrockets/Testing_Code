import pygame 
import os

WIDTH , HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello there ,OBI-WAN you are a bold one")

WHITE = (255,255,255)

FPS = 60

GAME_FILE_LOCATION = os.path.dirname(__file__)
IMAGES = os.path.join(GAME_FILE_LOCATION,'Assets', 'Images')
SOUNDS = os.path.join(GAME_FILE_LOCATION,'Assets', 'Sounds')



YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join(IMAGES, 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE,(60,40)),270)


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join(IMAGES, 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(60,40)),90)


def draw_window():
    WIN.fill((WHITE))
    WIN.blit(YELLOW_SPACESHIP_IMAGE,(500,100))
    WIN.blit(RED_SPACESHIP_IMAGE,(100,100))
    pygame.display.update()


def main():
    red = pygame.Rect(100,300 )

    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick (FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main() 
