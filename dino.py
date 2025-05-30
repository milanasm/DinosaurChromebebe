import pygame as pg

class Dino(pg.sprite.Sprite):
    def __init__(self):
        super(Dino,self).__init__()
        self.dino_run_list=[pg.image.load("assets/dino1.png").convert_alpha(),
                            pg.image.load("assets/dino2.png").convert_alpha()]
        self.dino_crouch_list=[pg.image.load("assets/dino_crouch1.png").convert_alpha(),
                            pg.image.load("assets/dino_crouch2.png").convert_alpha()]

        self.image=self.dino_run_list[0]
        self.mask=pg.mask.from_surface(self.image)
        self.resetDino()
        self.gravity=10
        self.jump_speed=250

    
    def update(self,dt):
        keys=pg.key.get_pressed()
        if keys[pg.K_DOWN]: self.crouch=True
        else: self.crouch=False

        if self.is_on_ground:
            if self.anim_counter==5:

                if self.crouch: 
                    self.image=self.dino_crouch_list[self.image_switch]
                    self.rect=pg.Rect(200,220,55,30)
                else: 
                    self.image=self.dino_run_list[self.image_switch]
                    self.rect=pg.Rect(200,200,43,51)
                self.mask=pg.mask.from_surface(self.image)
                
                if self.image_switch==0: self.image_switch=1
                else: self.image_switch=0

                self.anim_counter=0
            self.anim_counter+=1
        else:
            self.velocity_y+=self.gravity*dt
            self.rect.y+=self.velocity_y
            if self.rect.y>=200:
                self.is_on_ground=True
                self.rect.y=200

    def jumpDino(self,dt):
        if self.is_on_ground:
            self.velocity_y=-self.jump_speed*dt
            self.is_on_ground=False

    
    def resetDino(self):
        self.rect=pg.Rect(200,200,43,51)
        self.image_switch=1
        self.anim_counter=0
        self.crouch=False
        self.is_on_ground=True
        self.velocity_y=0
