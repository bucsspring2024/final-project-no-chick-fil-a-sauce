import pygame
import os
class Chicken:
    x_pos=80
    y_pos=310
    jump_velocity=8
    def __init__(self):
        running= [pygame.image.load(os.path.join("assets/pictures/chicken", "run1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run3.png"))]
        jumping= [pygame.image.load(os.path.join("assets/pictures/chicken", "jump1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump3.png"))]
        death= [pygame.image.load(os.path.join("assets/pictures/chicken", "death.png"))]
        self.run_img= running 
        self.jump_img= jumping
        self.death_img=death
        self.step_index=0
        self.jump_vel=self.jump_velocity
        self.img= self.run_img[0]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.x_pos
        self.dino_rect.y=self.y_pos
        def update