# Example file showing a circle moving on screen
import pygame
import random


# pygame setup
pygame.init()

#dimensions
width = 720
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DDONG Game")
# clock for controling speed of snake
clock = pygame.time.Clock()
# Snake parameters
snake_block = 10
snake_speed = 15
running = True
dt = 0


class FallingObject:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = 0
        self.speed = random.randint(600,1400)
    def draw(self):
        pygame.draw.circle(screen, "pink", pygame.Vector2(self.x, self.y), 10)



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height()-20)
poop_initial_pos = pygame.Vector2(screen.get_width() / 4, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Poop
    pygame.draw.circle(screen, "pink", poop_initial_pos, 10)

    pygame.draw.circle(screen, "red", player_pos, 20)

    keys = pygame.key.get_pressed()

    poop_initial_pos.y += 600 * dt
    
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    


    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()