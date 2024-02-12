import pygame
from Projectile import Projectile
import os
pygame.init()

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y, scale, Username, speed, ammo):
        super().__init__()
        self.health = 100
        self.name = Username
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0 
        self.jump = False
        self.in_air = False
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.score = 0
        self.direction = 1
        self.flip = False
        self.action = 0
        self.rect = pygame.Rect(0, 0, 125, 250)
        self.all_projectiles = pygame.sprite.Group()

        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'assets/player/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'assets/player/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        
        self.image = self.animation_list [self.action][self.frame_index]
      
    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def shoot(self, all_projectiles):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Projectile(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, self.game)
            self.all_projectiles.add(bullet)
            self.ammo -= 1

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0


    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.speed = 0
            self.update_action(3)
            

    def move_lateral(self, moving_left, moving_right):
        dx = 0
        dy = 0
            
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
            
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
   
        self.rect.x += dx
        self.rect.y += dy 

    def move_up(self,screen):
        if self.position == "standing":
            before_jump_image = self.image
            jump_speed = 75  # Ajustez la vitesse du saut selon vos besoins
            print (self.rect.x, self.rect.bottom)

            for i in range(6):
                # Changer l'image de saut à chaque frame
                self.image = self.jump_frames[i]
                
                if i < 3:
                    self.rect.y -= jump_speed
                    pygame.time.delay(50)
                    # afficher la nouvelle image de saut et retirer l'ancienne
                    screen.blit(self.image, (self.rect.x, self.rect.y))
                    pygame.display.flip()
                    print(self.rect.bottom,"je monte")
                else:
                    self.rect.y += jump_speed
                    pygame.time.delay(50)
                    screen.blit(self.image, (self.rect.x, self.rect.y))
                    pygame.display.flip()
                    print(self.rect.bottom,"je descend")

            self.image = before_jump_image

    def move_down(self):
        print (self.rect.x, self.rect.bottom)
        if self.position == "standing":
            if self.direction == "right":
                self.image = pygame.transform.scale(pygame.image.load('assets/crouch.png'), (125, 175))
            else : 
                self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/crouch.png'), (125, 175)), True, False)
            self.rect.bottom += 75
            self.position = "crouch"

    def reset_down_movement(self):
        if self.position == "crouch":
            if self.direction == "right":
                self.image = pygame.transform.scale(pygame.image.load('assets/character.png'), (125, 250))
            else : 
                self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load('assets/character.png'), (125, 250)), True, False)
            self.rect.bottom -= 75
            self.position = "standing"

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def launch_projectile(self):
        if self.attacklauncher:
            self.all_projectiles.add(Projectile(self))
            self.attacklauncher = False