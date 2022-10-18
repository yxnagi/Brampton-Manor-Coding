# pygame template - BMACS 2020
import pygame  # accesses pygame files
import sys  # to communicate with windows

# game setup ################ only runs once
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 800  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

currentheadx = 4
currentheady = 4
segments = 1

gameState = "running"  # controls which state the games is in
####### game loop #######runs 60 times a second!
while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab
    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
        if event.type == pygame.KEYDOWN:  # tests if a key has been pressed down
            if event.key == pygame.K_ESCAPE:  # tests if that pressed key is the escape key
                gameState = "exit"  # causes exit of game loop
            if event.key == pygame.K_DOWN:
                currentheady += 1
                currentheadx = currentheadx
            if event.key == pygame.K_UP:
                currentheady += -1
                currentheadx = currentheadx
            if event.key == pygame.K_RIGHT:
                currentheadx += 1
                currentheady = currentheady
            if event.key == pygame.K_LEFT:
                currentheadx += -1
                currentheady = currentheady
    ####### your code starts here #######
    print(currentheadx)
    print(currentheady)
    if currentheadx >= 8 or currentheadx < 0 or currentheady >= 8 or currentheady < 0:
        gameState = "exit"
    screen.fill(black)
    pygame.draw.rect(screen, white, (100 * currentheadx, 100 * currentheady, 100, 100))
    pygame.display.update()

    ####### your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value

####### out of game loop #######
print("The game has closed")  # notifies user the game has ended
pygame.quit()  # stops the game engine
sys.exit()  # close operating system window