# File Name:   Drawable.py
# Purpose:     Abstract class that allows us to create drawable objects
#              with different shapes, at a given location (x, y)
# Last update: Surabhi Rajbhandari sr3523

import pygame
from abc import ABC, abstractmethod
import random

class Drawable(ABC):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getLoc(self):
        return (self.__x, self.__y)

    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]

    @abstractmethod
    def draw(self, surface):
        pass


class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, (self.getLoc()[0], self.getLoc()[1], self.__width, self.__height))


class Snowflake(Drawable):
    def __init__(self, x):
        super().__init__(x, 0)

    def draw(self, surface):
      x, y = self.getLoc()

    # First draw black outline slightly offset
      for offset in [-1, 1]:
          pygame.draw.line(surface, (0, 0, 0), (x - 5 + offset, y), (x + 5 + offset, y))
          pygame.draw.line(surface, (0, 0, 0), (x, y - 5 + offset), (x, y + 5 + offset))
          pygame.draw.line(surface, (0, 0, 0), (x - 5 + offset, y - 5 + offset), (x + 5 + offset, y + 5 + offset))
          pygame.draw.line(surface, (0, 0, 0), (x - 5 + offset, y + 5 - offset), (x + 5 + offset, y - 5 + offset))

    # Then draw white snowflake on top
      pygame.draw.line(surface, (255, 255, 255), (x - 5, y), (x + 5, y))
      pygame.draw.line(surface, (255, 255, 255), (x, y - 5), (x, y + 5))
      pygame.draw.line(surface, (255, 255, 255), (x - 5, y - 5), (x + 5, y + 5))
      pygame.draw.line(surface, (255, 255, 255), (x - 5, y + 5), (x + 5, y - 5))


    def move(self):
        self.setLoc((self.getLoc()[0], self.getLoc()[1] + 1))

    @staticmethod
    def spawn():
        x = random.randint(0, 800)  # Adjust this range based on your window dimensions
        return Snowflake(x)

class Snowman(Drawable):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, surface):
      x, y = self.getLoc()
    
    # Body (bottom to top)
      pygame.draw.circle(surface, (0, 0, 0), (x, y + 60), 30)  # Outline
      pygame.draw.circle(surface, (255, 255, 255), (x, y + 60), 28)  # Fill

      pygame.draw.circle(surface, (0, 0, 0), (x, y + 30), 20)
      pygame.draw.circle(surface, (255, 255, 255), (x, y + 30), 18)

      pygame.draw.circle(surface, (0, 0, 0), (x, y), 15)
      pygame.draw.circle(surface, (255, 255, 255), (x, y), 13)

    # Eyes
      pygame.draw.circle(surface, (0, 0, 0), (x - 5, y - 5), 2)
      pygame.draw.circle(surface, (0, 0, 0), (x + 5, y - 5), 2)

    # Nose (carrot)
      pygame.draw.polygon(surface, (255, 165, 0), [(x, y), (x + 10, y + 2), (x, y + 5)])

    # Hat
      pygame.draw.rect(surface, (0, 0, 0), (x - 10, y - 25, 20, 10))  # brim
      pygame.draw.rect(surface, (0, 0, 0), (x - 5, y - 40, 10, 15))   # top



class Basket(Drawable):
    def __init__(self, x, y, width=60, height=20, color=(139, 69, 19)):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
        self.__speed = 10

    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, (*self.getLoc(), self.__width, self.__height))

    def move_left(self):
        x, y = self.getLoc()
        self.setLoc((max(0, x - self.__speed), y))

    def move_right(self, screen_width):
        x, y = self.getLoc()
        self.setLoc((min(screen_width - self.__width, x + self.__speed), y))

    def get_rect(self):
        x, y = self.getLoc()
        return pygame.Rect(x, y, self.__width, self.__height)

