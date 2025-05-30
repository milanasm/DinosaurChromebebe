import pygame as pg
import random

class Tree(pg.sprite.Sprite):
    def __init__(self,enemy_group,move_speed):
        super(Tree,self).__init__()
        self.img_list=[]
        for i in range(1,6):
            self.img_list.append(pg.image.load(f"assets/trees/tree{i}.png").convert_alpha())
        self.image=self.img_list[random.randint(0,4)]
        self.mask=pg.mask.from_surface(self.image)
        self.rect=pg.Rect(600,208,50,50)
        self.speed=move_speed
        self.enemy_group=enemy_group
    
    def update(self,dt):
        self.rect.x-=self.speed*dt

        if self.rect.right<0:
            self.deleteMyself()
    
    def setMoveSpeed(self,move_speed):
        self.speed=move_speed
    
    def deleteMyself(self):
        self.kill()
        del self
           