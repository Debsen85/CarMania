#####Importing the required modules 
import pickle
import dbm
import sys
import os
import pygame
import random
from pygame.locals import *
from os import path
import os.path

pygame.init()
gamedisplay = pygame.display.set_mode((800,600))
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Car Mania")
clock = pygame.time.Clock()

#####Loading Images

explodeimg = pygame.image.load("explode.png")
introimg = pygame.image.load("Car.jpg")
carchoicepageimg = pygame.image.load("intro_1.jpg") 
roadimg = pygame.image.load("Road.jpg")
grassimg = pygame.image.load("Grass.jpg")
car_1_img = pygame.image.load("car_1.png")
car_2_img = pygame.image.load("car_2.png")
car_3_img = pygame.image.load("car_3.png")
car_4_img = pygame.image.load("car_4.png")
car_5_img = pygame.image.load("car_5.png")
car_6_img = pygame.image.load("car_6.png")
car_7_img = pygame.image.load("car_7.png")
car_8_img = pygame.image.load("car_8.png")
car_9_img = pygame.image.load("car_9.png")
car_10_img = pygame.image.load("car_10.png")

#####Loading Sounds & Music

explode_sound = pygame.mixer.Sound("crash.wav")
intro_sound = pygame.mixer.Sound("Ahrix.ogg")
pygame.mixer.music.load("Alan_1.ogg")

#####Colour

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
brightred = (255,0,0)
green = (0,200,0)
brightgreen = (0,255,0)
blue = (0,0,200)
brightblue = (0,0,255)
yellow = (200,200,0)
brightyellow = (255,255,0)
purple = (200,0,200)
brightpurple = (255,0,255)

#####Functions

def quitgame():
    pygame.quit()
    sys.exit()
    
def road1(x,y):
    gamedisplay.blit(roadimg,(x,y))
    
def road2(x,y):
    gamedisplay.blit(roadimg,(x,y))
    
def road3(x,y):
    gamedisplay.blit(roadimg,(x,y))
    
def grass1(x,y):
    gamedisplay.blit(grassimg,(x,y))
    
def grass2(x,y):
    gamedisplay.blit(grassimg,(x,y))
    
def grass3(x,y):
    gamedisplay.blit(grassimg,(x,y))

def Label(msg,x,y,size,color):
    font = pygame.font.SysFont("Arial",size)
    text = font.render(msg,True,color)
    gamedisplay.blit(text,(x,y))

def car_Label(img,x,y):
    image = pygame.image.load(img)
    gamedisplay.blit(image,(x,y))  
    
def Button(msg,x,y,width,height,i_color,a_color,command=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gamedisplay,a_color,(x,y,width,height))
        if click[0] == 1 and command != None:
            command()
    else:
        pygame.draw.rect(gamedisplay,i_color,(x,y,width,height))
    buttontext = pygame.font.SysFont("Arial",20)
    buttonmsg = buttontext.render(msg,True,black)
    buttonmsgrect = buttonmsg.get_rect()
    buttonmsgrect.center = ((x+width/2),(y+height/2))
    gamedisplay.blit(buttonmsg,buttonmsgrect)

def car_Button(msg_1,msg_2,x,y,width,height,i_color,a_color,command=None):
    mouse = pygame.mouse.get_pos()
    global clk
    global image_2
    clk = mouse[1]
    click = pygame.mouse.get_pressed()
    if x+width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gamedisplay,a_color,(x,y,width,height))
        if click[0] == 1 and command != None:
            image_2 = msg_1
            command()
            
    else:
        pygame.draw.rect(gamedisplay,i_color,(x,y,width,height))
    buttontext = pygame.font.SysFont("Arial",20)
    buttonmsg = buttontext.render(msg_2,True,black)
    buttonmsgrect = buttonmsg.get_rect()
    buttonmsgrect.center = ((x+width/2),(y+height/2))
    gamedisplay.blit(buttonmsg,buttonmsgrect)
    
