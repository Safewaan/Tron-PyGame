'''
Created on Jun 17, 2018

@author: Safwaan
'''
import pygame, sys
import time
from pygame.locals import *
from pygame.constants import *
from pip._vendor.requests.api import options
from __builtin__ import True
from pickle import TRUE
fpsClock = pygame.time.Clock()
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800,600))

winner=""

AI=0 


def mainmenu(winner, AI):
    '''mainmenu(winner) - Function that stores the parameter winner to later blit it on to the screen when the victor is decided. 
       When the code returns back to mainmenu(winner), the winner will be blitted near the bottom right of the screen.
       The function also displays a working main menu, which allows the users to learn more about the game and to of course, close the game as necessary.'''
    
    #Music
    music="On"
    
    #Colors
    selectcolor=(255,255,255)
    
    #Pictures for various menu options
    menu=pygame.image.load('Main Menu.jpg')
    menu=pygame.transform.scale(menu,(800,600))
    
    help=pygame.image.load('Help.jpg')
    help=pygame.transform.scale(help,(800,600))
    
    choice=pygame.image.load("Choice.jpg")
    choice=pygame.transform.scale(choice,(800,600))
    
    screentoblit=menu
    
    #Variables needed for line 
    x=100 #x of the line to choose 
    y=260 #y of the line to choose
    optionsx=0 #Variable to adjust for length of options word
    helpx=0 #variable to adjust 2nd x for help option
    choicex=0 #variable to adjust for length of the words 
    selection=0 #0=play, 1=help, 2=options, 3=quit
    choiceselection=0 #0=1 player, 1=2 player, 2=back
    
    helptest=False #True locks ability to move up and down, false unlocks ability to move around. Used for help menu.
    helpcheck=0
    choicetest=False #True if you are in the choice menu, vice versa
    
    #Music
    sound = True #True plays music, False mutes music
    pygame.mixer.music.load("Music.wav")
    pygame.mixer.music.play()
    
    #Text
    myfont=pygame.font.SysFont('Electrolize',33)
    textsurface = myfont.render("", False, selectcolor)
    winnertext= myfont.render(winner, False, selectcolor)
    musictext= myfont.render("On", False, selectcolor)
    
    tf=False
    while not tf:
        fpsClock.tick(60)
        screen.blit(screentoblit,(0,0)) #Blits all needed images/text
        screen.blit(textsurface, (100,600))
        screen.blit(winnertext, (400,550))
        screen.blit(musictext, (260, 350))
        
        pygame.draw.line(screen, selectcolor, (x,y), (x+125+optionsx-helpx+choicex,y), 5) #Draws line under "Play" when the game starts.
        
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                
                if (event.key == K_DOWN): #Moves menu choice down one
                    if helptest==False: #If you are not in help menu
                        if choicetest==False:
                            if selection!=3: #Prevents selection from going past quit
                                selection+=1
                                y+=65
                                if selection==2: #Extends line to for options
                                    optionsx=40
                                else:
                                    optionsx=0 #Shorten line for other choices
                        else:
                            if choiceselection!=2:
                                choiceselection+=1
                                y+=40
                                if choiceselection==2:
                                    choicex=-52
                                else:
                                    choicex= 55
                            
                                
                if (event.key == K_UP): #Moves menu choice up one
                    if helptest==False:
                        if choicetest==False:
                            if selection!=0:
                                selection-=1
                                y-=65
                                if selection==2:
                                    optionsx=110 #Extends line to cover length of the word "options"
                                else:
                                    optionsx=0 #Reverts to original
                        else:
                            if choiceselection!=0:
                                choiceselection-=1
                                y-=40
                                if choiceselection==2:
                                    choicex=-52
                                else:
                                    choicex= 55
                                
                if (event.key == K_RETURN):
                    if choicetest==False:
                        if selection==0: #Selecting Play
                            screentoblit=choice
                            x=18
                            y=372
                            choicex=55
                            choicetest=True
                            musictext= myfont.render("", False, selectcolor)
                        if selection==1: #Selecting Help
                            if helpcheck==0:
                                screentoblit=help
                                helptest = True 
                                x=35
                                y=550 
                                helpx=45 #Shortens line to cover length of the word "back"
                                helpcheck=1
                            elif helpcheck==1:
                                helpcheck=0
                                selection=0
                                helptest = False
                                screentoblit=menu
                                x=100
                                y=260
                                selection=0
                                helpx=0 #Reverts to original
                        if selection==2:
                            if music=="On":
                                music="Off"
                                pygame.mixer.music.pause()
                                musictext= myfont.render("Off", False, selectcolor)
                            elif music=="Off":
                                music="On"
                                pygame.mixer.music.unpause()
                                musictext= myfont.render("On", False, selectcolor)
                        if selection==3:
                            pygame.quit()
                            sys.exit(0)
                    else:
                        if choiceselection==0: #1 player
                            AI=1
                            return AI
                        elif choiceselection==1: #2 players
                            AI=0
                            return AI
                        elif choiceselection==2: #Return back to the main menu
                            if music=="On":
                                musictext= myfont.render("On", False, selectcolor)
                            else:
                                musictext= myfont.render("Off", False, selectcolor)
                            choicetest=False
                            screentoblit=menu
                            x=100
                            y=260
                            selection=0
                            choiceselection=0
                            choicex=0 #Reverts to original
                if (event.key == K_ESCAPE): #Closes game
                    pygame.quit()
                    sys.exit(0)
                                
        pygame.display.update()