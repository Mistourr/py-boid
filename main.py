import pygame
from boid import Boid
import random

pygame.init()

screen_width = 1920
screen_height = 1080
fps = 60
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("py-boid")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial" , 12 , bold = False)

# FPS display util function
def fps_counter():
    fps = f"{int(clock.get_fps())} FPS"
    fps_t = font.render(fps , 1, pygame.Color("GREEN"))
    screen.blit(fps_t,(15,15))

boids = [Boid(random.randint(300, 600), random.randint(150,400)) for i in range(250)]
for boid in boids:
    _pos = boid.getPos()
    boid.setPos(_pos.x + random.randint(0, 150), _pos.y + random.randint(-15, 15))
## Main render loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    delta = clock.tick(fps)/1000

    # Fill the screen with a background color
    screen.fill((0, 0, 0))

    # Draw all boids
    for boid in boids:
        velocity = boid.getVelocity()
        # TODO: call your boid logic here
        separation = boid.separation(boids)
        alignement = boid.alignement(boids)
        cohesion = boid.cohesion(boids)
        circling = boid.circling(screen_width, screen_height)
        velocity += cohesion * 0.01 + alignement * 0.01 + separation * 0.35 + circling * 0.03
        boid.setVelocity(velocity.normalize())
        # -------------------------------
        boid.move(delta)
        boid.draw(screen)

    # Draw the FPS counter
    fps_counter()

    # Update the display
    pygame.display.update()