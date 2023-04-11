import pygame
import os
import random


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
        self.spaceshipRect.x = self.x
        self.spaceshipRect.y = self.y

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
        self.meteorRect.y = self.y

    def getWidth(self):
        return self.SCALED_METEOR_IMAGE_WIDTH

    def getHeight(self):
        return self.SCALED_METEOR_IMAGE_HEIGHT


class Missile():
    VELOCITY = 15
    MISSILE_IMAGE = pygame.image.load(
        os.path.join('assets', 'missiles', 'Missile_01.png'))

    SCALED_MISSILE_IMAGE_WIDTH = MISSILE_IMAGE.get_width() * 0.08
    SCALED_MISSILE_IMAGE_HEIGHT = MISSILE_IMAGE.get_height() * 0.08

    MISSILE = pygame.transform.scale(MISSILE_IMAGE, size=(
        SCALED_MISSILE_IMAGE_WIDTH, SCALED_MISSILE_IMAGE_HEIGHT))

    def __init__(self, x, y, WIN) -> None:
        self.x = x
        self.y = y
        self.WIN = WIN
        self.missileRect = pygame.Rect(
            self.x, self.y, int(self.SCALED_MISSILE_IMAGE_WIDTH), int(self.SCALED_MISSILE_IMAGE_HEIGHT))

    def draw(self):
        self.WIN.blit(self.MISSILE, dest=(self.x, self.y))
        self.update()

    def update(self):
        self.y -= self.VELOCITY
        self.missileRect.y = self.y

    def getHeight(self):
        return self.SCALED_MISSILE_IMAGE_HEIGHT

    def getWidth(self):
        return self.SCALED_MISSILE_IMAGE_WIDTH