def explode(x,y):
    x -= 50
    y += 15
    gamedisplay.blit(explodeimg,(x,y))
    pygame.mixer.Sound.play(explode_sound)

def crash(x,y):
    pygame.mixer.music.stop()
    explode(x,y)
    Label("You Crashed!",150,200,100,yellow)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Button("Try Again",200,420,100,50,green,brightgreen,gameloop)
        Button("Exit",500,420,100,50,red,brightred,quitgame)
        Button("Intro", 20, 500, 100, 50, purple, brightpurple, intro)
        Label("Tip: Dodge the incoming Cars",230,500,30,brightblue)
        Label("Your Score : "+str(score),310,320,30,brightblue)
        highscore()
        pygame.display.update()
        clock.tick(15)
        
def highscore():
    #####getting the directory of the text file in which the highscores will be saved if the function returns false a *.txt File will be created
    path = os.getcwd()
    if os.path.isfile(path+"/high.txt") == False :
        with open('high.txt', 'w+') as file:
            high_1 = 0
    try:
        with open('high.txt', 'rb') as file:
            high_1 = pickle.load(file)
    except:
        high_1 = 0

    if ((high_1 == 0) and (score == 0)) :
        Label("No high scores yet ",290,360,30,brightred)

    elif ((score < high_1) and (high_1 != 0)):
        Label("High score in previous attempts : "+str(high_1),210,360,30,brightred)
        
    elif (score >= high_1) :
        high_1 = score
        Label("Congratulations you have scored the highest score : "+str(high_1),97,360,30,brightred)
        with open('high.txt', 'wb') as file:
            pickle.dump(high_1, file)
       
    
def scorelabel(score):
    Label("Score: "+str(score),5,5,30,white)
    path = os.getcwd()
    if os.path.isfile(path+"/high.txt") == False :
        with open('high.txt', 'w+') as file:
            high = 0
    try:
        with open('high.txt', 'rb') as file:
            high = pickle.load(file)
    except:
        high = 0
    if (score < high):
        Label("H.S: "+str(high),5,45,30,white)
    else :
        Label("H.S: "+str(score),5,45,30,white) 
        
def unpause():
    pygame.mixer.music.unpause()
    global paused
    paused = False

def pause():
    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        Label("Paused",250,150,100,blue)
        Button("Continue",200,400,100,50,green,brightgreen,unpause)
        Button("Exit",500,400,100,50,red,brightred,quitgame)
        Button("Restart", 680, 500, 100, 50, yellow, brightyellow, gameloop)
        Button("Intro",20,500,100,50,purple,brightpurple,intro)
        pygame.display.update()
        clock.tick(15)
        
def mycar(image,x,y):
    gamedisplay.blit(image,(x,y))

def car_1(x,y):
    gamedisplay.blit(car_1_img,(x,y))

def car_2(x,y):
    gamedisplay.blit(car_2_img,(x,y))

def car_3(x,y):
    gamedisplay.blit(car_3_img,(x,y))

def car_4(x,y):
    gamedisplay.blit(car_4_img,(x,y))

def car_5(x,y):
    gamedisplay.blit(car_5_img,(x,y))

def car_6(x,y):
    gamedisplay.blit(car_6_img,(x,y))

def car_7(x,y):
    gamedisplay.blit(car_7_img,(x,y))

def car_8(x,y):
    gamedisplay.blit(car_8_img,(x,y))

def car_9(x,y):
    gamedisplay.blit(car_9_img,(x,y))

def car_10(x,y):
    gamedisplay.blit(car_10_img,(x,y))

#####Main_game

