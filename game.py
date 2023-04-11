import pygame
import os
import random

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))

FPS = 60

meteorList = []


def getScaledSize(image):
    width = ((WIDTH/image.get_width()) * image.get_width())
    height = int((HEIGHT/image.get_height()) * image.get_height())
    return (width, height)


bg = pygame.image.load(os.path.join('assets', 'background', 'bg2.jpg'))
size = getScaledSize(bg)


def drawFrame(spaceship, spaceship2):
    WIN.fill(pygame.Color(255, 255, 255))
    WIN.blit(pygame.transform.scale(bg, size=size), dest=(0, 0))
    spaceship.draw()
    spaceship2.draw()

    global meteorList
    for meteor in meteorList:
        meteor.draw()

    pygame.display.update()


def handleSpaceShipMovement(spaceship, keys_pressed):
    if keys_pressed[pygame.K_w] and spaceship.y > (HEIGHT//2):
        spaceship.y -= spaceship.velocity

    if keys_pressed[pygame.K_s] and spaceship.y <= HEIGHT-spaceship.getHeight()-10:
        spaceship.y += spaceship.velocity

    if keys_pressed[pygame.K_a] and spaceship.x > 0:
        spaceship.x -= spaceship.velocity

    if keys_pressed[pygame.K_d] and spaceship.x < WIDTH-spaceship.getWidth():
        spaceship.x += spaceship.velocity


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

    def __init__(self, x, y, WIN, choice, velocity):
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

        self.velocity = velocity

    def draw(self):
        self.WIN.blit(self.SPACESHIP, dest=(self.x, self.y))

    def getWidth(self):
        return self.SCALED_SPACESHIP_IMAGE_WIDTH

    def getHeight(self):
        return self.SCALED_SPACESHIP_IMAGE_HEIGHT


class Meteor():

    def __init__(self, x, y, WIN):
        self.x = x
        self.y = y
        num = random.randrange(1, 11)
        self.METEOR_IMAGE = pygame.image.load(os.path.join(
            'assets', 'meteors', 'Meteor_{:02d}.png'.format(num)))
        self.SCALED_METEOR_IMAGE_HEIGHT = int(
            self.METEOR_IMAGE.get_height()*0.3)
        self.SCALED_METEOR_IMAGE_WIDTH = int(self.METEOR_IMAGE.get_width()*0.3)

        self.METEOR = pygame.transform.scale(self.METEOR_IMAGE, size=(
            self.SCALED_METEOR_IMAGE_WIDTH, self.SCALED_METEOR_IMAGE_HEIGHT))

        self.METEOR_VELOCITY = random.randrange(5, 20)

        self.WIN = WIN

        self.meteorRect = pygame.Rect(
            self.x, self.y, self.SCALED_METEOR_IMAGE_WIDTH, self.SCALED_METEOR_IMAGE_HEIGHT)

    def draw(self):
        self.WIN.blit(self.METEOR, dest=(self.x, self.y))
        self.update()

    def update(self):
        self.y += self.METEOR_VELOCITY

    def getWidth(self):
        return self.SCALED_METEOR_IMAGE_WIDTH

    def getHeight(self):
        return self.SCALED_METEOR_IMAGE_HEIGHT


def generateMeteors(num):
    meteorList = []

    for i in range(num):
        x = random.randrange(0, 900)
        print(x)
        y = -random.randrange(100, 700)
        meteor = Meteor(x, y, WIN)
        meteorList.append(meteor)

    return meteorList


def checkMeteorCollision():
    for meteor in meteorList:
        if (meteor.y >= HEIGHT):
            meteorList.remove(meteor)
            meteorList.append(Meteor(random.randrange(
                0, 950), -random.randrange(100, 700), WIN))
            break


def main():

    clock = pygame.time.Clock()

    spaceship = Spaceship((WIDTH//2), HEIGHT, WIN, 2, 10)
    spaceship2 = Spaceship(200, 200, WIN, 3, 15)

    global meteorList
    meteorList = generateMeteors(5)

    run = True
    while (run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

        keys_pressed = pygame.key.get_pressed()

        handleSpaceShipMovement(spaceship, keys_pressed)

        drawFrame(spaceship, spaceship2)
        checkMeteorCollision()


if __name__ == "__main__":
    main()
