from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from pygame import *

app = QApplication([])
okno = QWidget()
okno.resize(700,400)
mixer.init()
mixer.music.load(#вставить музыку )
mixer.music.play()

class sprit(sprite.Sprite):
    def __init__(self, image, x, y, speed):
        self.image = transform.scale(image.load(image),(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def self (self):
        okno.blit(self.image,(self.rect.x, self.rect.y))
    def control():
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.x -=5
        if keys_pressed[K_s]:
            self.rect.x +=5
        if keys_pressed[K_w]:
            self.rect.y -=5
        if keys_pressed[K_s]:
            self.rect.y +=5
    def start():
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            control()



class wall(sprit):
    def __init__(self,wall_x,wall_y,wall_w,wall_h,):
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.wall_w = wall_w
        self.wall_h = wall_h

        self.image = Surface((self.wall_w, self.wall_h))
        self.rect = self.image.get_rect()
        self.rect.x = self.wall_x
        self.image.fill((0,100,200))
        self.rect.y = self.wall_y





okno.show()
app.exec()

