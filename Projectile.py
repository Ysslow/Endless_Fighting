import pygame

class Projectile(pygame.sprite.Sprite):

    

    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.SCREEN_WIDTH = 1080
      



    def update(self):
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > self.SCREEN_WIDTH:
            self.kill()

        if pygame.sprite.spritecollide(self.game.player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()
            
        if pygame.sprite.spritecollide(self.game.enemy, bullet_group, False):
            if enemy.alive:
                enemy.health -= 25
                self.kill()
                