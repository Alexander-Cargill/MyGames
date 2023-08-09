import pygame 
import random
import math
pygame.init() 

screen = pygame.display.set_mode((800, 600)) 
icon = pygame.image.load("alien-1.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Space Invaders")

backgroundImg = pygame.image.load("background.png")
invaderImg = pygame.image.load("Invader-1.png")
bulletImg = pygame.image.load("bullet.png")
explosionImg = pygame.image.load("explosion.png")

playerImg = pygame.image.load("Player.png")

playerImg = pygame.transform.scale(playerImg,[70, 54 ])
invaderImg = pygame.transform.scale(invaderImg, [70, 54])
explosionImg = pygame.transform.scale(explosionImg, [70,70])


# bullet
 
bulletX = 0 
bulletY = 480
bulletX_change = 0 
bulletY_change = 1
bullet_state = "ready"

def fire_bullet(x,y): 
   global bullet_state
   bullet_state = "fire"
   screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY,bulletX, bulletY):
   
   distance = math.sqrt(math.pow((enemyX +10) - bulletX, 2) + math.pow((enemyY+10)-bulletY, 2))
   if 0 < distance < 27:
      return True
   
   else: 
      return False

class Player():
   
   playerX = 370 
   playerY = 480
   dirnx = 0    

   def __init__(self): 
      pass

   def move(self):
      
      player.playerX += self.dirnx*0.4
      
      if self.playerX > 730: 
         self.playerX = 730 
      if self.playerX < 0: 
         self.playerX = 0
      
      screen.blit(playerImg, [self.playerX, 480])
   
class invader():
   pos = [0, 0] 
   isAlive = False
   direction = 1
   
   def __init__(self): 
      self.pos = [10, 10] 
      self.isAlive = True 
      screen.blit(invaderImg, self.pos)
      
   
   def move(self):
      self.pos[0] += self.direction*0.4
      if self.pos[0] < 5 or self.pos[0] > 730:
         self.direction *= -1
         self.pos[1] += 50
      screen.blit(invaderImg, self.pos)
   
   def __del__(self):
      Explosions.append(explosion(self.pos))
      
class explosion(): 
   ExPos = [] 
   start_timer = 0
   
   def __init__(self, arr):
      self.start_timer = pygame.time.get_ticks() 
      screen.blit(explosionImg, arr)
      self.ExPos = [arr[0],arr[1]]
      
      

global Explosions, ticks
Explosions = []
player = Player()
print(isinstance(player, Player), "player")
inv = invader()
print(isinstance(inv, invader), "invader") 
score = 0
running = True  
while running:
   
   screen.fill((40,40,40))
   #screen.blit(backgroundImg,[0,0])
   ticks = pygame.time.get_ticks()
   
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
         if event.key == pygame.K_SPACE and bullet_state== "ready": 
            fire_bullet(player.playerX, player.playerY)
            bulletX = player.playerX   
            
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_a and player.dirnx == -1:
            player.dirnx = 0
         if event.key == pygame.K_d and player.dirnx == 1:
            player.dirnx = 0 
         
        
   if bullet_state is "fire": 
      fire_bullet(bulletX, bulletY)
      bulletY -= bulletY_change
      if bulletY < 0: 
         bullet_state = "ready"
         bulletY = 480
   
   player.move()
   
   if inv.isAlive:
      inv.move()
      
      for exp in Explosions: 
         screen.blit(explosionImg, exp.ExPos)
         if (ticks - exp.start_timer)/1000 > 1: 
            Explosions.pop(Explosions.index(exp))
            del exp
   
     
   if isCollision(inv.pos[0], inv.pos[1], bulletX,bulletY):
      del inv
      bullet_state = "ready"
      bulletY = 480
      score += 1 
      print(score)
      
      inv = invader()
   
   pygame.display.update()
         
pygame.quit()