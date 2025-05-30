import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self,enemy_group,move_speed):
        super(Bird,self).__init__()
        self.img_list=[pg.image.load("assets/bird1.png").convert_alpha(),
                        pg.image.load("assets/bird2.png").convert_alpha()]
        self.image=self.img_list[0]
        self.mask=pg.mask.from_surface(self.image)
        self.rect=pg.Rect(600,180,42,31)
        self.anim_counter=0
        self.speed=move_speed
        self.enemy_group=enemy_group
        self.image_switch=1
    
    def update(self,dt):
        if self.anim_counter==8:
            self.image=self.img_list[self.image_switch]
            if self.image_switch==0: self.image_switch=1
            else: self.image_switch=0
            self.anim_counter=0
        self.anim_counter+=1
        
        self.rect.x-=self.speed*dt

        if self.rect.right<0:
            self.deleteMyself()
    
    def setMoveSpeed(self,move_speed):
        self.speed=move_speed
    
    def deleteMyself(self):
        self.kill()
        del self
