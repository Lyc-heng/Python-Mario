import pygame
from pygame.locals import *
from sys import exit

class Music():
    def __init__(self,sound):
        self.channel = None
        self.sound = sound     
    def play_sound(self):
        self.channel = pygame.mixer.find_channel(True)
        self.channel.set_volume(0.5)
        self.channel.play(self.sound)
    def play_pause(self):
        self.channel.set_volume(0.0)
        self.channel.play(self.sound)
