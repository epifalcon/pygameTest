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
        self.screen_width = 640
        self.screen_height = 360
        size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("testGame")
        self.screen.fill(self.BLACK)

        self.font = pygame.font.Font(None, 12)

        # Add some music
        pygame.mixer.music.load('sounds/All_The_Pretty_Little_Horses_lyrics.ogg')
        pygame.mixer.music.play(-1)

        # Assume player is 40x60
        self.player = pygame.image.load('playerImages/player.png').convert()
        self.player.set_colorkey(self.player.get_at((0, 0)))
        self.x = self.screen_width/2 - 20
        self.y = self.screen_height - 60 - 60
        self.backx = -50
        self.backy = -360
        self.xRate = 0
        self.yRate = 0
        self.RATE = 1
        self.gravity = 3
        self.jump_rate = 4

        self.backgroundPosition = [0,0]
        self.backgroundImage = pygame.image.load("levels/LevelTest2.png").convert()
        self.ground = pygame.Rect(0, self.screen_height - 60, self.screen_width, 100)


    def run(self):
        print "Running"
        while not self.done:
            text = "NOTHING"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                    if event.key == pygame.K_d:
                        text = "RIGHT"
                        self.xRate = self.RATE
                    if event.key == pygame.K_a:
                        text = "LEFT"
                        self.xRate = -self.RATE
                    if event.key == pygame.K_SPACE:
                        self.yRate = -self.jump_rate
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        if self.xRate > 0:
                            self.xRate = 0
                    if event.key == pygame.K_a:
                        if self.xRate < 0:
                            self.xRate = 0

            self.backx = self.backx - self.xRate
            if (self.backy - self.yRate) <= (self.y + 60):
                self.backy = self.backy - self.yRate
            self.screen.blit(self.backgroundImage, [self.backx, self.backy])
            self.ground = self.ground.move(-self.xRate, -self.yRate)
            self.screen.blit(self.player, [self.x, self.y])
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    testGame = TestGame()
    testGame.run()
