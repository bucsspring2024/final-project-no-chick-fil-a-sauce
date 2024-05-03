import pygame
import os
class Chicken:
    x_pos=80
    y_pos=310
    y_pos_duck=350
    jump_velocity=10
    def __init__(self):
        running= [pygame.image.load(os.path.join("assets/pictures/chicken", "run1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run3.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run3.png"))]
        jumping= [pygame.image.load(os.path.join("assets/pictures/chicken", "jump1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump3.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump3.png"))]
        ducking= [pygame.image.load(os.path.join("assets/pictures/chicken", "duck1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "duck1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "duck2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "duck2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "duck3.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "duck3.png"))]
        death=pygame.image.load(os.path.join("assets/pictures/chicken", "death.png"))
        self.run_img= running
        self.jump_img= jumping
        self.duck_img= ducking
        self.death_img=death
        
        self.frame_counter=0
        
        self.chicken_run=True
        self.chicken_jump= False
        self.chicken_duck=False
        
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
        if self.chicken_duck:
            self.duck()
        if self.step_index>=10:
            self.step_index=0
        if keys[pygame.K_UP] and not self.chicken_jump:
            self.chicken_run=False
            self.chicken_jump=True
            self.chicken_duck=False
        elif keys[pygame.K_DOWN] and not self.chicken_jump:
            self.chicken_run=False
            self.chicken_duck=True
            self.chicken_jump=False
        elif not (self.chicken_jump or keys[pygame.K_DOWN]):
            self.chicken_run=True 
            self.chicken_jump=False
            self.chicken_duck=False
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
        self.img = self.jump_img[self.step_index]
        if self.frame_counter % 20 == 0:
            self.step_index = (self.step_index + 1) % len(self.jump_img)
        if self.chicken_jump:
            self.chicken_rect.y-=self.jump_vel*4
            self.jump_vel-=0.8
        if self.jump_vel<-self.jump_velocity:
            self.chicken_jump=False
            self.jump_vel=self.jump_velocity 
    def duck(self):
        self.img=self.duck_img[self.step_index%6]
        new_height= 115
        self.chicken_rect=self.img.get_rect()
        self.chicken_rect.x=self.x_pos
        self.chicken_rect.y=self.y_pos_duck
        self.img= pygame.transform.scale(self.img, (self.img.get_width(), new_height))
        if self.frame_counter%20==0:
            self.img=pygame.transform.scale(self.duck_img[self.step_index], (self.img.get_width(), new_height))
            self.step_index=(self.step_index+1)%len(self.duck_img)
    def draw(self, screen):
        screen.blit(self.img, (self.chicken_rect.x, self.chicken_rect.y))

                
                        