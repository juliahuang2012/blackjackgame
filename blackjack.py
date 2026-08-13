import pygame
import random
import time

pygame.init()  

screen_width = 1000
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))

suits = ["diamonds", "hearts", "spades", "clubs"]
numbers = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
cardimages = {}
cardsize = 20

font = pygame.font.SysFont("Arial", 20)

for suit in suits:  #loading card image files into a dictionary by suit and number
    cardimages[suit] = {}
    for number in numbers:
        card = pygame.image.load("playing cards\\" + str(number) + "_of_" + suit + ".png")
        card = pygame.transform.scale(card, (cardsize*5, cardsize*7))
        cardimages[suit][number] = card

def createcard():
    suits = ["diamonds", "hearts", "spades", "clubs"]
    numbers = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
    suit = random.choice(suits)
    number = random.choice(numbers)
    return {"suit":suit, "number": number}

def facevalue(card):
    value = card["number"]
    cardconvert = {
        "ace": 1,
        "jack": 11,
        "queen": 12,
        "king": 13
    }
    if value in cardconvert:
        return cardconvert[value]
    else:
        return value

def randomizeCards():   #function for randomizing cards
    return cardimages[random.choice(suits)][random.choice(numbers)]

def getcardimage(card):
    return cardimages[card["suit"]][card["number"]]

def drawhandtoscreen(hand, x, y, spacebetweencards):
    for i in range(len(hand)):
        screen.blit(getcardimage(hand[i]), (spacebetweencards*i + x, y))  #displays 2 random cards
        
def getcardtotal(hand):
    cardtotal = 0
    for card in hand:
        cardtotal += facevalue(card)
    return cardtotal

def printcardvalue(total, x, y, person):
    card_value_text = font.render(f"{person} total is {total}", True, "black", None)
    text_position = (x, y)
    card_value_rect = card_value_text.get_rect(midtop = text_position)
    screen.blit(card_value_text, card_value_rect)


running = True    #game loop; handles graphics
#firstcard = cardimages[random.choice(suits)][random.choice(numbers)]
drawcards = False

playerhand = []
computerhand = []

playerhand.append(createcard())    #adds the random cards to the list
playerhand.append(createcard())
        
computerhand.append(createcard())
computerhand.append(createcard())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:    # adds a new card
            if event.key == pygame.K_SPACE and len(playerhand) < 5:   # caps the draws to 5 total cards
                playerhand.append(createcard())
                drawcards = False
                
    screen.fill((156, 180, 217))
    if drawcards == False:    #randomizes cards and does it once
        
        drawhandtoscreen(playerhand, 136, screen_height*1.75/3, 125)
        drawhandtoscreen(computerhand, 136, screen_height/6, 125)

        card_value_text = font.render("Your total is " + str(getcardtotal(playerhand)), True, "black", None)    #prints the total combined values
        
        card_value_text = font.render("Your total is " + str(getcardtotal(playerhand)), True, "black", None)
        
        #card_value_rect = card_value_text.get_rect(midtop = text_position)
        printcardvalue(getcardtotal(playerhand), screen_width/2, screen_height*8/9, "Player")
        printcardvalue(getcardtotal(computerhand), screen_width/2, screen_height*1/9, "Computer")
        #screen.blit(card_value_text, card_value_rect)
        drawcards = True
        pygame.display.flip() 
    
pygame.quit()

