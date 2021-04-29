import os
import time
import random
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame import mixer

pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projekt E.G.G")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        vel_x = 0
        vel_y = 0
        if keys[pygame.K_a]: # left
            print(vel_x - 5)
        if keys[pygame.K_d]: # right
            print(vel_x + 5)
        if keys[pygame.K_w]: # up
            print(vel_y + 5)
        if keys[pygame.K_s]: # down
            print(vel_y - 5)
        if keys[pygame.K_ESCAPE]:
            run = False

def main_menu():
    run = True
    while run:
        WIN.blit(BG, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()