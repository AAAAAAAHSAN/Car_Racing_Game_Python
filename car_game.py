import random
import pygame
import time

pygame.init()  # initialize the package
car_size=(55,90)
grey=(118,119,110) # color code in RGB form
black=(0,0,0)
display=pygame.display.set_mode((1000,600)) # set the width and height of display
pygame.display.set_caption("Car racing game")
car_image = pygame.image.load("imgs/car0.png")
car_image = pygame.transform.scale(car_image, car_size)

backgroundLeft=pygame.image.load("imgs/side.png")
backgroundLeft=pygame.transform.scale(backgroundLeft,(200,700))
backgroundRight=pygame.image.load("imgs/side2.png")
backgroundRight=pygame.transform.scale(backgroundRight,(200,700))


def policecar(police_startx,police_starty,police):
    if police==0:
        police_come=pygame.image.load("imgs/car2.png")
        police_come=pygame.transform.scale(police_come,car_size)

    if police==1:
        police_come=pygame.image.load("imgs/car1.png")
        police_come=pygame.transform.scale(police_come,car_size)

    if police==2:
        police_come=pygame.image.load("imgs/car2.png")
        police_come=pygame.transform.scale(police_come,car_size)
    if police==3:
        police_come=pygame.image.load("imgs/car3.png")
        police_come=pygame.transform.scale(police_come,car_size)

    if police==4:
        police_come=pygame.image.load("imgs/car4.png")
        police_come=pygame.transform.scale(police_come,car_size)
    if police==5:
        police_come=pygame.image.load("imgs/car5.png")
        police_come=pygame.transform.scale(police_come,car_size)

    if police==6:
        police_come=pygame.image.load("imgs/car6.png")
        police_come=pygame.transform.scale(police_come,car_size)
    if police==7:
        police_come=pygame.image.load("imgs/car7.png")
        police_come=pygame.transform.scale(police_come,car_size)

    if police==8:
        police_come=pygame.image.load("imgs/car8.png")
        police_come=pygame.transform.scale(police_come,car_size)

    if police==9:
        police_come=pygame.image.load("imgs/car9.png")
        police_come=pygame.transform.scale(police_come,car_size)

    display.blit(police_come,(police_startx, police_starty))  # display police car

def crash():
    message_display("Game Over")


def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_object(text,largetext)
    textrect.center=((400),(300))  # show the message position
    display.blit(textsurf,textrect) # display the message
    pygame.display.update()  # update the display
    time.sleep(3)
    loop()


def text_object(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()


def background():
    display.blit(backgroundLeft,(0,0)) # set left side position
    display.blit(backgroundRight, (700,0)) # right side position


def car(x,y): # create car function
    display.blit(car_image,(x,y)) # set position of car


def loop():  # all the function are called using this function
    x=400
    y=500
    x_change=0  # set x position at x axis
    y_change=0
    car_width=23
    policecar_speed=5
    police=0  # police car is 0 stage
    police_startx=random.randrange(130,(700-car_width))
    police_starty=-600
    police_width=23
    police_height=47 # police car height

    bumped=False  # if game is not problem to start
    while not bumped:  # game is start
        for event in pygame.event.get(): # if any input is given
            if event.type==pygame.QUIT: # if quit imput is given
                #bumped=True  # game is stop
                pygame.quit()
                quit()

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
        police_starty-=policecar_speed/4  # police car speed at y axis
        policecar(police_startx,police_starty,police)  #  call the function
        police_starty+=policecar_speed  # police car speed increase
        car(x,y) # call the function of car
        if x<130 or x>700-car_width:
            #bumped=True # stop the game
            crash()
        if police_starty>600:
            police_starty=0-police_height  # only onc car is passed
            police_startx=random.randrange(130,(1000-300))  # another car is come
            police = random.randrange(0,10) # different car every times come
            print(police)

        if y<police_starty+police_height:
            if x>police_startx and x<police_startx+ police_width or x + car_width > police_startx and x + car_width<police_startx+ police_width:
                crash()

        pygame.display.update()
loop()
pygame.quit()
quit()