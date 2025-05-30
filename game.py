import pygame as pg
import sys,time
from dino import Dino
from bird import Bird
from tree import Tree
import random
pg.init()

class Game:
    def __init__(self):
        self.width=600
        self.height=300
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()

        self.ground1=pg.image.load("assets/ground.png").convert_alpha()
        self.ground1_rect=self.ground1.get_rect(center=(300,250))

        self.ground2=pg.image.load("assets/ground.png").convert_alpha()
        self.ground2_rect=self.ground2.get_rect()
        self.ground2_rect=self.ground2.get_rect(center=(900,250))

        self.font=pg.font.Font("assets/font.ttf",20)
        self.label_score=self.font.render("Score: 0",True,(0,0,0))
        self.label_score_rect=self.label_score.get_rect(center=(500,20))

        self.label_restart=self.font.render("Restart Game",True,(0,0,0))
        self.label_restart_rect=self.label_restart.get_rect(center=(300,150))

        self.dino=Dino()
        self.game_lost=False
        self.move_speed=250
        self.enemy_spawn_counter=0
        self.enemy_spawn_time=80
        self.score=0
        self.enemy_group=pg.sprite.Group()

        self.gameLoop()
    
    def checkCollisions(self):
        if pg.sprite.spritecollide(self.dino,self.enemy_group,False,pg.sprite.collide_mask):
            self.stopGame()
    
    def stopGame(self):
        self.game_lost=True

    def restart(self):
        self.game_lost=False
        self.score=0
        self.enemy_spawn_counter=0
        self.move_speed=250
        self.label_score=self.font.render("Score: 0",True,(0,0,0))
        self.dino.resetDino()

        for enemy in self.enemy_group:
            enemy.deleteMyself()

    def gameLoop(self):
        last_time=time.time()
        while True:
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time

            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
                    if not self.game_lost:
                        self.dino.jumpDino(dt)
                    else:
                        self.restart()

            
            self.win.fill((255,255,255))
            if not self.game_lost:
                self.ground1_rect.x-=int(self.move_speed*dt)
                self.ground2_rect.x-=int(self.move_speed*dt)

                if self.ground1_rect.right<0:
                    self.ground1_rect.x=600
                if self.ground2_rect.right<0:
                    self.ground2_rect.x=600

                self.score+=0.1
                self.label_score=self.font.render(f"Score: {int(self.score)}",True,(0,0,0))
                self.dino.update(dt)
                self.enemy_group.update(dt)

                if self.enemy_spawn_counter==self.enemy_spawn_time:
                    if random.randint(0,1)==0: self.enemy_group.add(Bird(self.enemy_group,self.move_speed))
                    else: self.enemy_group.add(Tree(self.enemy_group,self.move_speed))
                    self.enemy_spawn_counter=0
                self.enemy_spawn_counter+=1

                if int(self.score)%30==0:
                    self.move_speed+=5
                    for enemy in self.enemy_group:
                        enemy.setMoveSpeed(self.move_speed)

                self.win.blit(self.dino.image,self.dino.rect)
                for enemy in self.enemy_group:
                    self.win.blit(enemy.image,enemy.rect)
                
                self.checkCollisions()
            else:
                self.win.blit(self.label_restart,self.label_restart_rect)
            
            self.win.blit(self.ground1,self.ground1_rect)
            self.win.blit(self.ground2,self.ground2_rect)
            self.win.blit(self.label_score,self.label_score_rect)
            pg.display.update()
            self.clock.tick(60)




game=Game()
