import pygame, sys
class Relsi:
      def __init__(self):
            self.relimage = pygame.image.load('relsi-2.png')
            self.rectRELimg = self.relimage.get_rect()
 
            self.relY1 = 0
            self.relX1 = 565
 
            self.relY2 = self.rectRELimg.height
            self.relX2 = 565

            self.movingUpSpeed = 5
            

            self.relimage1 = pygame.image.load('relsi-2.png')
            self.rectRELimg1 = self.relimage1.get_rect()
 
            self.relY3 = 0
            self.relX3 = 385
 
            self.relY4 = self.rectRELimg1.height
            self.relX4 = 385
         
      def update(self):
        self.relY1 += self.movingUpSpeed
        self.relY2 += self.movingUpSpeed
        if self.relY1 >= self.rectRELimg.height:
            self.relY1 = -self.rectRELimg.height + 8
        if self.relY2 >= self.rectRELimg.height:
            self.relY2 = -self.rectRELimg.height + 8

        self.relY3 += self.movingUpSpeed
        self.relY4 += self.movingUpSpeed
        if self.relY3 >= self.rectRELimg1.height:
            self.relY3 = -self.rectRELimg1.height + 8
        if self.relY4 >= self.rectRELimg1.height:
            self.relY4 = -self.rectRELimg1.height + 8
             
      def render(self):
         DISPLAYSURF.blit(self.relimage, (self.relX1, self.relY1))
         DISPLAYSURF.blit(self.relimage, (self.relX2, self.relY2))

         DISPLAYSURF.blit(self.relimage1, (self.relX3, self.relY3))
         DISPLAYSURF.blit(self.relimage1, (self.relX4, self.relY4))

DISPLAYSURF = pygame.display.set_mode((1000,600))
DISPLAYSURF.fill((61, 12, 2))
