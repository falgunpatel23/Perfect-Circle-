
import pygame
import circle

pygame.init()
_size = 640, 480
_screen = pygame.display.set_mode(_size)

circle.Init(_size)

def Update(deltaTime):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    circle.Update(deltaTime)

    return True

black = 0, 0, 0
def Render(screen):
    screen.fill(black)

    circle.Render(screen)

    pygame.display.flip()

_gTicksLastFrame = pygame.time.get_ticks()
_gDeltaTime = 0.0
while Update(_gDeltaTime):
    Render(_screen)
    t = pygame.time.get_ticks()
    _gDeltaTime = (t - _gTicksLastFrame) / 1000.0
    _gTicksLastFrame = t

circle.Close()