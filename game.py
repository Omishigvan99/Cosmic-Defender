import pygame

WIDTH = 1000
HEIGHT = 700
WIN = pygame.display.set_mode(size=(WIDTH, HEIGHT))


def main():
    run = True
    while (run):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False

if __name__ == "__main__":
    main()
