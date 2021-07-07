import pygame
import button

pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
w,h=screen.get_size()
pygame.display.set_caption("Space Trouble")

start_img = pygame.image.load('start.png').convert_alpha()
exit_img = pygame.image.load('quit.png').convert_alpha()
score_img = pygame.image.load('scores.png').convert_alpha()


start_button = button.Button(w/2-200, h/2+100, start_img, 0.2)
exit_button = button.Button(w/2+200, h/2+100, exit_img, 0.2)
score_button = button.Button(w/2-600, h/2+100, score_img, 0.2)

font = pygame.font.SysFont('cambria', 110)
heading = pygame.image.load("heading.png")
run = True
while run:

    bg = pygame.image.load("background2.png")
    bg= pygame.transform.scale(bg, (w,h))
    screen.blit(bg, bg.get_rect())
    screen.blit(heading, (w/2-500, h/2-200))

    if start_button.draw():
        import game
        continue

    if exit_button.draw():
        run = False

    if score_button.draw():
        import mysq2
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
pygame.quit()
