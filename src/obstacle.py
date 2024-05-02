import pygame
import os 
import random
screen_height= 500
screen_width=1100
image=[
    pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/obstacles", "cone.png")), (100,100)),
    pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/obstacles", "plane.png")), (150, 100))
    ]
screen=pygame.display.set_mode((screen_width, screen_height))
from src.constants import obstacles


class Obstacle:
    def __init__(self, image, type):
        image=[
            pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/obstacles", "cone.png")), (100,100)),
            pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/obstacles", "plane.png")), (150, 100))
            ]
        self.type=type
        self.image=image[type] 
        self.rect=self.image.get_rect()
        self.rect.x=1100

    def update(self):
        self.rect.x-=14
        if self.rect.x<-self.rect.width:
            if obstacles:
                obstacles.pop()
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
class Cone(Obstacle):
    def __init__(self,image):
        self.type=0
        image=pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/obstacles", "cone.png")), ((95),95))
        super().__init__(image, self.type)
        self.rect.y=375
    def draw(self,screen):
        screen.blit(self.image, self.rect)

class Plane(Obstacle):
    def __init__(self,image):
        self.type=1
        image=pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/obstacles", "plane.png")), (150, 100))
        super().__init__(image, self.type)
        self.rect.y=215
    def draw(self,screen):
        screen.blit(self.image, self.rect)