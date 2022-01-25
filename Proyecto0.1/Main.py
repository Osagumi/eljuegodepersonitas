#librerrias
from re import X
import sys
import os 
import pygame
from pygame.locals import *

#inicializacion 
pygame.init()

fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
#definiciones
picture = pygame.image.load(r'../Proyecto0.1/997073.png')
velocity = 5
x = 2
y = 0

# Game loop.
while True:
  fpsClock.tick(fps)
  screen.fill((0, 0, 0))
  screen.blit(picture, (x,y))
  x += velocity
  if x <= 0:
      velocity = 5
  if x >= 388:
      velocity = -5

  
  

  print(x)
  pygame.display.update()#esto hace que se actualice en tiempo real
  for event in pygame.event.get():  
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  
  # Draw.
  


