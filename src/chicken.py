import pygame
import os
class Chicken:
    x_pos=80
    y_pos=310
    def __init__(self):
        running= [pygame.image.load(os.path.join("assets/pictures/chicken", "run1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "run3.png"))]
        jumping= [pygame.image.load(os.path.join("assets/pictures/chicken", "jump1.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump2.png")), pygame.image.load(os.path.join("assets/pictures/chicken", "jump3.png"))]
        death= [pygame.image.load(os.path.join("assets/pictures/chicken", "death.png"))]
        self.run_img= running 