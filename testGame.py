#!/usr/local/bin/python

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
        size = (700, 500)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("testGame")
        self.screen.fill(self.WHITE)

        self.font = pygame.font.Font(None, 12)

        self.x = 50
        self.y = 50
        self.xRate = 0
        self.yRate = 0
        self.RATE = 1

    def run(self):
        print "Running"
        while not self.done:
            text = "NOTHING"
            self.screen.fill(self.WHITE)
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
                        self.yRate = 0
                    if event.key == pygame.K_DOWN:
                        self.yRate = 0
                    if event.key == pygame.K_RIGHT:
                        if self.xRate > 0:
                            self.xRate = 0
                    if event.key == pygame.K_LEFT:
                        if self.xRate < 0:
                            self.xRate = 0

            text = self.font.render(text, True, self.BLACK) # (Text, aliased, color)
            self.screen.blit(text, [10,10])
            self.x = self.x + self.xRate
            self.y = self.y + self.yRate
            pygame.draw.rect(self.screen, self.BLUE, [self.x,self.y,20,20])
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    testGame = TestGame()
    testGame.run()
