import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font("SuperPixel-m2L8j.ttf", 90)
font3 = pygame.font.Font("SuperPixel-m2L8j.ttf", 80)
font2 = pygame.font.Font("ARCADECLASSIC.TTF", 30)
class ball:
    def __init__(self, x: int, y: int, l: int, hp: 100, max_hp: 100):
        self.x = x
        self.y = y
        self.l = l
        self.hp = hp
        self.max_hp = max_hp
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
    def draw(self, color: str):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.ellipse(screen, color, self.rect)
    def moveleft(self):
        self.x -=5
    def moveright(self):
        self.x += 5
    def borderleft(self):
        if self.rect.x <= 0:
            self.x = 0
    def borderright(self):
        if self.rect.x >= (800 - self.l):
            self.x = (800 - self.l)
    def stop(self, colx, moving1, moving2):
        if moving1 or moving2:
            self.x = colx
    def attack(self, damage):
        if self.hp > 0:
            self.hp -= damage
        else:
            self.hp = self.hp
    def heal(self, gain):
        if self.hp >= self.max_hp:
            self.hp = self.hp
        else:
            self.hp += gain

# ball 1
ball1 = ball(600, 200, 50, 100, 100)
ball1left = False
ball1right = False
ball1lose = False
ball1name = font2.render("Player 2", False, "White")
ball1namerect = ball1name.get_rect(topright = (785, 10))

# ball 2
ball2 = ball(150, 200, 50, 100, 100)
ball2left = False
ball2right = False
ball2lose = False
ball2name = font2.render("Player 1", False, "White")
ball2namerect = ball1name.get_rect(topleft = (15, 10))

Play = font3.render('Play', False, 'White')
Play_rect = Play.get_rect(center = (400, 200))


run = True
in_game = False
home = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if ball2.rect.colliderect(ball1.rect):
                    ball1.attack(5)
            if event.key == pygame.K_UP:
                if ball1.rect.colliderect(ball2.rect):
                    ball2.attack(5)
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Play_rect.collidepoint(mouse_pos):
                home = False
                in_game = True

    if ball1.hp <= 0:
        ball1lose = True
        in_game = False
    if ball2.hp <= 0:
        ball2lose = True
        in_game = False
    if home:
        screen.fill('cadetblue3')
        play_border = pygame.draw.rect(screen, "cadetblue3", Play_rect)
        screen.blit(Play, Play_rect)
    if in_game:
        # keys
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            ball2left = True
        else:
            ball2left = False
        if pressed[pygame.K_d]:
            ball2right = True
        else:
            ball2right = False
        if pressed[pygame.K_LEFT]:
            ball1left = True
        else:
            ball1left = False
        if pressed[pygame.K_RIGHT]:
            ball1right = True
        else:
            ball1right = False
        
        
        # movement
        if ball1left:
            ball1.moveleft()
        if ball1right:
            ball1.moveright()   
        if ball2left:
            ball2.moveleft()
        if ball2right:
            ball2.moveright()
        
        # border collisions
        if ball1.x <= 0:
            ball1.borderleft()
        if ball1.x >= 750:
            ball1.borderright()
        if ball2.x <= 0:
            ball2.borderleft()
        if ball2.x >= 750:
            ball2.borderright()
        screen.fill("black")
        sky = pygame.draw.rect(screen, "cadetblue3", (0, 0, 800, 400))
        borderwidth = 1
        screen.blit(ball1name, ball1namerect)
        screen.blit(ball2name, ball2namerect)
        ball1bar = pygame.draw.rect(screen, "red", (785 - ball1.hp, 40, ball1.hp, 16))
        border1 = pygame.draw.rect(screen, "black", (685, 40, 100, 16), 3)
        ball2bar = pygame.draw.rect(screen, "red", (15, 40, ball2.hp, 16))
        border = pygame.draw.rect(screen, "black", (15, 40, 100, 16), 3)
        # border2 = pygame.draw.rect(screen, 'black',)
        ground = pygame.draw.rect(screen, "chartreuse4", (0, (ball1.y + 50), 800, (800 - ball1.y)))
        ball1.draw("yellow")
        ball2.draw("green")
    elif home == False:
        screen.fill("cadetblue3")
        text = font.render("YOU LOSE!", False, "white")
        text_rect = text.get_rect(center=(400, 200))
        screen.blit(text, text_rect)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()