import pygame
import os

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))

FPS = 60

SHIP_VELOCITY = 5


def drawFrame(spaceship):
    WIN.fill(pygame.Color(255, 255, 255))
    spaceship.draw()
    pygame.display.update()


def handleSpaceShipMovement(spaceship, keys_pressed):
    if keys_pressed[pygame.K_w] and spaceship.y > (HEIGHT//2):
        spaceship.y -= SHIP_VELOCITY

    if keys_pressed[pygame.K_s] and spaceship.y <= HEIGHT-spaceship.getHeight():
        spaceship.y += SHIP_VELOCITY

    if keys_pressed[pygame.K_a] and spaceship.x > 0:
        spaceship.x -= SHIP_VELOCITY

    if keys_pressed[pygame.K_d] and spaceship.x < WIDTH-spaceship.getWidth():
        spaceship.x += SHIP_VELOCITY


class Spaceship():
    SPACESHIP_IMAGE2 = pygame.image.load(
        os.path.join("assets", "spaceship", "spaceship2.png"))

    SPACESHIP_IMAGE1 = pygame.image.load(
        os.path.join("assets", "spaceship", "spaceship1.png"))

    SPACESHIP_IMAGE3 = pygame.image.load(
        os.path.join("assets", "spaceship", "spaceship3.png"))

    spaceship_dict = {
        1: SPACESHIP_IMAGE1,
        2: SPACESHIP_IMAGE2,
        3: SPACESHIP_IMAGE3
    }

    def __init__(self, x, y, WIN, choice):
        self.SCALED_SPACESHIP_IMAGE_HEIGHT = int(
            self.spaceship_dict[choice].get_height() * 0.08)
        self.SCALED_SPACESHIP_IMAGE_WIDTH = int(
            self.spaceship_dict[choice].get_width() * 0.08)

        self.SPACESHIP = pygame.transform.scale(
            self.spaceship_dict[choice], size=(self.SCALED_SPACESHIP_IMAGE_WIDTH, self.SCALED_SPACESHIP_IMAGE_HEIGHT))

        self.x = x-(self.SCALED_SPACESHIP_IMAGE_WIDTH//2)
        self.y = y-self.SCALED_SPACESHIP_IMAGE_HEIGHT
        self.WIN = WIN
        self.spaceshipRect = pygame.Rect(
            self.x, self.y, self.SCALED_SPACESHIP_IMAGE_WIDTH, self.SCALED_SPACESHIP_IMAGE_HEIGHT)

    def draw(self):
        self.WIN.blit(self.SPACESHIP, dest=(self.x, self.y))

    def getWidth(self):
        return self.SCALED_SPACESHIP_IMAGE_WIDTH

    def getHeight(self):
        return self.SCALED_SPACESHIP_IMAGE_HEIGHT


def main():

    spaceship = Spaceship((WIDTH//2), HEIGHT, WIN, 3)
    clock = pygame.time.Clock()

    run = True
    while (run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

        keys_pressed = pygame.key.get_pressed()

        handleSpaceShipMovement(spaceship, keys_pressed)

        drawFrame(spaceship)


if __name__ == "__main__":
    main()
