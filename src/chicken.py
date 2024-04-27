import pygame
import os
class Chicken:
    x_pos=80
    y_pos=310
    jump_velocity=8.5
    def __init__(self):
        running= [pygame.image.load(os.path.join("assets/pictures/chicken", "run1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run3.png"))]
        jumping= [pygame.image.load(os.path.join("assets/pictures/chicken", "jump3.png"))]
        death= [pygame.image.load(os.path.join("assets/pictures/chicken", "death.png"))]
        self.run_img= running
        self.jump_img= jumping
        self.death_img=death
        
        self.frame_counter=0
        
        self.chicken_run=True
        self.chicken_jump= False
        
        self.step_index=0
        self.jump_vel=self.jump_velocity
        self.img= self.run_img[0]
        self.chicken_rect=self.img.get_rect()
        self.chicken_rect.x=self.x_pos
        self.chicken_rect.y=self.y_pos
        self.width=self.img.get_width()
        self.height=self.img.get_height()
        self.chicken_rect=pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)  
    def update(self, keys):
        if self.chicken_run:
            self.run()
        if self.chicken_jump:
            self.jump()
        if self.step_index>=10:
            self.step_index=0
        if keys[pygame.K_UP] and not self.chicken_jump:
            self.chicken_run=False
            self.chicken_jump=True
        elif not (self.chicken_jump or keys[pygame.K_DOWN]):
            self.chicken_run=True 
            self.chicken_jump=False
    def run(self):
        self.img=self.run_img[self.step_index]
        self.chicken_rect=self.img.get_rect()
        self.chicken_rect.x=self.x_pos
        self.chicken_rect.y= self.y_pos
        self.step_index=(self.step_index)
        self.img = self.run_img[self.step_index]
    
        if self.frame_counter%20==0:
            self.img=self.run_img[self.step_index]
            self.step_index=(self.step_index+1)%len(self.run_img)
    def jump(self):
        self.img= self.jump_img[0] 
        if self.chicken_jump:
            self.chicken_rect.y-=self.jump_vel*4
            self.jump_vel-=0.8
        if self.jump_vel<-self.jump_velocity:
            self.chicken_jump=False
            self.jump_vel=self.jump_velocity 
        if self.frame_counter%100==0:
            self.img=self.jump_img[0]
            self.step_index=(self.step_index+3)%len(self.run_img) 
    def draw(self, screen):
        screen.blit(self.img, (self.chicken_rect.x, self.chicken_rect.y))

                
                        