#  Copyright (c) 2017 Jon Cooper
#
#  This file is part of pygame-xbox360controller.
#  Documentation, related files, and licensing can be found at
#
#      <https://github.com/joncoop/pygame-xbox360controller>.


import pygame
import logitechG29_wheel
import socket

pygame.init()

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# window settings
size = [600, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Steering")

FPS = 10

clock = pygame.time.Clock()

# make a controller
controller = logitechG29_wheel.Controller(0)

# make a ball
ball_pos = [290, 290]
ball_radius = 20
ball_color = WHITE

# game loop
done = False

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    # handle joysticks
    left_x, left_y = controller.get_left_stick()
    
    msgX = bytes([126 + int(left_x * 126)])
    msgY = bytes([126 + int(left_y * 126)])
    sock.sendto(msgX + msgY, ("192.168.0.100", 5005))
    
    
    # game logic
    ball_pos[0] = 290 + int(left_x * 200)
    ball_pos[1] = 290 + int(left_y * 200)
    
    # drawing
    screen.fill(BLACK)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    # update screen
    pygame.display.flip()
    clock.tick(FPS)

# close window on quit
pygame.quit ()
