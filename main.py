import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Игра')
clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load('img/bg.png').convert_alpha()
castle_img_100 = pygame.image.load('img/castle/castle_100.png').convert_alpha()


class Castle():
    def __init__(self, image100, x, y, scale):
        self.health = 1000
        self.max_health = self.health

        width = image100.get_width()
        height = image100.get_height()

        self.image100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.rect = self.image100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.image = self.image100

        screen.blit(self.image, self.rect)


castle = Castle(castle_img_100, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.2)

run = True
while run:

    clock.tick(FPS)

    screen.blit(bg, (0, 0))
    castle.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
