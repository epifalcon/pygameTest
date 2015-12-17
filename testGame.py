#!/usr/bin/python

import pygame

class TestGame():
    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.BLUE = (0,0,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)

        self.done = False
        self.clock = pygame.time.Clock()

        pygame.init()
        # Developed for 16x9 at 640x360, scale everything from there
        size = (640, 360)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("testGame")
        self.screen.fill(self.BLACK)

        self.font = pygame.font.Font(None, 12)

        self.x = 50
        self.y = 250
        self.backx = -50
        self.backy = -360
        self.xRate = 0
        self.yRate = 0
        self.RATE = 2

        self.backgroundPosition = [0,0]
        self.backgroundImage = pygame.image.load("levels/LevelTest2.png").convert()

    def run(self):
        print "Running"
        while not self.done:
            text = "NOTHING"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        text = "UP"
                        self.yRate = -self.RATE
                    if event.key == pygame.K_DOWN:
                        text = "DOWN"
                        self.yRate = self.RATE
                    if event.key == pygame.K_RIGHT:
                        text = "RIGHT"
                        self.xRate = self.RATE
                    if event.key == pygame.K_LEFT:
                        text = "LEFT"
                        self.xRate = -self.RATE
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        if self.yRate < 0:
                            self.yRate = 0
                    if event.key == pygame.K_DOWN:
                        if self.yRate > 0:
                            self.yRate = 0
                    if event.key == pygame.K_RIGHT:
                        if self.xRate > 0:
                            self.xRate = 0
                    if event.key == pygame.K_LEFT:
                        if self.xRate < 0:
                            self.xRate = 0

            self.backx = self.backx - int(self.xRate/2)
            self.backy = self.backy - int(self.yRate/2)
            self.screen.blit(self.backgroundImage, [self.backx, self.backy])
            self.x = self.x + self.xRate
            self.y = self.y + self.yRate
            pygame.draw.circle(self.screen, self.WHITE, [self.x, self.y], 5)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    testGame = TestGame()
    testGame.run()
