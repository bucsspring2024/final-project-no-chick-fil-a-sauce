import pygame
import os
from src.sample_controller import Controller
#import your controller

def main():
    pygame.init()
    play=Controller()
    play.run()

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':  
    main()
