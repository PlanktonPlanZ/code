from random import randint
from pygame import *
font.init()
win_width = 1000
win_height = 750
window = display.set_mode((win_width, win_height))
display.set_caption("Maze") 

background = transform.scale(image.load("kosmos.png"), (win_width, win_height))
fail = 0

mixer.init()
mixer.music.load('sooong.ogg')
mixer.music.play(-1)

class GameSprite(sprite.Sprite):
    def __init__(self, player, c_x, c_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = c_x
        self.rect.y = c_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_Movement(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 850:
            self.rect.x += self.speed
    def fire(self):
        keys = key.get_pressed()
        if keys[K_s]:
            Sprite_top =  self.rect.top
            Sprite_center_x1 = self.rect.centerx - self.rect.width / 5 * 1.5
            Sprite_center_x2 = self.rect.centerx + self.rect.width / 5 * 1.5
            bullet_hell1.add(Bullet('laser.png', Sprite_center_x1, Sprite_top, 20, 5, 20))
            bullet_hell1.add(Bullet('laser.png', Sprite_center_x2, Sprite_top, 20, 5, 20))
class Enemy(GameSprite):
    def update(self):
      self.rect.y += self.speed
      global fail
      if self.rect.y > win_height:
          self.rect.y = 0
          self.rect.x = randint(0, 900)
          fail += 1

class Bullet(GameSprite):
    def update(self):
            self.rect.y -= self.speed

class Meter():
    def __init__(self, text, x, y):
        self.font1 = font.Font(None, 36)
        self. text = self.font1.render(text, True, (255, 255, 255))
        self.x = x
        self.y = y
    def set_text(self, text):
        self. text = self.font1.render(text, True, (255, 255, 255))
    def draw(self):
        window.blit(self.text, (self.x, self.y))

Label = Meter('Счет:', 25, 25)

XWing = Player_Movement('X-Wing.png', 400, 550, 50, 200, 100)
empire = sprite.Group()
Laser = Bullet('laser.png', 475, 560, 40, 10, 50 )
run = True
bullet_hell1 = sprite.Group()
while run:
    for ev in event.get():
        if ev.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    if len(empire) < 5:
        X = randint(0, 900)
        empire.add(Enemy('TIE.png', X, 5, 40, 100, 100))
    empire.update()
    empire.draw(window)
    bullet_hell1.update()
    bullet_hell1.draw(window)
    XWing.update()
    XWing.fire()
    XWing.reset()
    display.update()
    time.delay(50)