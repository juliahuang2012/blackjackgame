import pygame as pg
import random

pg.init()

screen = pg.display.set_mode(flags = pg.FULLSCREEN)

font = pg.font.SysFont("Clear Sans Bold", 100)


class Square(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

square1 = Square(200, 200)

all_squares = pg.sprite.Group()
all_squares.add(Square)



running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    screen.fill((201, 199, 199))
    
    name_text = font.render("2048", True, "black", None)
    all_squares.draw(screen)
    screen.blit(name_text, (900, 70))
    screen.blit(square1.image, square1.rect)
    pg.display.flip()
    
pg.quit()