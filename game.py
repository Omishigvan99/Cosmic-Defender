import pygame
import os
import random
import game_objects
import DB

pygame.font.init()

PAUSE = False
WIDTH = 1000
HEIGHT = 700
WIN = None

FPS = 60

NO_OF_METEORS = 5
SPACESHIP_NO = 2
SPACESHIP_VELOCITY = 10
GAME_BACKGROUND = 1
SPACESHIP_HEALTH = 100
HEALTH_DECREMENT_FACTOR = 10
SCORE_INCREMENT_FACTOR = 1
METEOR_HIT_INCREMENT_FACTOR = 5
SPACESHIP_HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
SCORE = 0
SCORE_FONT = pygame.font.SysFont("comicsans", 40)
GAME_OVER_FONT = pygame.font.SysFont("comicsans", 100)

meteorList = []
missileList = []

SPACESHIP_HIT = pygame.USEREVENT+1
INCREMENT_SCORE = pygame.USEREVENT+2


def getScaledSize(image):
    width = ((WIDTH/image.get_width()) * image.get_width())
    height = int((HEIGHT/image.get_height()) * image.get_height())
    return (width, height)


bg = pygame.image.load(os.path.join(
    'assets', 'background', f'bg{GAME_BACKGROUND}.jpg'))
size = getScaledSize(bg)


def drawFrame(spaceship):
    WIN.blit(pygame.transform.scale(bg, size=size), dest=(0, 0))

    spaceship.draw()

    global meteorList
    for meteor in meteorList:
        meteor.draw()

    for missile in missileList:
        missile.draw()

    spaceship_heath_text = SPACESHIP_HEALTH_FONT.render(
        "HEALTH: "+str(SPACESHIP_HEALTH), 1, pygame.Color(255, 255, 255))

    score_text = SCORE_FONT.render(
        "SCORE: "+str(SCORE), 1, pygame.Color(255, 255, 255))

    WIN.blit(spaceship_heath_text, (0, 0))
    WIN.blit(score_text, (WIDTH-score_text.get_width(), 0))

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


def checkCollisions(spaceship):
    global meteorList, missileList, SCORE

    for meteor in meteorList:
        if (meteor.y > HEIGHT):
            meteorList.remove(meteor)
            meteorList.append(game_objects.Meteor(random.randrange(
                0, 950), random.randrange(-700, -100), WIN=WIN))

        if (spaceship.spaceshipRect.colliderect(meteor.meteorRect)):
            pygame.event.post(pygame.event.Event(SPACESHIP_HIT))
            meteorList.remove(meteor)
            meteorList.append(game_objects.Meteor(random.randrange(
                0, 950), random.randrange(-700, -100), WIN=WIN))

    for missile in missileList:
        if (missile.y < 0-missile.getHeight()):
            missileList.remove(missile)

    try:
        for missile in missileList:
            for meteor in meteorList:
                if (meteor.meteorRect.colliderect(missile.missileRect)):
                    meteorList.remove(meteor)
                    meteorList.append(game_objects.Meteor(random.randrange(
                        0, 950), random.randrange(-700, -100), WIN=WIN))
                    missileList.remove(missile)
                    SCORE += METEOR_HIT_INCREMENT_FACTOR
    except Exception as e:
        print(e)


def main(name, spaceship_no, level):
    global meteorList, SCORE, SPACESHIP_HEALTH, PAUSE, WIN, SPACESHIP_NO, NO_OF_METEORS

    WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    pygame.display.set_caption("Cosmic Defender")

    clock = pygame.time.Clock()
    pygame.time.set_timer(INCREMENT_SCORE, 1000)

    SPACESHIP_NO = spaceship_no

    if (level == 1):
        NO_OF_METEORS = 3
    elif level == 2:
        NO_OF_METEORS = 6
    else:
        NO_OF_METEORS = 9

    spaceship = game_objects.Spaceship(
        (WIDTH//2), HEIGHT, WIN, SPACESHIP_NO, SPACESHIP_VELOCITY)

    meteorList = generateMeteors(NO_OF_METEORS)

    run = True
    while (run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
                pygame.quit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                if not PAUSE:
                    PAUSE = True
                else:
                    PAUSE = False

            if (not PAUSE):
                if (event.type == INCREMENT_SCORE):
                    SCORE += 10

                if event.type == SPACESHIP_HIT:
                    SPACESHIP_HEALTH -= 10
                    if (SPACESHIP_HEALTH <= 0):
                        gameOverText = GAME_OVER_FONT.render(
                            "GAME OVER", 1, pygame.Color(255, 0, 0))
                        drawFrame(spaceship)
                        WIN.blit(gameOverText, (WIDTH//2 -
                                 gameOverText.get_width()//2, HEIGHT//2 - gameOverText.get_height()//2))
                        pygame.display.update()
                        PAUSE = True
                        DB.insert_data(name, level, SCORE)

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE and len(missileList) < 4):
                        missileList.append(
                            game_objects.Missile(spaceship.x+15, spaceship.y, WIN))
                        missileList.append(
                            game_objects.Missile(spaceship.x+spaceship.getWidth()-20, spaceship.y, WIN))

        if (not PAUSE):
            keys_pressed = pygame.key.get_pressed()
            handleSpaceShipMovement(spaceship, keys_pressed)

            checkCollisions(spaceship=spaceship)

            drawFrame(spaceship)


if __name__ == "__main__":
    main("admin", 2, 3)
