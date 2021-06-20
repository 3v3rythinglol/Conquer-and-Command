import pygame
pygame.init()

wn = pygame.display.set_mode((900, 900))
pygame.display.set_caption('conquer and command')

menuB = pygame.image.load('re/menu.png')
endcardB = pygame.image.load('re/endcard2.png')
gameB = pygame.image.load('re/background.png')
shopB = pygame.image.load('re/shopB.png')
nickfab = pygame.image.load('re/NickFab.png')
uselessT = pygame.image.load('re/uselessT.png')
nick = pygame.image.load('re/nick.png')

endcardy = 0
endcardmove = 0
money = 0
nickc = 0
nickfabc = 0
nickfabcd = 0
nickadd = 0
nickfabl = []
nikl = []
run = True
menu = True
game = False
endcard = False
shop = False
shopcd = False
shopcd2 = False
nickfabp = False

arial = pygame.font.SysFont("arial", 50)
arial15 = pygame.font.SysFont("arial", 15)
money_ = arial15.render(str(money), 1, (0, 0, 0))
start_ = arial.render("START", 1, (0, 0, 0))
quit_ = arial.render("QUIT", 1, (0, 0, 0))
schlecht_ = arial15.render("(schlechte Lebensentscheidung)", 1, (0, 0, 0))

class nikfab():
    def __init__(self, nfx, nfy):
        self.nfx = nfx
        self.nfy = nfy
    def draw(self, wn):
        wn.blit(nickfab, (self.nfx, self.nfy))

class nik():
    def __init__(self, nx, wn):
        self.nx = nx
    def draw(self, wn):
        wn.blit(nick, (self.nx, 80))

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while menu:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                run = False

        wn.fill((255, 255, 255))

        keys = pygame.key.get_pressed()

        wn.blit(menuB, (0, 0))
        pygame.draw.rect(wn, (255, 0, 0), (200, 500, 500, 80))
        if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[1] < 580:
            pygame.draw.rect(wn, (255, 255, 0), (200, 500, 500, 80))
            if pygame.mouse.get_pressed()[0]:
                menu = False
                game = True
        wn.blit(start_, (370, 510))
        pygame.draw.rect(wn, (255, 0, 0), (200, 650, 500, 80))
        if pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 700 and pygame.mouse.get_pos()[1] > 650 and pygame.mouse.get_pos()[1] < 730:
            pygame.draw.rect(wn, (255, 255, 0), (200, 650, 500, 80))
            if pygame.mouse.get_pressed()[0]:
                menu = False
                run = False
        wn.blit(quit_, (370, 660))
        wn.blit(schlecht_, (488, 680))
        wn.blit(nick, (100, 100))

        pygame.display.update()

    while game:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        wn.blit(gameB, (0, 0))

        keys = pygame.key.get_pressed()

        pygame.draw.rect(wn, (30, 30, 30), (350, 650, 200, 200))

        for nickfa in nickfabl:
            nickfa.draw(wn)

        if nickfabp == True:
            wn.blit(nickfab, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
            if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1] < 560 and pygame.mouse.get_pos()[1] > 0:
                nickfabl.append(nikfab(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                nickfabp = False
                nickfabc += 1
            if keys[pygame.K_e]:
                nickfabp = False
                money += 100

        for nic in nikl:
            nic.draw(wn)

        nickfabcd += 1
        if nickfabcd > 299:
            nickfabcd = 0
            nickadd = 1 * nickfabc
            while nickadd > 0:
                nickadd -= 1
                nickc += 1
                nikl.append(nik(pygame.mouse.get_pos()[0]))


        #shop
        if keys[pygame.K_e] and shopcd2 == False:
            shopcd = True
        if shopcd == True and not keys[pygame.K_e]:
            shop = True
        if pygame.mouse.get_pos()[0] > 830 and pygame.mouse.get_pos()[0] < 880 and pygame.mouse.get_pos()[1] > 560 and pygame.mouse.get_pos()[1] < 600 and pygame.mouse.get_pressed()[0]:
            shop = False
            shopcd = False
        if shop == True and keys[pygame.K_e] and shopcd == True:
            shopcd2 = True
            shop = False
            shopcd = False
        if shopcd2 == True and not keys[pygame.K_e]:
            shopcd2 = False

        if shop:
            wn.blit(shopB, (0, 0))
            pygame.draw.rect(wn, (255, 0, 0), (40, 640, 60, 60))
            if money > 999:
                pygame.draw.rect(wn, (0, 255, 0), (40, 640, 60, 60))
                if pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[1] > 640 and pygame.mouse.get_pos()[0] < 100 and pygame.mouse.get_pos()[1] < 700 and pygame.mouse.get_pressed()[0]:
                    money -= 1000
            wn.blit(uselessT, (50, 650))
            pygame.draw.rect(wn, (255, 0, 0), (140, 640, 60, 60))
            if money > 99:
                pygame.draw.rect(wn, (0, 255, 0), (140, 640, 60, 60))
                if pygame.mouse.get_pos()[0] > 140 and pygame.mouse.get_pos()[1] > 640 and pygame.mouse.get_pos()[0] < 200 and pygame.mouse.get_pos()[1] < 700 and pygame.mouse.get_pressed()[0]:
                    nickfabp = True
                    money -= 100
                    shop = False
                    shopcd2 = False
                    shopcd = False
            wn.blit(nickfab, (150, 650))

        # money
        money += 1
        money_ = arial15.render(str(money) + "$", 1, (0, 0, 0))
        wn.blit(money_, (800, 30))
        nickc_ = arial15.render(str(nickc), 1, (0, 0, 0))
        wn.blit(nickc_, (800, 50))

        pygame.display.update()

        if nickc > 100:
            game = False
            endcard = True

    while endcard:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endcard = False

        wn.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        wn.blit(endcardB, (0, endcardy))

        endcardmove += 1
        if endcardmove > 400 and endcardy > -900:
            endcardy -= 0.75

        pygame.display.update()

pygame.QUIT