import pygame
import os
from src.sample_controller import Controller
#import your controller

def main():
    pygame.init()
    play=Controller()
    play.mainloop()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
