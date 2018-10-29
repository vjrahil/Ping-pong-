import pygame
from pygame.locals import *    #importing the locals library from pygame module
import time


chartreuse  =          (127,255,0)              #all the colours used in program
blue        =          (0,0,255)
red         =          (255,0,0)
white       =          (245,245,245)
black       =          (0,0,0)
orange      =          (255,127,80)
green       =	       (154,205,50)
yellow      =          (255,255,0)


class PingPong(object):                               #ping_pong class initialize
    
    def __init__(self, screensize):

        self.screensize = screensize

        self.centerx = int(screensize[0]*0.5)    #initializing the ping_pong position initially at the game start
        self.centery = int(screensize[1]*0.5)
        

        self.radius = 8
    
        self.rect = pygame.Rect(self.centerx-self.radius,       
                                self.centery-self.radius,
                                self.radius*2, self.radius*2)

        self.color = orange

        self.direction = [1,1]               #initial direction defined

        self.speedx = 3.8                     #specifying the ping_pong speed
        self.speedy = 6

        self.hit_edge_left = False         #initially assigning them to be false 
        self.hit_edge_right = False

    def update(self, player_paddle, computer_paddle):

        self.centerx += self.direction[0]*self.speedx
        self.centery += self.direction[1]*self.speedy

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:                                #checking that the ping_pong doesnt go out of the screen 
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1]-1:
            self.direction[1] = -1

        if self.rect.right >= self.screensize[0]-1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True

        if self.rect.colliderect(player_paddle.rect):#this part checks to change the direction of ping_pong if it hit th paddle
            self.direction[0] = -1
            pygame.mixer.music.load("pong.wav")
            pygame.mixer.music.play(1) 
        if self.rect.colliderect(computer_paddle.rect):
            self.direction[0] = 1
            pygame.mixer.music.load("pong.wav")
            pygame.mixer.music.play(1) 

    def do_it(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)    #creating the ping_pong
        pygame.draw.circle(screen, orange, self.rect.center, self.radius, 1)       #creating the black boundary around the ping_pong

    def reset(self):
        
        self.centerx = int(self.screensize[0]*0.5)    #initializing the ping_pong position initially at the game start(calling them again)
        self.centery = int(self.screensize[1]*0.5)

        
        self.hit_edge_left = False          #initially assigning them to be false (calling them again)
        self.hit_edge_right = False

        if(score1==5 or score2==5):
            self.speedx = self.speedx + .2        #increasing speed of ping_pong after 5 points scored


class ComputerPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = 5
        self.centery = int(screensize[1]*0.5)

        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5), self.width, self.height)

        self.color = black

        self.speed = 5.8

    def update(self, ping_pong):                                       
        if ping_pong.rect.top < self.rect.top:                        #condition for movement of ai paddle by comparing the ping_pong ordinate and the top of the ai paddle
            self.centery -= self.speed
        elif ping_pong.rect.bottom > self.rect.bottom:
            self.centery += self.speed

        self.rect.center = (self.centerx, self.centery)

    def do_it(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)     #creating the ai paddle
        pygame.draw.rect(screen, white, self.rect, 1)        #creating the black boundary around the paddle
        
class PlayerPaddle(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = screensize[0]-5
        self.centery = int(screensize[1]*0.5)

        self.height = 100
        self.width = 10

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5), self.width, self.height)

        self.color = red

        self.speed = 5.7
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1

    def do_it(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)      #creating the player paddle
        pygame.draw.rect(screen, white, self.rect, 1)         #creating the black boundary around the paddle

def ping_pong_table():
        pygame.draw.line(screen,white,((screensize[0]/2),0),(screensize[0]/2,screensize[1]),2)

        pygame.draw.rect(screen,white,((0,0),(screensize[0],screensize[1])),5)

def score_2(score):
    font = pygame.font.Font("foo.ttf",20)
    text = font.render("SCORE :" + str(" ") + str(score),True, chartreuse)
    text1= font.render("COMPUTER", True, chartreuse)
    screen.blit(text1,[120,30])
    screen.blit(text,[120,60])

def score_1(score):
    font = pygame.font.Font("foo.ttf",20)
    text = font.render("SCORE :" + str(" ") + str(score),True, chartreuse)
    text1= font.render("PLAYER", True, chartreuse)
    screen.blit(text1,[450,30])
    screen.blit(text,[450,60])


def text_objects(text,color):                                   
    font = pygame.font.Font("lexo.ttf",50)
    textsurface = font.render(text,True,color)
    return textsurface, textsurface.get_rect()

def message_to_screen(message,color):
        font = pygame.font.Font("lexo.ttf",50)
        textsurf, textrect = text_objects(message,color)
        textrect.center = (screensize[0]/2),(screensize[1]/2)
        screen.blit(textsurf,textrect)

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("PING PONG!")
    global screen
    global screensize
    screensize = (640,480)              
    screen = pygame.display.set_mode(screensize)  #creating the screen
    clock = pygame.time.Clock()  
    ping_pong = PingPong(screensize)     
    computer_paddle = ComputerPaddle(screensize)
    player_paddle = PlayerPaddle(screensize)
    global score1
    score1=0
    global score2
    score2=0
    running = True

    while running:
        clock.tick(64)                     # used for limiting  the FPS
        

        #event handling phase
        for event in pygame.event.get():      #checking condition (if running = false then the program should quit) 
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN:      # initializing the player paddle controls
                if event.key == K_UP :
                    player_paddle.direction = -1
                elif event.key == K_DOWN :
                    player_paddle.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP  and player_paddle.direction == -1:
                    player_paddle.direction = 0
                elif event.key == K_DOWN and player_paddle.direction == 1:
                    player_paddle.direction = 0
        score_2(score2)
        score_1(score1)
        computer_paddle.update(ping_pong)             #object updating phase
        ping_pong_table()
        player_paddle.update()
        ping_pong.update(player_paddle, computer_paddle)

        if ping_pong.hit_edge_left:  #make some text on the screen over everything else saying you lost/won, and then exit on keypress
            score1+=1
            pygame.mixer.music.load("score.wav")
            pygame.mixer.music.play(1)
            if (score1==11):
                print ('YOU WON')     
            ping_pong.reset()
        elif ping_pong.hit_edge_right:
            score2+=1
            pygame.mixer.music.load("score.wav")
            pygame.mixer.music.play(1)
            if (score2==11):                  
                print ('YOU lOST')
            ping_pong.reset()
                
        if score1==11 or score2==11:
            pygame.mixer.music.load("win.wav")
            pygame.mixer.music.play(1)
            running = False

        screen.fill(blue)                  #screen color
        ping_pong_table()                  #calling the side boundaries in the main function
        computer_paddle.do_it(screen)
        player_paddle.do_it(screen)
        ping_pong.do_it(screen)
        score_2(score2)
        score_1(score1)
        pygame.display.update()
    if score1==11:
        message_to_screen("YOU WON",yellow)
        pygame.display.update()
        time.sleep(4)
    elif score2==11:
        message_to_screen("YOU LOST",yellow)
        pygame.display.update()
        time.sleep(4)
    
    
    pygame.quit()

if __name__== '__main__':
    main()
