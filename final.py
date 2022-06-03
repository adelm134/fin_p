import amodule
import button
import pygame, sys

pygame.init()

background_colour = (170, 170, 223)
white = (255, 255, 255)

font = pygame.font.Font('app/font.ttf', 10)

img = pygame.image.load('app/alatoo.png')
image = pygame.transform.scale(img, (260, 250))
icon = pygame.image.load('app/alatoo.png')

pygame.display.set_icon(icon)

start_img = pygame.image.load('app/start_btn.png').convert_alpha()
exit_img = pygame.image.load('app/exit_btn.png').convert_alpha()
options_img1 = pygame.image.load('app/options.png').convert_alpha()
options_img = pygame.transform.scale(options_img1, (50, 50))
return_img1 = pygame.image.load('app/return.png').convert_alpha()
return_img = pygame.transform.scale(return_img1, (150, 150))

start_button = button.Button(100, 320, start_img, 0.15)
exit_button = button.Button(320, 320, exit_img, 0.15)
options_button = button.Button(390, 50, options_img, 1)

pygame.display.set_caption('Batch Image App')
screen = pygame.display.set_mode((480, 480))

def face():
    running = True
    while True:
        screen.fill(background_colour)
        screen.blit(image, (95, 35))
        pygame.display.set_caption('Batch Image App')
        if start_button.draw(screen):
            amodule.batch()
        if options_button.draw(screen):
            about()
        if exit_button.draw(screen):
            running = False
            pygame.quit()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

        pygame.display.update()
        pygame.display.flip()

def caption(text, x, y):
    x = x
    y = y
    mes = font.render(text, True, white)
    textRect = mes.get_rect()
    textRect.center = (x // 2, y // 2)
    screen.blit(mes, textRect)
    pygame.display.update()


def about():
    screen.fill(background_colour)
    while True:
        pygame.display.set_caption('About')
        return_button = button.Button(30, 30, return_img, 0.3)
        caption('ABOUT', 500, 180)
        caption('IT APPLIES B/W FILTER AND CROPS TO', 390, 250)
        caption('1080x1080 SIZE ALL IMAGES IN FOLDER.', 520, 290)
        caption('ADDS A WATERMARK TO ALL IMAGES', 390, 420)
        caption('AT RIGHT BOTTOM CORNER.', 620, 460)
        caption('Credits: @almostvornehm.', 300, 600)

        if return_button.draw(screen):
            face()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        pygame.display.flip()
    

running = True
while running:
    screen.fill(background_colour)
    screen.blit(image, (95, 35))

    if start_button.draw(screen):
        amodule.Openfolder()
    if options_button.draw(screen):
        about()
    if exit_button.draw(screen):
        running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()

pygame.quit()