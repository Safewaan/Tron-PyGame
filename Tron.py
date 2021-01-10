'''
Created on Jun 12, 2018

@author: Safwaan
'''
#Imports
import sys, time
from pygame.locals import *
from pygame.constants import *
from Functions import *
import random
import time
import os

#Starts main menu
AI=mainmenu(winner, AI)

#Initializations 
fpsClock = pygame.time.Clock()
pygame.init()
pygame.joystick.init()

#Font
myfont=pygame.font.SysFont('Electrolize',33)

#Player scores (Used to test for when to stop game function from looping)
p1s=0
p2s=0
winner=""

def game(p1s,p2s):
    ''' game(p1s,p2s) - Function that returns the parameters p1s,p2s. p1s and p2s are then used to determine the victor of the game. 
        Every time collision is made, p1s or p2s will go up by one. When either is at 3, the code will stop looping and call upon the mainmenu(winner) function. (line 200)
        The function also displays various visuals such as the trails, the score and the game itself. 
        It also takes in key input using pygame to move around the player's cars.'''
    #Settings for the screen
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption ('bRON')
    background=pygame.image.load('background.jpg')
    background=pygame.transform.scale(background,(800,600))
    
    #Player 1 variables
    x1=200
    y1=300
    movex1=0
    movey1=0
    direction1='R.png'
    trailcolor1=(38,95,225)
    listplayer1=[]
    
    initialspeed1x=4 #Gets player 1 moving when the game starts
    initialspeed2x=-4 #Gets player 2 moving when the game starts
    
    count=0 #Helps with AI 
    
    def player1(x1,y1):
        '''player1(x1,y1) - Function that uses the parameters x1,y1 to blit the sprite of player 1's car to the x1 and y1 location.
           Every time the car moves, x1 and y1 will change accordingly. This helps to determine collisions with trails, enemy trails, and borders.'''
        player1sprite=pygame.image.load(os.path.join("Player1Sprites",direction1))
        screen.blit(player1sprite, (x1,y1))
        
    #Player 2 variables
    x2=600
    y2=300
    movex2=0
    movey2=0
    direction2='RedL.png'
    trailcolor2=(214,0,3)                                       
    listplayer2=[]
    
    def player2(x2,y2):
        '''player2(x2,y2) - Function that uses the parameters x2,y2 to blit the sprite of player 2's car to the x2 and y2 location.
           Every time the car moves, x2 and y2 will change accordingly. This helps to determine collisions with trails, enemy trails, and borders.'''
        player2sprite=pygame.image.load(os.path.join("Player2Sprites",direction2))
        screen.blit(player2sprite, (x2,y2))
       
    done=False

    while not done:
        fpsClock.tick(60)
        screen.blit(background,(0,0))
        
        #Draws the borders
        pygame.draw.line(screen, (4,205,255), (0,0), (0,600), 10)
        pygame.draw.line(screen, (4,205,255), (0,0), (800,0), 10)
        pygame.draw.line(screen, (4,205,255), (800,0), (800,600), 10)
        pygame.draw.line(screen, (4,205,255), (0,600), (800,600), 10)
        
        #Limits trails for players
        listplayer1.append((x1,y1))
        if len(listplayer1)>50: #Keeps the line limited to 50 boxes
            del listplayer1[0]
        listplayer2.append((x2,y2))
        if len(listplayer2)>50: #Same for player 2
            del listplayer2[0]
            
        
        #Prints the trails for the players
        for i in range(len(listplayer1)):
            pygame.draw.rect(screen, trailcolor1, (listplayer1[i][0]+5, listplayer1[i][1]+10, 5, 5))
            pygame.draw.rect(screen, trailcolor2, (listplayer2[i][0]+5, listplayer2[i][1]+10, 5, 5))
            
        #Prints score (Put after trail so trail does not overlap score)
        p1s=str(p1s)
        p2s=str(p2s)
        
        p1ssurface = myfont.render(p1s, False, (255, 255, 255))
        p2ssurface = myfont.render(p2s, False, (255, 255, 255))
        
        screen.blit(p1ssurface,(385,80))
        screen.blit(p2ssurface,(415,80))
        
        p1s=int(p1s)
        p2s=int(p2s)
        
        #Conditionals for when collision occurs
        for i in range(len(listplayer2)-1):    
            if x1==listplayer2[i][0] and y1==listplayer2[i][1]: #Tests to see if player 1 runs into player 2's line
                p2s+=1
                return p1s,p2s
            elif x2==listplayer1[i][0] and y2==listplayer1[i][1]: #Tests to see if player 2 runs into player 1's line
                p1s+=1
                return p1s,p2s
            elif x1==listplayer1[i][0] and y1==listplayer1[i][1]: #Tests to see if player 1 runs into own line
                if len(listplayer1)!=1:
                    p2s+=1
                    return p1s,p2s
            elif x2==listplayer2[i][0] and y2==listplayer2[i][1]: #Tests to see if player 2 runs into own line
                if len(listplayer2)!=1:
                    p1s+=1
                    return p1s,p2s
            elif y1==0 or y1==600 or x1==0 or x1==800: #Tests to see if player 1 drives out of the boundary 
                p2s+=1
                return p1s,p2s
            elif y2==0 or y2==600 or x2==0 or x2==800: #Tests to see if player 2 drives out of the boundary
                p1s+=1
                return p1s,p2s
            else:
                player1(x1,y1)
                player2(x2,y2)
        
        #Key inputs
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    done = True
                    pygame.quit()
                    sys.exit(0)
                #Player 1 inputs
                if (event.key == K_d):
                    movex1 = 4
                    movey1 = 0
                    initialspeed1x=0
                    direction1='R.png'
                if (event.key == K_a):
                    movex1 = -4
                    movey1 = 0
                    initialspeed1x=0
                    direction1='L.png'
                if (event.key == K_s):
                    movey1 = 4
                    movex1 = 0
                    initialspeed1x=0
                    direction1='D.png'
                if (event.key == K_w):
                    movey1 = -4
                    movex1 = 0
                    initialspeed1x=0
                    direction1='U.png'
                
                #Player 2 input
                if AI==0:
                    if (event.key == K_RIGHT):
                        movex2 = 4
                        movey2 = 0
                        initialspeed2x=0
                        direction2='redR.png'
                    if (event.key == K_LEFT):
                        movex2 = -4
                        movey2 = 0
                        initialspeed2x=0
                        direction2='redL.png'
                    if (event.key == K_DOWN):
                        movey2 = 4
                        movex2 = 0
                        initialspeed2x=0
                        direction2='redD.png'
                    if (event.key == K_UP):
                        movey2 = -4
                        movex2 = 0
                        initialspeed2x=0
                        direction2='redU.png'
                        
        if AI==1:
            randnum=random.randint(0,3)
            count+=random.randint(0,2)
            if count>=10: #provides small delay before moves
                count=0
                if movex2==0: #Stops the bot from annoyingly running into itself but not it's own trail
                    if randnum==0 or y2==599 or y2==1 or x2==799 or x2==1:
                        movex2 = 4
                        movey2 = 0
                        initialspeed2x=0
                        direction2='redR.png'
                if movex2==0:
                    if randnum==1 or y2==599 or y2==1 or x2==799 or x2==1:
                        movex2 = -4
                        movey2 = 0
                        initialspeed2x=0
                        direction2='redL.png'
                if movey2==0:
                    if randnum==2:
                        movey2 = 4
                        movex2 = 0
                        initialspeed2x=0
                        direction2='redD.png'
                if movey2==0:
                    if randnum==3:
                        movey2 = -4
                        movex2 = 0
                        initialspeed2x=0
                        direction2='redU.png'
                            
        
        x1+=movex1
        x1+=initialspeed1x 
        y1+=movey1
        
        x2+=movex2
        x2+=initialspeed2x
        y2+=movey2
        
        pygame.display.update()

while True:
    if p1s==3 or p2s==3: #When the game is over, this code will determine who the winner is then return the main menu.
        if p1s==3:
            winner="Winner: Blue Player"
        if p2s==3:
            winner="Winner: Red Player"
        AI = mainmenu(winner, AI)
        p1s=0
        p2s=0
    else:
        p1s,p2s=game(p1s,p2s) #Else, it will continue as normal