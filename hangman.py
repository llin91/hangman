import pygame

def main():
        
    pygame.init()

    black = (0,0,0)
    white = (225,225,225)

    gameDisplay = pygame.display.set_mode((800,600))

    pygame.display.set_caption('Hangman')

    clock = pygame.time.Clock()

    hangmanImag=loadImag()

    gameDisplay.fill(white)
    gameDisplay.blit(hangmanImag[0],(0,0))
    pygame.display.update()

    pygame.draw.lines(gameDisplay, black, False, [(100,100), (150,200), (200,100)], 1)
    pygame.draw.line(gameDisplay, (0, 0, 255), (0, 0), (639, 479))
    pygame.display.update()


    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        pygame.display.update()
    pygame.quit()
    quit()



    # a function that display different image while player enter a letter

    # a function that place image
def loadImag():
        hangmanImag0 = pygame.image.load('hangman0.jpg')
        hangmanImag1 = pygame.image.load('hangman1.jpg')
        hangmanImag2 = pygame.image.load('hangman2.jpg')
        hangmanImag3 = pygame.image.load('hangman3.jpg')
        hangmanImag4 = pygame.image.load('hangman5.jpg')
        hangmanImag5 = pygame.image.load('hangman6.jpg')
        hangmanImag6 = pygame.image.load('hangman7.jpg')
        hangmanImag = [hangmanImag0,hangmanImag1,hangmanImag2,hangmanImag3,hangmanImag4,hangmanImag5,hangmanImag6]
        return hangmanImag





    # function that draw the lines

    # function that displays correct letter

    # pick vocab

main()
