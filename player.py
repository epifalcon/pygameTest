import pygame
import collision

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, skin, position):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.x = position[0]
        self.y = position[1]
        
        self.health = 3
        self.jumped = False
        self.gravity = 0.25
        self.action = "standing"
        self.touchingGround = False
        self.animateCounter = 0

        self.skin = pygame.image.load('PlayerImages/'+skin+'.png').convert()
        self.colorkey = self.skin.get_at((1,1))
        self.skin.set_colorkey(self.colorkey)
        self.skinStanding = self.skin.subsurface((220,424),(340,565))
        self.skinWalking1 = self.skin.subsurface((345,424),(423,565))
        self.skinWalking2 = self.skin.subsurface((428,424),(522,565))
        self.skinWalking3 = self.skin.subsurface((524,424),(659,565))
        self.skinWalking4 = self.skin.subsurface((686,424),(775,565))
        self.skinWalking5 = self.skin.subsurface((775,424),(870,565))
        self.skinWalking6 = self.skin.subsurface((889,424),(1024,565))
        '''
        self.skinJumping1 = self.skin.subsurface((x,y),(x,y))
        self.skinJumping2 = self.skin.subsurface((x,y),(x,y))
        self.skinShooting1 = self.skin.subsurface((x,y),(x,y))
        self.skinShooting2 = self.skin.subsurface((x,y),(x,y))
        self.skinHit1 = self.skin.subsurface((x,y),(x,y))
        self.skinHit2 = self.skin.subsurface((x,y),(x,y))
        self.skinPickup1 = self.skin.subsurface((x,y),(x,y))
        self.skinPickup2 = self.skin.subsurface((x,y),(x,y))
        '''
        self.image = self.skinStanding
        self.rect = self.image.get_rect()
        self.rect = self.rect.mmove(self.x, self.y)

        self.walkCounter = 0

    def movement(self):
        if self.action == "ready":
            if not self.pressed_keys[K_SPACE]:
                self.jumped == False

            

