from pygame import*

okno = display.set_mode((600,400))
bkgd = transform.scale(image.load('подводный мир.jpg'),(800,600))
gm = True
FPS = 80
clock = time.Clock()   
mixer.init()
mixer.music.load('phonky.mp3' )
mixer.music.play()

class sprit(sprite.Sprite):
    def __init__(self, imag, x, y):
        super().__init__()
        self.image = transform.scale(image.load(imag),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xvel = 0
    def self (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))

class wall(sprite.Sprite):
    def __init__(self,  x, y, speed):
        super().__init__()
        self.image = Surface((60,10))
        self.image.fill((0,50,200))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def selff (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def update(self):
        if self.rect.y < 200:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(10,200)
  
ochki = 0
health = 10
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 80)
h1 = sprit("ball.png",100,100)
#los = font.render('you lose', True, (200,200,0))

level = [
"-------------------------",
"-                       -",
"-                       -",
"-                       -",
"-            --         -",
"-                       -",
"--                      -",
"-                       -",
"-                   --- -",
"-                       -",
"-                       -",
"-      ---              -",
"-                       -",
"-   -----------        -",
"-                       -",
"-                -      -",
"-                   --  -",
"-                       -",
"-                       -",
"-------------------------"]

x = 100
y = 20

while gm:
    okno.blit(bkgd,(0,0))
    for i in event.get():
        if i.type == QUIT:
            gm = False
    #txt = 'очки '+ str(ochki)
    #txt2 = 'здоровье' + str(health)
    h1.self()
    keys_pressed = key.get_pressed()
    if keys_pressed[K_d]:
        x += 5
    if keys_pressed[K_w]:
        y -=5
    if keys_pressed[K_s]:
        y +=5

    #text = font1.render(txt,1,(230,40,230))
    #text2 = font2.render(txt2,2,(40,115,235))
    #okno.blit(text,(5,200))
    #okno.blit(text2,(10,300))
    #if health <= 1:
        #print(los)
        #gm = False
    display.update()
    clock.tick(FPS)
