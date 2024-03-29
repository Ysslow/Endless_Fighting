import pygame



class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.speed = 1
        self.image = pygame.image.load('assets/monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = 950
        self.rect.bottom = 705 

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.speed
            return True
        print("collision")
        return False
        

