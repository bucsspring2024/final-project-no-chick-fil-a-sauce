import pygame
import os
class Controller:
  def mainloop(self):
    from chicken import Chicken 
    player=Chicken()
    screen_height= 600
    screen_width=1100
    screen=pygame.display.set_mode((screen_width, screen_height))
    run=True
    while run:
      clock=pygame.time.Clock()
      while run:
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            run=False
        screen.fill(255,255,255)
        userinput=pygame.key.get_pressed()
        player.draw(screen)
        player.update(userinput)
        clock.tick(30)
        pygame.display.update()
  def __init__(self):
      
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