def intro():
    pygame.mixer.Sound.play(intro_sound, -1)
    gamedisplay.blit(introimg, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Label("Welcome to Car Mania",70,50,80,red)
        Label("Press p to pause",320,490,27,purple)
        Label("Press Right and Left Arrow Keys to Navigate",185,550,27,purple)
        Button("Next",200,470,100,50,green,brightgreen,instruction)
        Button("Exit",500,470,100,50,blue,brightblue,quitgame)
        pygame.display.update()

def instruction():
    gamedisplay.fill(black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
                
        Label("INSTRUCTIONS :", 10, 10, 40, red)
        Label("Select Between Road-Cars & F1-Cars on the next page", 10, 60, 20, white)
        Label("Top 5 are the Road-Cars & Bottom 5 are the F1-Cars", 10, 90, 20, white)
        Label("Click on the rectangular button above the car to select the car", 10, 120, 20, white)
        Label("Race against other cars", 10, 150, 20, white)
        Label("Don't crash.If you do crash no need to panic just start over again", 10, 180, 20, white)
        Label("REMEMBER :", 10, 230, 40, green)
        Label("If you pick the Road-Cars you will race against the F1-Cars & vice-versa", 10, 280, 20, white)
        Button("Next",100,450,100,50,green,brightgreen,carchoice)
        Button("Exit",600,450,100,50,red,brightred,quitgame)
        pygame.display.update()
        clock.tick(15)


def carchoice():
    gamedisplay.blit(carchoicepageimg, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Label("Please Select a car from the list given below",150,10,30,black)        
        car_Label("car_1.png",65,165)
        car_Label("car_2.png",215,165)
        car_Label("car_3.png",365,165)
        car_Label("car_4.png",515,165)
        car_Label("car_5.png",670,165)
        car_Label("car_6.png",65,365)
        car_Label("car_7.png",215,365)
        car_Label("car_8.png",365,365)
        car_Label("car_9.png",515,365)
        car_Label("car_10.png",670,365)           
        car_Button("car_1.png","Convertible",50,110,100,50,green,brightgreen,gameloop)
        car_Button("car_2.png","Roadster",200,110,100,50,blue,brightblue,gameloop)
        car_Button("car_3.png","Tesla",350,110,100,50,green,brightgreen,gameloop)
        car_Button("car_4.png","Lambo",500,110,100,50,blue,brightblue,gameloop)
        car_Button("car_5.png","GTR",650,110,100,50,green,brightgreen,gameloop)
        car_Button("car_6.png","F1-Marussia",50,310,100,50,green,brightgreen,gameloop)
        car_Button("car_7.png","F1-Williams",200,310,100,50,blue,brightblue,gameloop)
        car_Button("car_8.png","F1-Ferrari",350,310,100,50,green,brightgreen,gameloop)
        car_Button("car_9.png","F1-Renault",500,310,100,50,blue,brightblue,gameloop)
        car_Button("car_10.png","F1-Mclaren",650,310,100,50,green,brightgreen,gameloop)
        Button("Exit",350,530,100,50,red,brightred,quitgame)
        pygame.display.update()

def gameloop():
    pygame.mixer.Sound.stop(intro_sound)
    pygame.mixer.music.play(-1)
    global paused
    speed = 0
    global score
    score = 0
    change_x = 0
    myx = 370
           
    mycarimg = pygame.image.load(image_2)
    
    road1y = -225
    road2y = -225-825
    road3y = -225-825-825
    road_speed = 15

    grass1y = -1422+600
    grass2y = -1422*2 + 600
    grass3y = -1422*3 + 600

    car_1_x = random.randrange(100,700-62)
    car_1_y = -130
    car_1_speed = 0

    car_2_x = random.randrange(100,700-62)
    car_2_y = -130
    car_2_speed = -2
    
    car_3_x = random.randrange(100,700-62)
    car_3_y = -130
    car_3_speed = -4

    car_4_x = random.randrange(100,700-62)
    car_4_y = -130
    car_4_speed = -6

    car_5_x = random.randrange(100,700-62)
    car_5_y = -130
    car_5_speed = -8

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -5
                if event.key == pygame.K_RIGHT:
                    change_x = 5
                if event.key == pygame.K_p:
                    paused = True
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_x = 0
   
        #####grass
        
        if grass1y > 600:
            grass1y = -1422
        if grass2y > 600:
            grass2y = -1422
        if grass3y > 600:
            grass3y = -1422
        grass1y += road_speed + speed
        grass2y += road_speed + speed
        grass3y += road_speed + speed
        grass1(0,grass1y)
        grass2(0,grass2y)
        grass3(0,grass3y)

        #####Road

        if road1y > 600:
            road1y = -825
        if road2y > 600:
            road2y = -825
        if road3y > 600:
            road3y = -825
        road1y += road_speed + speed
        road2y += road_speed + speed
        road3y += road_speed + speed
        road1(100, road1y)
        road2(100,road2y)
        road3(100,road3y)

        #####Cars

        scorelabel(score)
        myx += change_x
        mycar(mycarimg, myx, 460)

        if 160 > clk > 110 :
            
            car_6(car_1_x,car_1_y)
            car_1_y += car_1_speed + speed
            if car_1_y > 600:
                car_1_y = -2000
                car_1_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_1_x < car_2_x + 62 or car_2_x < car_1_x + 62 < car_2_x + 62 or car_2_x < car_1_x + 31 < car_2_x + 62) or (car_3_x < car_1_x < car_3_x + 62 or car_3_x < car_1_x + 62 < car_3_x + 62 or car_3_x < car_1_x + 31 < car_3_x + 62) or (car_4_x < car_1_x < car_4_x + 62 or car_4_x < car_1_x + 62 < car_4_x + 62 or car_4_x < car_1_x + 31 < car_4_x + 62) or (car_5_x < car_1_x < car_5_x + 62 or car_5_x < car_1_x + 62 < car_5_x + 62 or car_5_x < car_1_x + 31 < car_5_x + 62):
                car_1_x = random.randrange(100,700-62)

            car_7(car_2_x,car_2_y)
            car_2_y += car_2_speed + speed
            if car_2_y > 600:
                car_2_y = -2000
                car_2_x = random.randrange(100,700-62)
                score += 1
            while (car_1_x < car_2_x < car_1_x + 62 or car_1_x < car_2_x + 62 < car_1_x + 62 or car_1_x < car_2_x + 31 < car_1_x + 62) or (car_3_x < car_2_x < car_3_x + 62 or car_3_x < car_2_x + 62 < car_3_x + 62 or car_3_x < car_2_x + 31 < car_3_x + 62) or (car_4_x < car_2_x < car_4_x + 62 or car_4_x < car_2_x + 62 < car_4_x + 62 or car_4_x < car_2_x + 31 < car_4_x + 62) or (car_5_x < car_2_x < car_5_x + 62 or car_5_x < car_2_x + 62 < car_5_x + 62 or car_5_x < car_2_x + 31 < car_5_x + 62):
                car_2_x = random.randrange(100,700-62)

            car_8(car_3_x,car_3_y)
            car_3_y += car_3_speed + speed
            if car_3_y > 600:
                car_3_y = -2000
                car_3_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_3_x < car_2_x + 62 or car_2_x < car_3_x + 62 < car_2_x + 62 or car_2_x < car_3_x + 31 < car_2_x + 62) or (car_1_x < car_3_x < car_1_x + 62 or car_1_x < car_3_x + 62 < car_1_x + 62 or car_1_x < car_3_x + 31 < car_1_x + 62) or (car_4_x < car_3_x < car_4_x + 62 or car_4_x < car_3_x + 62 < car_4_x + 62 or car_4_x < car_3_x + 31 < car_4_x + 62) or (car_5_x < car_3_x < car_5_x + 62 or car_5_x < car_3_x + 62 < car_5_x + 62 or car_5_x < car_3_x + 31 < car_5_x + 62):
                car_3_x = random.randrange(100,700-62)

            car_9(car_4_x,car_4_y)
            car_4_y += car_4_speed + speed
            if car_4_y > 600:
                car_4_y = -2000
                car_4_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_4_x < car_2_x + 62 or car_2_x < car_4_x + 62 < car_2_x + 62 or car_2_x < car_4_x + 31 < car_2_x + 62) or (car_3_x < car_4_x < car_3_x + 62 or car_3_x < car_4_x + 62 < car_3_x + 62 or car_3_x < car_4_x + 31 < car_3_x + 62) or (car_1_x < car_4_x < car_1_x + 62 or car_1_x < car_4_x + 62 < car_1_x + 62 or car_1_x < car_4_x + 31 < car_1_x + 62) or (car_5_x < car_4_x < car_5_x + 62 or car_5_x < car_4_x + 62 < car_5_x + 62 or car_5_x < car_4_x + 31 < car_5_x + 62):
                car_4_x = random.randrange(100,700-62)

            car_10(car_5_x,car_5_y)
            car_5_y += car_5_speed + speed
            if car_5_y > 600:
                car_5_y = -2000
                car_5_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_5_x < car_2_x + 62 or car_2_x < car_5_x + 62 < car_2_x + 62 or car_2_x < car_5_x + 31 < car_2_x + 62) or (car_3_x < car_5_x < car_3_x + 62 or car_3_x < car_5_x + 62 < car_3_x + 62 or car_3_x < car_5_x + 31 < car_3_x + 62) or (car_4_x < car_5_x < car_4_x + 62 or car_4_x < car_5_x + 62 < car_4_x + 62 or car_4_x < car_5_x + 31 < car_4_x + 62) or (car_1_x < car_5_x < car_1_x + 62 or car_1_x < car_5_x + 62 < car_1_x + 62 or car_1_x < car_5_x + 31 < car_1_x + 62):
                car_5_x = random.randrange(100,700-62)


        elif 360 > clk > 310 :
            
            car_1(car_1_x,car_1_y)
            car_1_y += car_1_speed + speed
            if car_1_y > 600:
                car_1_y = -2000
                car_1_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_1_x < car_2_x + 62 or car_2_x < car_1_x + 62 < car_2_x + 62 or car_2_x < car_1_x + 31 < car_2_x + 62) or (car_3_x < car_1_x < car_3_x + 62 or car_3_x < car_1_x + 62 < car_3_x + 62 or car_3_x < car_1_x + 31 < car_3_x + 62) or (car_4_x < car_1_x < car_4_x + 62 or car_4_x < car_1_x + 62 < car_4_x + 62 or car_4_x < car_1_x + 31 < car_4_x + 62) or (car_5_x < car_1_x < car_5_x + 62 or car_5_x < car_1_x + 62 < car_5_x + 62 or car_5_x < car_1_x + 31 < car_5_x + 62):
                car_1_x = random.randrange(100,700-62)

            car_2(car_2_x,car_2_y)
            car_2_y += car_2_speed + speed
            if car_2_y > 600:
                car_2_y = -3000
                car_2_x = random.randrange(100,700-62)
                score += 1
            while (car_1_x < car_2_x < car_1_x + 62 or car_1_x < car_2_x + 62 < car_1_x + 62 or car_1_x < car_2_x + 31 < car_1_x + 62) or (car_3_x < car_2_x < car_3_x + 62 or car_3_x < car_2_x + 62 < car_3_x + 62 or car_3_x < car_2_x + 31 < car_3_x + 62) or (car_4_x < car_2_x < car_4_x + 62 or car_4_x < car_2_x + 62 < car_4_x + 62 or car_4_x < car_2_x + 31 < car_4_x + 62) or (car_5_x < car_2_x < car_5_x + 62 or car_5_x < car_2_x + 62 < car_5_x + 62 or car_5_x < car_2_x + 31 < car_5_x + 62):
                car_2_x = random.randrange(100,700-62)

            car_3(car_3_x,car_3_y)
            car_3_y += car_3_speed + speed
            if car_3_y > 600:
                car_3_y = -3000
                car_3_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_3_x < car_2_x + 62 or car_2_x < car_3_x + 62 < car_2_x + 62 or car_2_x < car_3_x + 31 < car_2_x + 62) or (car_1_x < car_3_x < car_1_x + 62 or car_1_x < car_3_x + 62 < car_1_x + 62 or car_1_x < car_3_x + 31 < car_1_x + 62) or (car_4_x < car_3_x < car_4_x + 62 or car_4_x < car_3_x + 62 < car_4_x + 62 or car_4_x < car_3_x + 31 < car_4_x + 62) or (car_5_x < car_3_x < car_5_x + 62 or car_5_x < car_3_x + 62 < car_5_x + 62 or car_5_x < car_3_x + 31 < car_5_x + 62):
                car_3_x = random.randrange(100,700-62)

            car_4(car_4_x,car_4_y)
            car_4_y += car_4_speed + speed
            if car_4_y > 600:
                car_4_y = -2000
                car_4_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_4_x < car_2_x + 62 or car_2_x < car_4_x + 62 < car_2_x + 62 or car_2_x < car_4_x + 31 < car_2_x + 62) or (car_3_x < car_4_x < car_3_x + 62 or car_3_x < car_4_x + 62 < car_3_x + 62 or car_3_x < car_4_x + 31 < car_3_x + 62) or (car_1_x < car_4_x < car_1_x + 62 or car_1_x < car_4_x + 62 < car_1_x + 62 or car_1_x < car_4_x + 31 < car_1_x + 62) or (car_5_x < car_4_x < car_5_x + 62 or car_5_x < car_4_x + 62 < car_5_x + 62 or car_5_x < car_4_x + 31 < car_5_x + 62):
                car_4_x = random.randrange(100,700-62)

            car_5(car_5_x,car_5_y)
            car_5_y += car_5_speed + speed
            if car_5_y > 600:
                car_5_y = -1000
                car_5_x = random.randrange(100,700-62)
                score += 1
            while (car_2_x < car_5_x < car_2_x + 62 or car_2_x < car_5_x + 62 < car_2_x + 62 or car_2_x < car_5_x + 31 < car_2_x + 62) or (car_3_x < car_5_x < car_3_x + 62 or car_3_x < car_5_x + 62 < car_3_x + 62 or car_3_x < car_5_x + 31 < car_3_x + 62) or (car_4_x < car_5_x < car_4_x + 62 or car_4_x < car_5_x + 62 < car_4_x + 62 or car_4_x < car_5_x + 31 < car_4_x + 62) or (car_1_x < car_5_x < car_1_x + 62 or car_1_x < car_5_x + 62 < car_1_x + 62 or car_1_x < car_5_x + 31 < car_1_x + 62):
                car_5_x = random.randrange(100,700-62)

        if myx < 100 or myx+62 > 700:
            crash(myx+31,460)

        if car_1_y + 130 > 460 :
            if car_1_x < myx < car_1_x + 62 or car_1_x < myx + 62 < car_1_x + 62 or car_1_x < myx + 31 < car_1_x + 62 :
                crash(myx+31,460)
                
        if car_2_y + 130 > 460 :
            if car_2_x < myx < car_2_x + 62 or car_2_x < myx + 62 < car_2_x + 62 or car_2_x < myx + 31 < car_2_x + 62 :
                crash(myx+31,460)
                
        if car_3_y + 130 > 460 :
            if car_3_x < myx < car_3_x + 62 or car_3_x < myx + 62 < car_3_x + 62 or car_3_x < myx + 31 < car_3_x + 62 :
                crash(myx+31,460)
                
        if car_4_y + 130 > 460 :
            if car_4_x < myx < car_4_x + 62 or car_4_x < myx + 62 < car_4_x + 62 or car_4_x < myx + 31 < car_4_x + 62 :
                crash(myx+31,460)
                
        if car_5_y + 130 > 460 :
            if car_5_x < myx < car_5_x + 62 or car_5_x < myx + 62 < car_5_x + 62 or car_5_x < myx + 31 < car_5_x + 62 :
                crash(myx+31,460)
                
        if speed < 17:
            speed += 0.005

        pygame.display.update()
        clock.tick(60)

intro()
instruction()
carchoice()
gameloop()
quitgame()

