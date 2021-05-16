from pygame import*

okno = display.set_mode((600,400))
fon = transform.scale(image.load('exture.jpg'),(600,400))
gm = True
clock = time.Clock()
FPS = 60

class sprit(sprite.Sprite):
    def __init__(self, imimage, x, y, sspeed):
        super().__init__()
        self.image = transform.scale(image.load(imimage),(65,65))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))

class mach(sprit):
    def __init__(self, imimage,  x, y, sspeed):
        keys_pressed = key.get_pressed()
        self.image = transform.scale(image.load(imimage),(65,65))
        self.speed = sspeed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))


class wall(sprit):
    def __init__(self,wall_x,wall_y,wall_w,wall_h,):
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.wall_h = wall_h
        self.wall_w = wall_w

        self.image = Surface((self.wall_w, self.wall_h))
        self.rect = self.image.get_rect()
        self.rect.x = self.wall_x
        self.image.fill((0,100,200))
        self.rect.y = self.wall_y
    def uprav(self):
        #okno.blit(self.image,(self.rect.x,self.rect.y))
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -=5
        if keys_pressed[K_s]:
            self.rect.y +=5


clock = time.Clock()   

tennis = mach('tennis.png',60,2,0)
stena = wall(50,100,13,110)
stena2 = wall(550,100,13,110)
dx = 5
dy = 3

while gm:
    tennis.rect.x += dx
    tennis.rect.y -= dy
    if tennis.rect.x > 550:
        dx *= -1
    if tennis.rect.y < 0:
        dy *= -1
    if tennis.rect.x < 0:
        dx *= -1
    if tennis.rect.y > 350:
        dy *=-1
    if sprite.collide_rect(tennis, stena):
        dx *= -1
    if sprite.collide_rect(tennis, stena2):
        dx *= -1
    okno.blit(fon,(0,0))
    stena.uprav()
    stena.selff()
    stena2.uprav()
    stena2.selff()
    tennis.selff()
    for i in event.get():
        if i.type == QUIT:
            gm = False
    clock.tick(60)
    display.update()