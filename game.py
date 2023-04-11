import pygame
import os
import random
import game_objects

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))

FPS = 60

NO_OF_METEORS = 5
SPACESHIP_NO = 2
SPACESHIP_VELOCITY = 10
GAME_BACKGROUND = 1

meteorList = []
missileList = []


def getScaledSize(image):
    width = ((WIDTH/image.get_width()) * image.get_width())
    height = int((HEIGHT/image.get_height()) * image.get_height())
    return (width, height)


bg = pygame.image.load(os.path.join(
    'assets', 'background', f'bg{GAME_BACKGROUND}.jpg'))
size = getScaledSize(bg)


def drawFrame(spaceship):
    WIN.fill(pygame.Color(255, 255, 255))
    WIN.blit(pygame.transform.scale(bg, size=size), dest=(0, 0))
    spaceship.draw()

    global meteorList
    for meteor in meteorList:
        meteor.draw()

    for missile in missileList:
        missile.draw()

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


def generateMeteors(num):
    meteorList = []

    for i in range(num):
        x = random.randrange(0, 900)
        y = -random.randrange(100, 700)
        meteor = game_objects.Meteor(x, y, WIN)
        meteorList.append(meteor)

    return meteorList


def checkMeteorCollision():
    for meteor in meteorList:
        if (meteor.y >= HEIGHT):
            meteorList.remove(meteor)
            meteorList.append(game_objects.Meteor(random.randrange(
                0, 950), -random.randrange(100, 700), WIN))
            break


def checkMissileCollision():
    global missileList
    for missile in missileList:
        if (missile.y < 0):
            missileList.remove(missile)
            break


def main():

    clock = pygame.time.Clock()

    spaceship = game_objects.Spaceship(
        (WIDTH//2), HEIGHT, WIN, SPACESHIP_NO, SPACESHIP_VELOCITY)

    global meteorList, bulletList
    meteorList = generateMeteors(NO_OF_METEORS)

    run = True
    while (run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE and len(missileList) < 2):
                    missileList.append(
                        game_objects.Missile(spaceship.x + (spaceship.getWidth()//2)-5, spaceship.y, WIN))

        keys_pressed = pygame.key.get_pressed()
        handleSpaceShipMovement(spaceship, keys_pressed)

        checkMeteorCollision()
        checkMissileCollision()

        drawFrame(spaceship)


if __name__ == "__main__":
    main()
