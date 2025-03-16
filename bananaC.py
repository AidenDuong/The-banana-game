from pygame import *
font.init()
#Class
class gamesprite():
    def __init__(self,width,height,pic,x,y):
        self.image = transform.scale(image.load(pic),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
class GameText():
    def __init__(self,x ,y ,text,color):
        self.color= color
        self.font = font1.render(text,True,self.color)
        self.x = x
        self.y = y
    def setText(self, text):
        self.font = font1.render(text,True,self.color)

    def update(self):
        window.blit(self.font, (self.x, self.y))
clock = time.Clock()
FPS = 50
click = 1
wait = 0
udcost1 = 50
udcost = 10
udcost2 = 100 
udcost3 = 1000 
clcikercost = 20
clcikercost1 = 100
vob = 0
BPS = 0
yellow = (218, 165, 32)
game = True
window = display.set_mode()
width, height = window.get_size()

#text
font1 = font.Font(None, 30)
scoretext = GameText(25,40,"Bananas: "+ str(vob),yellow)
scoretext1 = GameText(25,50,"Bananas per second: "+ str(BPS),yellow)
scoretext2 = GameText(25,height-70 - 130/4,"cost: "+ str(udcost),yellow)
scoretext3 = GameText(150,400,"cost: "+ str(udcost1),yellow)
scoretext4 = GameText(275,400,"cost: "+ str(udcost2),yellow)
scoretext5 = GameText(350,400,"cost: "+ str(udcost3),yellow)
scoretext6 = GameText(50,400,"cost: "+ str(clcikercost),yellow)
scoretext7 = GameText(400,35,"cost: "+ str(clcikercost1),yellow)

#Gamesspriiiiiiiiit
banana = gamesprite(200 * 2,75 * 2,"yipppe.png",width /2 - 200,height / 2 - 75)
upgrade = gamesprite(477/4,130/4,"bananaBoy.png",25,height -70)
upgrade1 = gamesprite(477/4,130/4,"bananaMan.png",150,height -70)
upgrade2 = gamesprite(477/4,130/4,"bananafarm.png",275,height -70)
upgrade3 = gamesprite(477/4,130/4,"bananafactory.png",350,height -70)
clicker1 = gamesprite(50,50,"cligrader.png",width,0)
clicker2 = gamesprite(50,50,"cligrader.png",500,85)

#Looooooooooooooooooooooooooooop
while game:
    for e in event.get():    
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = False
        if e.type == MOUSEBUTTONDOWN:
            x,y = e.pos
            if banana.rect.collidepoint(e.pos):
                print("touching",vob)
                vob += click
                scoretext.setText("Bananas: " + str(vob))
            if upgrade.rect.collidepoint(x,y) and vob >= udcost:
                print("stfu")
                vob -= udcost
                BPS += 1
                udcost *= 1.1
                udcost = int(udcost)
            if upgrade1.rect.collidepoint(x,y) and vob >= udcost1:
                print("stfu1")
                vob -= udcost1
                BPS += 5
                udcost1 *= 1.1
                udcost1 = int(udcost1)
            if upgrade2.rect.collidepoint(x,y) and vob >= udcost2:
                print("stfu1")
                vob -= udcost2
                BPS += 20
                udcost2 *= 1.1
                udcost2 = int(udcost2)
            if upgrade3.rect.collidepoint(x,y) and vob >= udcost3:
                print("stfu1")
                vob -= udcost3
                BPS += 100
                udcost3 *= 1.1
                udcost3 = int(udcost3)
            if clicker1.rect.collidepoint(x,y) and vob >= clcikercost:
                print("stfu1")
                vob -= clcikercost
                click *= 2
                clcikercost *= 9
                clcikercost = int(clcikercost)
            if clicker2.rect.collidepoint(x,y) and vob >= clcikercost1:
                print("stfu1")
                vob -= clcikercost1
                click *= 2
                clcikercost1 *= 10
                clcikercost1 = int(clcikercost1)
    wait += 1 
    if wait >= FPS:
        vob += BPS
        wait = 0
# The damn update
    bananaman = gamesprite(600,75,"banana.gif",200 ,200)
    scoretext7 = GameText(width -139,70,"cost: "+ str(clcikercost1),yellow)
    clicker2 = gamesprite(50,50,"cligrader.png",width - 50 ,0)
    scoretext6 = GameText(width -135,20,"cost: "+ str(clcikercost),yellow)
    clicker1 = gamesprite(50,50,"cligrader.png",width - 50,55)
    scoretext5 = GameText(400,height - 70 -130/4,"cost: "+ str(udcost3),yellow)
    upgrade3 = gamesprite(477/4,130/4,"bananafactory.png",400,height-70)
    scoretext4 = GameText(275,height-70 - 130/4,"cost: "+ str(udcost2),yellow)
    upgrade2 = gamesprite(477/4,130/4,"bananafarm.png",275,height-70)
    upgrade1 = gamesprite(477/4,130/4,"bananaMan.png",150,height-70)
    scoretext3 = GameText(150,height-70 - 130/4,"cost: "+ str(udcost1),yellow)
    scoretext2 = GameText(25,height-70 - 130/4,"cost: "+ str(udcost),yellow)
    scoretext1 = GameText(25,25,"Bananas per second: "+ str(BPS),yellow)
    scoretext = GameText(25,50,"Bananas:"+ str(vob),yellow)
    window.fill((253,253,150))
    clicker1.update()
    clicker2.update()
    upgrade.update()
    upgrade1.update()
    banana.update()
    scoretext.update()
    scoretext6.update()
    scoretext7.update()
    scoretext5.update()
    upgrade3.update()
    scoretext4.update()
    scoretext3.update()
    scoretext1.update()
    scoretext2.update()
    upgrade2.update()
    display.update()
    clock.tick(FPS)
