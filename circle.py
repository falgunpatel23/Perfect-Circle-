
import pygame
import math
import numpy as np

def Init(size):
    global _size
    global _radius
    _size = np.array(size)
    _radius = _size[0]
    if _size[1] < _radius:
        _radius = _size[1]
    _radius -= 1
    _radius //= 2

def Update(deltaTime):
    pass

def DrawLine(screen, x1, y1, x2, y2):
    pygame.draw.line(screen, (255,255,255), (x1,y1), (x2,y2))

def Render(screen):
    global _size
    global _radius

    center_x = _size[0] // 2
    center_y = _size[1] // 2
    radius = _radius

    pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), radius, 1)


    for x_offset in range(-radius, radius + 1):
        x = center_x + x_offset
        y_squared = radius**2 - x_offset**2
        
        if y_squared >= 0:
            y = int(y_squared**0.5) 
            
            DrawLine(screen, x, center_y - y, x, center_y - y)
            DrawLine(screen, x, center_y + y, x, center_y + y)

def Close():
    pass