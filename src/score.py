import pygame
import os
class Score:
    def __init__(self):
        self.score=0
        self.font=pygame.font.Font(None, 36)
    def increment_score(self):
        global game_speed, points
        self.score=self.score+1
        if self.score%100==1:
            global game_speed
            game_speed=+1
    def draw(self, screen):
        text= self.font.render(f"Score: {self.score}", True, (255,255,255))
        textRect= text.get_rect()
        textRect.center= (1000,50)
        screen.blit(text, textRect)
        
    def update(self):
        self.increment_score()