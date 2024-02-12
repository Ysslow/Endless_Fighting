import pygame
from Game import Game

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

pygame.display.set_caption("Endless Fighting")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets/background.jpg')

game = Game()

clock = pygame.time.Clock()
FPS = 60

moving_left = False
moving_right = False
shoot = False




running = True
# Main loop
while running:
    
    clock.tick(FPS)

    screen.blit(background, (0, 0))

    game.player.update()
    game.player.draw(screen)

    game.player.all_projectiles.update()
    game.player.all_projectiles.draw(screen)


    game.player.draw(screen)
    
    pygame.display.flip()
    
    if game.player.alive:
        if shoot:
            game.player.shoot()
        if game.player.in_air:
            game.player.update_action(2)
        elif moving_left or moving_right:
            game.player.update_action(1)
        else:
            game.player.update_action(0)
        game.player.move_lateral(moving_left, moving_right)

    for event in pygame.event.get():
		#quit game
        if event.type == pygame.QUIT:
            running = False
            print("Endless Fighting has been closed.")
		#keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False

pygame.quit()