from pygame import *
from random import randint
vis = [randint(-20,40)for i in range(100)]
print(vis)
#создай окно игры
okno = display.set_mode((960,400))
bkgd = transform.scale(image.load('fon.png'), (960,400))
gm = True
clock = time.Clock()
FPS = 60
x1 = 150
y1 = 150

class char(sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image =  transform.scale(image.load('sprite1.png'), (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff(self):
        okno.blit(self.image,(self.rect.x, self.rect.y))




class wall(sprite.Sprite):
    def __init__(self,wall_x,wall_y):
        super().__init__()
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.image = Surface((50,60))
        self.rect =  self.image.get_rect()
        self.rect.x = self.wall_x
        self.image.fill((5,7,8))
        self.rect.y = self.wall_y
    def draw(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        press = key.get_pressed()
        if press [K_a]:
            self.rect.x +=5
        if press [K_w]:
            self.rect.y -=5
pol= sprite.Group()   
for i in range(100):
    w = wall(i*50, vis[i]+350)
    pol.add(w)



h1=char(100,100)

while gm:
    okno.blit(bkgd,(0,0))
    for i in event.get():
        if i.type == QUIT:
            gm = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_d]:
        x1 += 5
    if keys_pressed[K_w]:
        y1 -=5
    if keys_pressed[K_s]:
        y1 +=5
    for i in pol:
        i.draw()
        i.move()
    if sprite.spritecollideany(h1,pol):
        h1.rect.y -=1
    else:
        h1.rect.y +=1
    h1.selff()
    display.update()
    clock.tick(FPS)

