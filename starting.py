import pygame
import turtle
import random
import time

from main import *

pygame.init()

screen = pygame.display.set_mode((1200, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("CreepQuizz")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
Background_1 = pygame.image.load("BG1.png")
Background_2 = pygame.image.load("Rules.png")

# Play Button
class button:
    def __init__(self, color, x, y, width, height, text=""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(
                screen,
                outline,
                (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                0,
            )

        pygame.draw.rect(
            screen, self.color, (self.x, self.y, self.width, self.height), 0
        )

        if self.text != "":
            font = pygame.font.SysFont("comicsans", 60)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(
                text,
                (
                    self.x + (self.width / 2 - text.get_width() / 2),
                    self.y + (self.height / 2 - text.get_height() / 2),
                ),
            )

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True


def redrawindow():
    screen.blit(Background_1, (0, 0))
    playbutton.draw(screen, ())
    return


playbutton = button((16, 144, 84), 200, 400, 250, 100, "Play")
continueButton = button((16, 144, 84), 1000, 500, 100, 100, "Play")
