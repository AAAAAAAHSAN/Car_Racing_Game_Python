import pygame
pygame.init()  # initialize the package

grey=(118,119,110) # color code in RGB form

display=pygame.display.set_mode((1000,600)) # set the width and height of display
pygame.display.set_caption("Car racing game")
car_image=pygame.image.load("imgs/car1.png")
car_image= pygame.transform.scale(car_image,(55,90))

backgroundLeft=pygame.image.load("imgs/side.png")
backgroundLeft=pygame.transform.scale(backgroundLeft,(200,700))
backgroundRight=pygame.image.load("imgs/side2.png")
backgroundRight=pygame.transform.scale(backgroundRight,(200,700))


def background():
    display.blit(backgroundLeft,(0,0)) # set left side position
    display.blit(backgroundRight, (700,0)) # right side position


def car(x,y): # create car function
    display.blit(car_image,(x,y)) # set position of car


def loop():  # all the function are called using this function
    x=400
    y=500
    x_change=0  # set x position at x axis
    car_width=23
    bumped=False  # if game is not problem to start
    while not bumped:  # game is start
        for event in pygame.event.get(): # if any input is given
            if event.type==pygame.QUIT: # if quit imput is given
                bumped=True  # game is stop

            if event.type==pygame.KEYDOWN:  # if any key pressed
                if event.key==pygame.K_LEFT:
                    x_change=-5  # move left side -5
                if event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type == pygame.KEYUP:
                x_change=0
        x+= x_change

        display.fill(grey)
        background()
        car(x,y) # call the function of car
        if x<130 or x>700-car_width:
            bumped=True # stop the game
        pygame.display.update()
loop()
pygame.quit()
quit()