import pygame
from boid import Boid

pygame.init()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("py-boid")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial" , 12 , bold = False)

# FPS display util function
def fps_counter():
    fps = f"{int(clock.get_fps())} FPS"
    fps_t = font.render(fps , 1, pygame.Color("GREEN"))
    screen.blit(fps_t,(15,15))

boids = [Boid() for i in range(500)]
## Main render loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    # Draw all boids
    for boid in boids:
        # TODO: call your boid logic here

        # -------------------------------
        boid.draw(screen)

    # Draw the FPS counter
    fps_counter()

    # Update the display
    pygame.display.update()
    clock.tick(60)