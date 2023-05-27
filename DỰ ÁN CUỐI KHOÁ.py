#**PLEASE WAIT A FEW SECONDS FOR THE PROGRAM TO RUN!**#
#**LAM ON DOI VAI GIAY DE CHUONG TRINH KHOI DONG!**#
import pygame
import random
import turtle
import time

from starting import *
from main import *

def exit_of_choice():
    syns.exit(0)

play_music("Music 2.wav")
run = False
run2 = False
running = True
while running:
    redrawindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if playbutton.isOver(pos):
                run = True
    while run:
        screen.blit(Background_2,(0,0))
        continueButton.draw(screen,())
        pygame.display.update()
            
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.isOver(pos):
                    setup_turtle()
                    state.reset_timer()
                    draw_timer()
                    data = read_data() + generate_math_questions()
                    random.shuffle(data)
                    for question in data:
                        ask_question(question)
                    pygame.quit()
                    quit()