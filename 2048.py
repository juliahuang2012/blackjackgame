import pygame as pg
import random

pg.init()

# screen = pg.display.set_mode(flags = pg.FULLSCREEN)

screen_width = 1280
screen_height = 720

screen = pg.display.set_mode([screen_width, screen_height])


font = pg.font.SysFont("Clear Sans Bold", 100)


class Square(pg.sprite.Sprite):
    def __init__(self, x, y, color = (117, 116, 116)):
        super().__init__()
        self.image = pg.Surface((100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image.fill(color)

gap = 10 

# square1 = Square(402.5, 150)
# square2 = Square(502.5 + gap, 150)
# square3 = Square(602.5 + gap*2, 150)
# square4 = Square(702.5 + gap*3, 150)

all_squares = pg.sprite.Group()

for x in range(4):    #makes the grid of squares
    for y in range(4):
        all_squares.add(Square(425 + 100*x + gap*x, 150 + 100*y + gap*y))


class NumberSquare(pg.sprite.Sprite):    #specific initial number sprite w/ different color
    def __init__(self, x, y, color = (189, 180, 160),):
        super().__init__()
        self.image = pg.Surface((100,100))
        self.image.fill(color)
        
        self.number = "2"    #for the text
        self.squarefont = pg.font.SysFont("Clear Sans Bold", 80)
        text_surface = self.squarefont.render(self.number, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = self.image.get_rect().center
        
        self.image.blit(text_surface, text_rect)    #for the surface
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        
nsquare1 = NumberSquare(525 + gap, 150)

#all_squares.add(Square)


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    screen.fill((201, 199, 199))
    
    name_text = font.render("2048", True, "black", None)
    name_text_rect = name_text.get_rect()       #position of title text by adding rectangle to text
    name_text_rect.center = (screen_width/2, 70)   
    all_squares.draw(screen) #draws squares on screen
    screen.blit(name_text, name_text_rect)  #draws title on screen
    screen.blit(nsquare1.image, nsquare1.rect) #draws number square on screen
    
    pg.display.flip()
    
pg.quit()