import pygame
import random
pygame.init()

class DrawInfo:
    BLACK = 0,0,0 # COLORS ARE DEFINED IN RGB
    WHITE = 2,5,5
    GREEN = 0,255,0
    RED  = 255,0,0
    GREY = 128,128,128
    BACKGROUND_COLOR = WHITE

    SIDE_PAD = 100
    TOP = 150

    def __init__(self,width,height,list):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst)) #14.30
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_value - self.min_value))