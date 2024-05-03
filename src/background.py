import pygame
import os
class Background:
    background= pygame.image.load(os.path.join("assets/pictures/extras", "background.jpg"))
    resized_bg=(1150,500)
    background= pygame.transform.scale(background, resized_bg)
    x_pos_bg=0
    x_pos_bg2=background.get_width()
    y_pos_bg=0
    @classmethod
    def draw(cls, screen):
        width= cls.background.get_width()
        screen.blit(cls.background, (cls.x_pos_bg, cls.y_pos_bg))
        screen.blit(cls.background, (cls.x_pos_bg2, cls.y_pos_bg))
        if cls.x_pos_bg<= -cls.background.get_width():
            cls.x_pos_bg=cls.x_pos_bg2 + cls.background.get_width()
        if cls.x_pos_bg2 <= -cls.background.get_width():
            cls.x_pos_bg2 = cls.x_pos_bg + cls.background.get_width()
        cls.x_pos_bg-=10
        cls.x_pos_bg2-=10
