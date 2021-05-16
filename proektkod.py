from pygame import*

okno = display.set_mode((600,400))
app = transform.scale(image.load('подводный мир.jpg'),(600,400))
from random import*

gm = True
FPS = 80
clock = time.Clock()
vis = [randint(-20,40)for i in range(100)]

mixer.init()
mixer.music.load('proektmusic.mp3' )
mixer.music.play()

class sprit(sprite.Sprite):
    def __init__(self, imag, x, y):
        super().__init__()
        self.image = transform.scale(image.load(imag),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def self (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
   # def control():
        #keys_pressed = key.get_pressed()
       # if keys_pressed[K_d]:
        #x += 5
        #if keys_pressed[K_w]:
        #y -=5
       # if keys_pressed[K_a]:
        #x -=5


class wall(sprite.Sprite):
    def __init__(self,  x, y):
        super().__init__()
        self.image = Surface((20,5))
        self.image.fill((0,100,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def update(self):
        if self.rect.y < 400:
            self.rect.y += 2
        else:
            self.rect.y = 0
            self.rect.x = randint(60,700)
pol= sprite.Group()   
for i in range(100):
    w = wall(i*50, vis[i]+350)
    pol.add(w)
ochki = 0
health = 10
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 80)
h1 = sprit("ball.png",100,100)

while gm:
    okno.blit(app,(0,0))
    for i in event.get():
        if i.type == QUIT:
            gm = False
    txt = 'очки '+ str(ochki)
    for i in pol:
        i.selff()
        i.update()
    if sprite.spritecollideany(h1,pol):
        h1.rect.y -=1
    else:
        h1.rect.y +=1
    h1.self()
    text = font1.render(txt,1,(250,0,0))
    okno.blit(text,(10,30))
    h1.update()
    w.selff()
    w.update()
    display.update()
    clock.tick(FPS)


