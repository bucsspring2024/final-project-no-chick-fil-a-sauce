import pygame
import os
from src.chicken import Chicken
from src.cloud import Cloud 
from src.background import Background
from src.score import Score 
class Controller:
  def mainloop(self):
    global game_speed, points
    background=Background()
    cloud=Cloud()
    player=Chicken()
    score=Score()
    screen_height= 500
    screen_width=1100
    game_speed=14
    
    points=0
    
    screen=pygame.display.set_mode((screen_width, screen_height))
    run=True
    while run:
      clock=pygame.time.Clock()
      while run:
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            run=False
        screen.fill((255,255,255))
        userinput=pygame.key.get_pressed()
        background.draw(screen)
        cloud.draw(screen)
        cloud.update()
        clock.tick(30)
        score.draw(screen)
        score.update()
        player.draw(screen)
        player.update(userinput)
        pygame.display.update()       

  def __init__(self):
    pass
  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw
