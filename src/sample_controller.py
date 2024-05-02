import pygame
import os
import random
from src.chicken import Chicken
from src.cloud import Cloud 
from src.background import Background
from src.score import Score 
from src.obstacle import Obstacle
from src.obstacle import Cone, Plane
class Controller:
  def __init__(self):
    pygame.init()
    self.screen=pygame.display.set_mode((1100, 500))
    self.clock=pygame.time.Clock()
    self.points=0
    self.score=0
    self.screen_height= 500
    self.screen_width=1100
    
  def run(self):
    death_count=0
    while True:
      self.menu(death_count)
      game_over, death_count=self.mainloop()
      if game_over:
        continue

  def mainloop(self):
    global game_speed
    obstacles=[]
    background=Background()
    cloud=Cloud()
    player=Chicken()
    score_obj=Score()
    game_speed=14
    death_count=0
    
    self.screen=pygame.display.set_mode((self.screen_width, self.screen_height))
    cone=pygame.image.load(os.path.join("assets/pictures/obstacles", "cone.png"))
    plane=pygame.image.load(os.path.join("assets/pictures/obstacles", "plane.png"))
    run=True
    obstacle_counter=0
    obstacle_frequency=60
    
    while run:
      clock=pygame.time.Clock()
      while run:
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            run=False
        self.screen.fill((255,255,255))
        userinput=pygame.key.get_pressed()
        
        obstacle_counter=obstacle_counter+1
        if obstacle_counter>=obstacle_frequency:
          if len(obstacles)==0:
            if random.randint(0,1)==0:
              obstacles.append(Cone(cone))
            else:
              obstacles.append(Plane(plane))
          else: 
            if random.randint(0,1)==0:
              obstacles.append(Cone(cone))
            else:
              obstacles.append(Plane(plane))
          obstacle_counter=0
        background.draw(self.screen)
        cloud.draw(self.screen)
        cloud.update()
        clock.tick(30)
        score_obj.draw(self.screen)
        score_obj.update()
        self.score=score_obj.score
        player.draw(self.screen)
        player.update(userinput)  
        new_obstacles=[]
        for obstacle in obstacles:
          if obstacle.rect.x+obstacle.rect.width<0:
            continue
          else:
            obstacle.update()
            obstacle.draw(self.screen)
          if player.chicken_rect.colliderect(obstacle.rect):
            player.img=player.death_img
            player.draw(self.screen)
            pygame.display.update()
            pygame.time.delay(500)
            death_count+=1
            return True, death_count
 
          new_obstacles.append(obstacle)
        obstacles=new_obstacles
        pygame.display.update()
    return False, death_count
        
  def menu(self, death_count):   
      run=True
      while run:
        self.screen.fill((105,177,191))
        font=pygame.font.Font(None, 40)
        
        if death_count==0:
          display=pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/extras", "logo.png")), (175,200))
          text=font.render(f'Press any key to start.', True, (0,0,0))  
        elif death_count>0:
          display=pygame.transform.scale(pygame.image.load(os.path.join("assets/pictures/extras", "sandwich.png")), (150,100))
          text=font.render(f'You just got cooked! Press any key to restart.', True, (0,0,0))
          score_text=font.render(f'Your score: {self.score}', True, (0,0,0))
          scoreRect=score_text.get_rect()
          scoreRect.center=(self.screen_width//2, self.screen_height//2+75)  
          self.screen.blit(score_text, scoreRect) 
        textRect=text.get_rect()
        textRect.center=(self.screen_width//2, self.screen_height//2+25) 
        self.screen.blit(text, textRect) 
        self.screen.blit(display, (self.screen_width//2-display.get_width()//2, 50))
        pygame.display.update()
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            pygame.quit()
          if event.type==pygame.KEYDOWN:
            self.points=0
            return


  
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
