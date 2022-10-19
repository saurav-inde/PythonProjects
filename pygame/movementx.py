import pygame
import os

cwd = os.getcwd()


def main():
    pygame.init()

    icon = pygame.image.load("logo.bmp")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Movement")

    width, height = 500, 500
    screen = pygame.display.set_mode(size=(width, height))
    screen.fill(color=(0, 0, 220))

    ship = pygame.image.load("01_image.png")
    ship.set_colorkey((255, 0, 255))
    shipx, shipy = 50, 50
    ship_speed_x, ship_speed_y = 10, 13
    screen.blit(ship, dest=(shipx, shipy))

    pygame.display.update()

    clock = pygame.time.Clock()

    running = True

    while running:
        clock.tick(144)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                
                running = False
            # speed controls
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                ship_speed_y += 1 if ship_speed_x > 0 else -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                ship_speed_y -= 1 if ship_speed_x > 0 else -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                ship_speed_x += 1 if ship_speed_y > 0 else -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                ship_speed_y -= 1 if ship_speed_y > 0 else -1

        if shipx + 64 > width or shipx < 0:
            ship_speed_x = -1 * ship_speed_x
        if shipy + 64 > height or shipy < 0:
            ship_speed_y = -1 * ship_speed_y

        screen.fill(color=(0, 0, 220))

        shipx += ship_speed_x
        shipy += ship_speed_y
        screen.blit(ship, dest=(shipx, shipy))
        print(shipx, shipy, ship_speed_x, ship_speed_y, end="\n")

        pygame.display.update()


if __name__ == "__main__":
    main()
