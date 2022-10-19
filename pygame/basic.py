import pygame
import os
cwd = os.getcwd()
# print(cwd)
# defining the main function for the program


def main():
    pygame.init()
    logo = pygame.image.load(str(cwd) + "\logo.bmp")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Ambani")
    pygame.display.set_mode(size=(500, 500))

    running = True

    while running:
        for event in pygame.event.get():
            if event == pygame.K_5:
                pygame.display.set_mode(size=(1000, 500))
            if event.type == pygame.QUIT:
                running = 0


if __name__ == "__main__":
    main()
