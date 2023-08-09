import pygame 
import math

pygame.init() 


screen = pygame.display.set_mode((800, 600)) 
icon = pygame.image.load("alien-1.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")

invaderImg = pygame.image.load("Invader-1.png")
bulletImg = pygame.image.load("bullets.png")
explosionImg = pygame.image.load("explosion.png")
backgroundImg = pygame.image.load("background.png")

playerImg = pygame.image.load("Player.png")

playerImg = pygame.transform.scale(playerImg,[70, 54 ])
invaderImg = pygame.transform.scale(invaderImg, [70, 54])
bulletImg = pygame.transform.scale(bulletImg, [50, 54])
explosionImg = pygame.transform.scale(explosionImg, [70,70])
backgroundImg = pygame.transform.scale(backgroundImg, [800,300])

# TEXT
FontBig = pygame.font.SysFont("ubuntumono", 72)
LvlUp = FontBig.render("LEVEL UP", True, [255,255,255])
GameOver = FontBig.render("Game Over",True,[255,255,255])


def isCollision(InvPosX, InvPosY, BulPosX, BulPosY): 
   distance1 = math.sqrt((InvPosX-BulPosX+5)**2+(InvPosY-BulPosY)**2)  
   distance2 = math.sqrt((InvPosX-BulPosX+50)**2+(InvPosY-BulPosY)**2)  
   if 0<distance1<30 or 0<distance2<30: 
      return True 
   else: 
      return False 
   

class player():
   
   playerX = 370 
   playerY = 480
   dirnx = 0    
   playerSpeed = 6
   
   def __init__(self): 
      pass

   def move(self):
      
      player.playerX += player.dirnx*self.playerSpeed
      
      if player.playerX > 730: 
         player.playerX = 730
      if player.playerX < 0: 
         player.playerX = 0
         
      screen.blit(playerImg,[self.playerX, self.playerY]) 
   

class invader: 
   
   pos = [0, 0] 
   direction = 1
   speed = 1.2
   
   def __init__(self, i):
      if i < 12:
         self.pos = [10 + 63*i, 10]
      else:
         i = i-12
         self.pos = [10 + 63*i, 60]
         self.direction = -1
         
   
   def move(self):
      self.pos[0] += self.direction*self.speed
      if self.pos[0] < 0 or self.pos[0] > 740:
         self.direction *= -1
         self.pos[1] += 50
      screen.blit(invaderImg, inv.pos) 
     
   def Explode(self):
      Explosions.append(explosion(self.pos)) 
   
   
class explosion(): 
   ExPos = [] 
   start_timer = 0
   
   def __init__(self, arr):
      self.start_timer = pygame.time.get_ticks() 
      screen.blit(explosionImg, arr)
      self.ExPos = [arr[0],arr[1]] 

class bullet: 
   isActive = False
   pos = [] 
   bullet_speed = 5
   
   def __init__(self, x, y): 
      self.pos = [x+10, y-50]
      self.isActive = True
       
   def move(self): 
      
      self.pos[1] -= self.bullet_speed
      screen.blit(bulletImg, self.pos)
      if self.pos[1] < - 50:
         self.isActive = False
           
global Explosions, ticks
Explosions = []
bulletLst = [] 
invaderLst = [invader(i) for i in range(24)]
player = player()
reload_timer = 0
fire_state = "ready"
reload_time = 0.4
score = 0

level_timer = pygame.time.get_ticks()
running = True  
while running:

   screen.fill([0,0,0])
   screen.blit(backgroundImg, [0,300])
   ticks = pygame.time.get_ticks()
   
   if len(invaderLst) == 0: 
      screen.fill((0,0,0))
      screen.blit(backgroundImg, [0,300])
      text_rect = LvlUp.get_rect(center=(400,300))
      screen.blit(LvlUp, text_rect)
      pygame.display.update()
      Explosions.clear()
      invaderLst = [invader(i) for i in range(24)]
      invader.speed += 0.4
      if reload_time  > 0.58:
         reload_time -= 0.11
      else: 
         bullet.bullet_speed += 0.15
         
      pygame.time.delay(2000)
      
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False  
      if event.type == pygame.KEYDOWN: 
         if event.key == pygame.K_a:
            player.dirnx = -1 
         if event.key == pygame.K_d:
            player.dirnx = 1 
         if event.key == pygame.K_ESCAPE:
            running = False
         if event.key == pygame.K_SPACE and fire_state=="ready": 
            bul = bullet(player.playerX, player.playerY)
            bulletLst.append(bul)
            reload_timer = pygame.time.get_ticks()
            fire_state = "reloading"
            
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_a and player.dirnx == -1:
            player.dirnx = 0
         if event.key == pygame.K_d and player.dirnx == 1:
            player.dirnx = 0
            
   if (ticks-reload_timer)/1000 > reload_time: 
      fire_state = "ready"
            
   player.move()
   
   for exp in Explosions:
      screen.blit(explosionImg, exp.ExPos)
      if (ticks - exp.start_timer)/1000 > 3: 
         Explosions.pop(Explosions.index(exp))
   
   for inv in invaderLst:  
         inv.move()
            
   for i,c in enumerate(bulletLst): 
      if c.isActive:
         c.move()
      else: 
         bulletLst.pop(i)
         
   for i in invaderLst:
      for k in bulletLst: 
         if isCollision(i.pos[0],i.pos[1],k.pos[0],k.pos[1]):
            invaderLst.pop(invaderLst.index(i))
            i.Explode() 
            bulletLst.pop(bulletLst.index(k))
            score += 1
            print(score)
            
      if isCollision(i.pos[0],i.pos[1], player.playerX, player.playerY):
            ticks = pygame.time.get_ticks()
            print(round((ticks-level_timer)/1000,3))
            screen.fill((0,0,0))
            GameOver_rect = GameOver.get_rect(center=(400,300))
            Score = FontBig.render(f"{score}", True, [255,255,255])
            score_rect = Score.get_rect(center = (400, 400))
            screen.blit(Score, score_rect)
            screen.blit(GameOver, GameOver_rect) 
            pygame.display.update()
            pygame.time.delay(2000)
            running = False
            
   pygame.display.update()


pygame.quit()