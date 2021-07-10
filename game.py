import sys, pygame, random, os
import time

# initialize the pygame
pygame.init()

size = width, height = 500, 500

screen = pygame.display.set_mode(size)
speed = [0, 0]
# need an image for the game

# Title and Icon
pygame.display.set_caption("Avoid red beads!")

# Character
    # Icon url: https://www.flaticon.com/free-icon/profile_4372360?related_id=4372293&origin=search#

class MainCharacter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # image
        # rect
        self.image = pygame.image.load(os.path.join(base_path, "profile.png"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
        self.defaultScore = 5
    def redupdate(self):
        self.defaultScore -= 1
        if (self.defaultScore <= 0):
            sys.exit()
    def greenupdate(self):
        self.defaultScore += 1

class Redbead(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # image
        # rect
        self.image = pygame.image.load(os.path.join(base_path, "ball.png"))
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.badSpeed = [3, 3]
        self.rect.center = (random.randint(0, 500), random.randint(0, 500))
    def update(self):
        self.rect = self.rect.move(self.badSpeed)
        if self.rect.left < 0 or self.rect.right > width:
            self.badSpeed[0] = -self.badSpeed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.badSpeed[1] = -self.badSpeed[1]

class Greenbead(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # image
        # rect
        self.image = pygame.image.load(os.path.join(base_path, "green.png"))
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.goodSpeed = [3, 3]
        self.rect.center = (random.randint(0, 500), random.randint(0, 500))
    def update(self):
        self.rect = self.rect.move(self.goodSpeed)
        if self.rect.left < 0 or self.rect.right > width:
            self.goodSpeed[0] = -self.goodSpeed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.goodSpeed[1] = -self.goodSpeed[1]


main = MainCharacter()

main_sprite = pygame.sprite.Group()
main_sprite.add(main)

badSprites = pygame.sprite.Group()
goodSprites = pygame.sprite.Group()
for i in range(0, 4):
    badSprites.add(Redbead())

for i in range(0, 2):
    goodSprites.add(Greenbead())
    
clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    screen.fill(0, 0, 0)
    badSprites.draw(screen)
    goodSprites.draw(screen)
    main_sprite.draw(screen)

    key = pygame.key.get_pressed()

    if (key[pygame.K_a]):
        if (speed[0] > -10):
            speed[0] -= 1.5
    if (key[pygame.K_w]):
        if (speed[1] > -10):
            speed[1] -= 1.5
    if (key[pygame.K_s]):
        if (speed[1] < 10):
            speed[1] += 1.5
    if (key[pygame.K_d]):
        if (speed[0] > 10):
            speed[0] += 1.5

    if main.rect.left < 0 or main.rect.right > width:
        speed[0] = -speed[0]
    if main.rect.top < 0 or main.rect.bottom > height:
        speed[1] = -speed[1]

    main.rect = main.rect.move(speed)
    badSprites.update()
    goodSprites.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    pygame.display.update()
