import pygame 
import os
import random
game_speed=14
screen_height= 500
screen_width=1100
class Cloud:
    def __init__(self):
        cloud=pygame.image.load(os.path.join("assets/pictures/extras", "cloud.png"))
        default_size=(150,100)
        cloud= pygame.transform.scale(cloud, default_size)
        self.x=screen_width+random.randint(800,1000)
        self.y=random.randint(50,150)
        self.image= cloud
        self.width=self.image.get_width()
        
    def update(self):
        self.x-= game_speed
        if self.x<-self.width:
            self.x=screen_width+random.randint(2500,3000)
            self.y=random.randint(50,100)
            
    def draw(self, screen):
        screen.blit(self.image, (self.x,self.y))