import random
import pygame

pygame.init() 


screenW = 1024
screenH = 706
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Vikings&Rednecks")
icon = pygame.image.load("lib_images/VikingIcon.png")
pygame.display.set_icon(icon)



# Background

backgroundImg = pygame.image.load("./lib_images/background.png")

# Players

class Player():
    
    standingViking = [pygame.image.load("./lib_images/viking_standing_1.png"),pygame.image.load("./lib_images/viking_standing_2.png")]
    walkingViking = [pygame.image.load("./lib_images/viking_standing_1.png"),pygame.image.load("./lib_images/viking_step_1.png"),pygame.image.load("./lib_images/viking_standing_1.png"),pygame.image.load("./lib_images/viking_step_2.png")]
    deadViking = pygame.image.load("./lib_images/viking_death.png")
    
    standingRedneck = [pygame.image.load("./lib_images/redneck_standing_1.png"),pygame.image.load("./lib_images/redneck_standing_2.png")]
    walkingRedneck = [pygame.image.load("./lib_images/redneck_standing_1.png"),pygame.image.load("./lib_images/redneck_step_1.png"),pygame.image.load("./lib_images/redneck_standing_1.png"),pygame.image.load("./lib_images/redneck_step_2.png")]
    deadRedneck = pygame.image.load("./lib_images/redneck_death.png")
    
    isWalk = False
    isJump = False
    facing = ""
    
    hitbox = None
    pos = [] 
    Type = ""
    
    speedx = 7.5
    dirnx = 0.0
    speedy = 5.4
    dirny = 1.0
    dead = False
    
    Berzerk = False  # Powerup
    Redneck = False  # Powerup
    
    def __init__(self, arr, char):
        self.lives = 3 
        self.pos = arr
        self.hitbox = pygame.Rect(self.pos,(75,85))
        self.Type = char 
        
    
    def move(self, event): 
        
        global fire_state, reload_timer
        
        if self.Type == "viking":
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_a:
                    self.dirnx = -1.0
                    self.isWalk = True
                    self.facing = "left"
                    
                if event.key == pygame.K_d:
                    self.dirnx = 1.0
                    self.isWalk = True 
                    self.facing = "right"
                    
                if event.key == pygame.K_w and not self.isJump:
                    self.dirny = -2.9
                    self.isJump = True
                    
                    
                if event.key == pygame.K_e and self.Redneck and fire_state =="ready":
                    bulletLst.append(Bullet(self.facing, self.pos))
                    reload_timer = pygame.time.get_ticks()
                    fire_state = "reload"
                
                  
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_a and self.dirnx < 0: 
                    self.dirnx = 0.0  
                    self.isWalk = False
                if event.key == pygame.K_d and self.dirnx > 0:
                    self.dirnx = 0.0 
                    self.isWalk = False
            
        if self.Type == "redneck":
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT:
                    self.dirnx = -1.0
                    self.isWalk = True
                    self.facing = "left"
                            
                if event.key == pygame.K_RIGHT:
                    self.dirnx = 1.0
                    self.isWalk = True 
                    self.facing = "right"
                            
                if event.key == pygame.K_UP and not self.isJump:
                    self.dirny = -2.9
                    self.isJump = True
                            
                if event.key == pygame.K_l and self.Redneck and fire_state =="ready":
                    bulletLst.append(Bullet(self.facing, self.pos))
                    reload_timer = pygame.time.get_ticks()
                    fire_state = "reload"
                            
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT and self.dirnx  < 0: 
                    self.dirnx = 0.0  
                    self.isWalk = False
                if event.key == pygame.K_RIGHT and self.dirnx  > 0:
                    self.dirnx = 0.0 
                    self.isWalk = False  
                    
    
    def Draw(self,screen): 
    
        self.pos[0] = self.pos[0]+self.dirnx*self.speedx
        self.pos[1] = self.pos[1]+self.dirny*self.speedy
        self.hitbox.left = self.pos[0]
        self.hitbox.top = self.pos[1]
        
        if self.isWalk and self.facing == "left": 
            self.dirnx -= 0.005
        if self.isWalk and self.facing == "right":
            self.dirnx += 0.005
       
        if self.Type == "viking":
            
            if self.dirny < 1.5:
                
                self.dirny+= 0.2
                if self.dead: 
                    screen.blit(self.deadViking, self.pos)
                else:
                    screen.blit(self.standingViking[0], self.pos)
            elif self.dead: 
                screen.blit(self.deadViking, self.pos)
            elif self.isWalk: 
                screen.blit(self.walkingViking[FrameCount//8],self.pos)
            else:   
                screen.blit(self.standingViking[FrameCount//15], self.pos)
            
            if self.Berzerk:
                screen.blit(PowerUp.berzerkImg,(self.pos[0]+55,self.pos[1]+20))
            if self.Redneck: 
                if self.facing == "left":
                    screen.blit(PowerUp.redneckImg[self.facing],(self.pos[0]-15, self.pos[1]+25))
                else: 
                    screen.blit(PowerUp.redneckImg[self.facing],(self.pos[0]+60, self.pos[1]+25))
                    
        if self.Type == "redneck":
            if self.dirny < 1.5:
                
                self.dirny+= 0.2
                if self.dead: 
                    screen.blit(self.deadRedneck, self.pos)
                else:
                    screen.blit(self.standingRedneck[0], self.pos)
                    
            elif self.dead: 
                screen.blit(self.deadRedneck, self.pos)                    
            elif self.isWalk: 
                screen.blit(self.walkingRedneck[FrameCount//8],self.pos)
            else:   
                screen.blit(self.standingRedneck[FrameCount//15], self.pos)
            
            if self.Berzerk:
                screen.blit(PowerUp.berzerkImg,(self.pos[0]+60,self.pos[1]+17))
            if self.Redneck: 
                if self.facing == "left":
                    screen.blit(PowerUp.redneckImg[self.facing],(self.pos[0]-15, self.pos[1]+20))
                else: 
                    screen.blit(PowerUp.redneckImg[self.facing],(self.pos[0]+50, self.pos[1]+20))
        
    
    def PowerUp(self,pwrUp):
        if pwrUp == "berzerk": 
            self.Berzerk = True 
        elif pwrUp == "redneck":
            self.Redneck = True
      
    def Death(self): 
        self.dirny =  -3.5
        self.dead = True 
    
# PowerUps

class PowerUp(object):
    
    redneckImg = {"left": pygame.image.load("./lib_images/redneck_left.png"), "right": pygame.image.load("./lib_images/redneck_right.png")}
    redneckImg["left"] =  pygame.transform.scale(redneckImg["left"], (50,50)) 
    redneckImg["right"] = pygame.transform.scale(redneckImg["right"], (50,50))
    
    
    berzerkImg = pygame.image.load("./lib_images/berzerk.png")
    
    
    berzerkImg = pygame.transform.scale(berzerkImg, (50,50))
    
    SpawnLocations = [(500, 375), (70, 460), (930, 6), (954, 460)]
    SpawnLocation = ()
    
    hitbox = None
    isActive = False 
    
    Types = ["berzerk", "redneck"]
    Type = ""
    
    def __init__(self):
        
        self.isActive = True 
        s = random.randrange(0,4)
        self.SpawnLocation = self.SpawnLocations[s]
        t = random.randrange(0,2)
        
        if self.Types[t] == "berzerk":
            self.Type = "berzerk"
            self.hitbox = pygame.Rect(self.SpawnLocation, (50,50)) 
        if self.Types[t] == "redneck":
            self.Type = "redneck"
            self.hitbox = pygame.Rect(self.SpawnLocation, (60,60)) 
    
    def Draw(self, screen): 
        
        if self.Type == "berzerk":
            screen.blit(self.berzerkImg, self.SpawnLocation)
        elif self.Type == "redneck":
            screen.blit(self.redneckImg["right"], self.SpawnLocation)
    
    def PowerUpTimer(self, char, start_timer): 
        timer = pygame.time.get_ticks() 
        
        if (timer-start_timer)/1000 > 8:
            char.Berzerk = False 
            char.Redneck = False
            return PowerUp()
        else:
            return None
            
class Bullet(object):
    bulletImg = {1:pygame.image.load("./lib_images/bullet_right.png"),-1: pygame.image.load("./lib_images/bullet_left.png")}
    
    speed = 15
    dirnx = 0.0
    pos = []
    hitbox = None 
    
    isActive = False
    
    def __init__(self, facing, playerPos): 
        if facing == "right":
            self.dirnx = 1.0
        elif facing == "left":
            self.dirnx = -1.0
            
        self.pos = [playerPos[0]+45,playerPos[1]+40]
        
        self.isActive = True 
     
    def Draw(self, screen): 
        self.pos = [self.pos[0]+self.dirnx*self.speed,self.pos[1]]
        self.hitbox = pygame.Rect(self.pos, (4,10))
        if self.pos[0] < -200 or self.pos[0] > screenW+200:
            self.isActive = False
        
        screen.blit(self.bulletImg[self.dirnx], self.pos)
         
         
class Terrain(object):
    TerrainLocations = {0:(0,642), 1:(620, 642), 2:(0,546),3:(846,546),4:(330,450),5:(105,354),6:(844,354),7:(0,258), 8:(0,162),9:(355,66)}
    loc = ()
    TerrainSizes = {0:(405, 20),1:(405,20), 2:(173,1),3:(175,1),4:(362,1),5:(15,1),6:(175,1),7:(720,1), 8:(158,1),9:(668,1)}
    size = ()
    
    rectangle = None
    
    def __init__(self,i):
        self.size = self.TerrainSizes[i] 
        self.loc = self.TerrainLocations[i]
        self.rectangle = pygame.Rect(self.loc,self.size) 
        
        
# Fonts 

FontBig = pygame.font.SysFont("ubunumono", 60)
BeginText = FontBig.render("Press Any Key To Begin", True, (0,0,0))
BeginTextRect = BeginText.get_rect(center=(screenW/2,screenH/2))

# Functions 

def Respawn(): 
        
        bulletLst.clear()
        obj = PowerUp()
        char1 = Player([250, 520], "viking")
        char2 = Player([610, 520], "redneck")        
        return char1, char2, obj
        
def RedrawWindow(screen):
    
    screen.blit(backgroundImg, (0,0))
    
def TerrainCollision(ter, char): 
    global isJump
    
    if (ter.rectangle).colliderect(char.hitbox) and not char.pos[1]+85 > ter.rectangle.top+10  and not (char.dirny < 1) and not char.dead:
            char.pos[1] = (ter.rectangle).top-90   
            char.isJump = False

def isCollision(obj1, obj2):
    return obj1.hitbox.colliderect(obj2.hitbox)
    

def playerCollision(char1, char2): 
    if not char1.dead and not char2.dead:
        if abs(char1.dirnx) > abs(char2.dirnx): 
            if char1.hitbox.collidepoint(char2.hitbox.midleft): 
                char2.pos[0] = char1.hitbox.midright[0]
            
            if char1.hitbox.collidepoint(char2.hitbox.midright):
                char2.pos[0] = char1.hitbox.midleft[0]-80
        
        elif abs(char2.dirnx) > abs(char1.dirnx): 
            playerCollision(char2, char1)
            
    if char1.hitbox.collidepoint(char2.hitbox.midbottom): 
            char2.pos[1] = char1.hitbox.midtop[1]-80
            char2.isJump = False     
    if char2.hitbox.collidepoint(char1.hitbox.midbottom): 
            char1.pos[1] = char2.hitbox.midtop[1]-80
            char1.isJump = False             
    

# Variables 

global FrameCount, bulletLst, fire_state, reload_timer
FrameCount = 0
bulletLst = []
fire_state = "ready"
reload_timer = 0

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
ragnar = Player([250, 520], "viking")
lennie = Player([610, 520], "redneck")
PwrObj = PowerUp()
Terrain = [Terrain(i) for i in range(10)]

# PreGameText 

RedrawWindow(screen)
screen.blit(BeginText, BeginTextRect)
pygame.display.update()

flag = True 
while flag: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            flag = False
            

# GameWindow

flag = True 
while flag: 
    
    # Background and Framerate S
    
    clock.tick(30)
  
    
    if FrameCount+1 >= 30:
        FrameCount = 0
    else: 
        FrameCount +=1
        
    RedrawWindow(screen)
   
   # Collisions 
   
    for ter in Terrain:
        TerrainCollision(ter,ragnar)
        TerrainCollision(ter,lennie)
    
    if isCollision(ragnar,PwrObj) and PwrObj.isActive: 
        ragnar.PowerUp(PwrObj.Type)
        PwrObj.isActive = False
        start_timer = pygame.time.get_ticks()
        
    if isCollision(lennie,PwrObj) and PwrObj.isActive: 
        lennie.PowerUp(PwrObj.Type)
        PwrObj.isActive = False
        start_timer = pygame.time.get_ticks()
        
    for bul in bulletLst:
        if isCollision(ragnar, bul) and not ragnar.Redneck and not ragnar.dead:
            ragnar.Death()
            bul.isActive = False
        if isCollision(lennie, bul) and not lennie.Redneck and not lennie.dead:
            lennie.Death()
            bul.isActive = False
    
    if isCollision(lennie, ragnar) and (not lennie.dead and not ragnar.dead):
        if ragnar.Berzerk: 
            lennie.Death()
        elif lennie.Berzerk:
            ragnar.Death()
          
        playerCollision(lennie, ragnar)
        
   # Event Management
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        ragnar.move(event)
        lennie.move(event)
    

    ticks = pygame.time.get_ticks()
    if (ticks - reload_timer)/1000 > 1.5:
        fire_state = "ready"        
        
    
    # Rendering
    if PwrObj.isActive:
        PwrObj.Draw(screen)
    elif ragnar.Berzerk or ragnar.Redneck: 
        ObjTemp = PwrObj.PowerUpTimer(ragnar, start_timer)
        if isinstance(ObjTemp,PowerUp):
            PwrObj = ObjTemp
    elif lennie.Berzerk or lennie.Redneck:
        ObjTemp = PwrObj.PowerUpTimer(lennie, start_timer)
        if isinstance(ObjTemp,PowerUp):
            PwrObj = ObjTemp
            
    for bul in bulletLst:
        if bul.isActive:
            bul.Draw(screen)
        else: 
            bulletLst.pop(bulletLst.index(bul))
    
    if ragnar.pos[1] > screenH+40 or lennie.pos[1] > screenH+40:
        lennie, ragnar, PwrObj = Respawn()
           
    ragnar.Draw(screen) 
    lennie.Draw(screen)
    
    pygame.display.update()
    
pygame.quit()

