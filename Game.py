import pygame
from Player import Player
from Projectile import Projectile

class Game:

    def __init__(self):        
        self.player = Player(200, 200, 3, 'player', 5, 20)
        self.pressed = {}