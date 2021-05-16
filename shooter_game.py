#Создай собственный Шутер!

from pygame import *
okno = display.set_mode((800,600))
bkgd = transform.scale(image.load('galaxy.jpg'),(800,600))
gm = True
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
class sprit(sprite.Sprite):
    def __init__(self, imimage, x, y, sspeed):
        super().__init__()
        self.image = transform.scale(image.load(imimage),(110,130))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self): 
        okno.blit(self.image,(self.rect.x, self.rect.y))

from random import*
class Enemy(sprit):
    def __init__(self, imimage, x, y, sspeed):
        self.image = transform.scale(image.load(imimage),(130,100))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(0,500)

class bullet(sprit):
    def __init__(self, imimage, x, y, sspeed):
        self.image = transform.scale(image.load(imimage),(30,70))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def fire(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.rect.y = -100
b=bullet('bullet.png',-200,-200,10)

class igrok(sprit):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x >0:
            self.rect.x -=5
        if keys_pressed[K_d] and self.rect.x < 620-5:
            self.rect.x +=5
        if keys_pressed[K_SPACE]:
            b.rect.x = self.rect.x+40
            b.rect.y = self.rect.y-20

        
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 80)
hero = igrok('rocket.png', 150,470,5)
monsters = Enemy('ufo.png', 100,50, 3)
ochki = 0
health = 10

while gm:
    okno.blit(bkgd,(0,0))
    for i in event.get():
        if i.type == QUIT:
            gm = False
    txt = 'очки '+ str(ochki)
    text = font1.render(txt,1,(250,0,0))
    okno.blit(text,(10,30))
    hero.selff()
    hero.update()
    monsters.selff()
    monsters.update()
    b.selff()
    b.fire()
    if sprite.collide_rect(monsters, b):
        monsters.rect.y = -10
        monsters.rect.x = randint(0,500)
        b.rect.y = -100
        ochki += 1
    if ochki >10:
        gm =  False
    helths = 'здоровье ' + str(health)
    hearts = font2.render(helths,2,(250,0,0))
    okno.blit(hearts,(450,30))
    if sprite.collide_rect(monsters, hero):
        monsters.rect.y = -10
        monsters.rect.x = randint(0,500)
        helth -= 1
    if helth < 1:
        gm =  False
    b.update()
    display.update()

