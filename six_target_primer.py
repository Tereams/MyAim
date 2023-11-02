import random

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((960, 680))
pygame.display.set_caption('Six_Target')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surf = pygame.image.load('imgs/shoot_bk1.png').convert()
target_surf = pygame.image.load('imgs/target2.png').convert_alpha()

rects = []
for _ in range(6):
    x = random.randint(50, 850)
    y = random.randint(50, 630)
    target_rect = target_surf.get_rect(topleft=(x, y))
    rects.append(target_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for rec in rects:
                if rec.collidepoint(mouse_pos):
                    x = random.randint(50, 850)
                    y = random.randint(50, 630)
                    rec.x, rec.y = x, y

    screen.blit(sky_surf, (0, 0))
    for rec in rects:
        screen.blit(target_surf,rec)

    pygame.display.update()
    clock.tick(60)
