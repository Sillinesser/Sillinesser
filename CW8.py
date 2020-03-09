# import pygame

# WHITE = (255, 255, 255)  
# ORANGE = (255, 150, 100)

# DISPLAY_WIDTH = 1200 
# DISPLAY_HEIGH = 600 

# pygame.init()
# gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGH))
# pygame.display.set_caption("My first game")
# # Loop until the user clicks the close button.
# done = False
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
  
# # -------- Main Program Loop -----------
# while not done:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             print("User asked to quit.")
# #         elif event.type == pygame.KEYDOWN:
# #             print("User pressed a key.")
# #         elif event.type == pygame.KEYUP:
# #             print("User let go of a key.")
# #         elif event.type == pygame.MOUSEBUTTONDOWN:
# #             print("User pressed a mouse button")
#   # --- Main event loop
#     for event in pygame.event.get(): # User did something
#         if event.type == pygame.QUIT: # If user clicked close
#             done = True # Flag that we are done so we exit this loop
    

  
#   # --- Game logic should go here
#   # --- Drawing code should go here
#   # First, clear the screen to white. Don't put other drawing commands
#   # above this, or they will be erased with this command.
#     gameDisplay.fill(ORANGE)
#   # --- Go ahead and update the screen with what we've drawn.
#     pygame.display.update()
#   # --- Limit to 60 frames per second
#     clock.tick(60)


# #######################################


# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()
# WHITE=(255,255,255)
# done = False
# clock = pygame.time.Clock()
# PI = 3.14
# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    #функції lines і aalines малюють ламані
    # лінії, а параметр Ttue означає замкнути ламані,
    # False не замикати
    # 
    # pygame.draw.lines(screen, WHITE, True, [[10, 10], [140, 70], [280, 20]], 2)
    # pygame.draw.aalines(screen, WHITE, False, [[10, 100], [140, 170], [280, 110]])
    
    # #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 7)
    # pygame.draw.line(screen, WHITE, [10, 50], [290, 35])

    # 
    # pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
    # #pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
    # pygame.draw.aalines(screen, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])
    
    #aaline згладжена лінія, товщина в цьому
    # випадку не задається
    # pygame.draw.ellipse(screen, WHITE, (10, 50, 50, 100))
   


    # pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
   


    # (100, 100) координати центра
    # 50 - радіус

    # pygame.draw.circle(screen, WHITE, (100, 100), 50,5)
    # # pygame.draw.circle(screen, WHITE, (200, 100), 50)


    # pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI/8)
    # pygame.draw.arc(screen, WHITE, (50, 30, 200, 150), PI, 2*PI, 3)


    # pygame.display.update()
    
#     import pygame

# pygame.init()

# gameDisplay=pygame.display.set_mode((400,300))

# pygame.display.set_caption("my first game")

# clock=pygame.time.Clock()

# crashed=False
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True

#         print(event)

#     pygame.display.update()

#     clock.tick(60)

# pygame.quit()
# #quit()



#pylint: disable=C0321 
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("My first game")
# #clock = pygame.time.Clock()

# done = False
# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    
#     pygame.draw.rect(screen, (255,0,0), [55, 50, 80, 55])
    
    
#     pygame.display.update()
#   #clock.tick(60)




############################################################################################
# import pygame
# pygame.init()
# display_height = 500
# display_width =300
# screen = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption("My first game")

# x=50
# y=50
# width=20
# height=30
# vol=5
# clock = pygame.time.Clock()
# Aqua = (0, 255, 255)
# Green = (0, 128, 0)
# Blue = (0, 0, 255)
# Purple = (128, 0, 128)
# a = Aqua
# run = True
# while run:
#     pygame.time.delay(10)
    
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             run=False

#     keys=pygame.key.get_pressed()
    
#     if keys[pygame.K_LEFT] and x>0:
#             x=x-vol
#             a=(200, 50, 30)
#     if keys[pygame.K_RIGHT] and x<(display_width-width):
#             x=x+vol
#             a=(120, 0, 0)
#     if keys[pygame.K_UP] and y>0:
#             y=y-vol
#             a=(0, 255, 30)
#     if keys[pygame.K_DOWN] and y<(display_height-height):
#             y=y+vol
#             a=(20, 30, 250)
#     ##################
    
    

#     #without trace 
#     screen.fill((0,0,0)) 
#     pygame.draw.rect(screen,a,(x,y,width,height))
#     pygame.display.update()
###########################################################################################################


# import pygame

# # Define some colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Call this function so the Pygame library can initialize itself
# pygame.init()
 
# # Create an 800x600 sized screen
# screen = pygame.display.set_mode([800, 600])
 
# # This sets the name of the window
# pygame.display.set_caption('Fly')
 
# clock = pygame.time.Clock()

# #обновляємо екран 
# pygame.display.update()
 
# # Set positions of graphics
# background_position = [0, 0]
 
# # Load and set up graphics.
# #background_image = pygame.image.load("saturn_family1.jpg").convert()
# player_image = pygame.image.load("D:\Delit\Ver.png").convert()

# #Якщо в зображення не має прозорого слою, то щоб його встановити,
# #необхідно використати метод set_colorkey() класу Surface:
# player_image.set_colorkey(BLACK)
 
# done = False
#  #########################################


#  #########################################
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True            
 
    
# # Get the current mouse position. This returns the position
#     # as a list of two numbers.
# #повертає поточну позицію мишки на екрані
#     player_position = pygame.mouse.get_pos()
#     x =player_position[0]
#     y =player_position[1]
 
#     # Copy image to screen:
# #копіює картинку на екран
#     screen.blit(player_image, [x, y])
    
# #обновляємо екран
#     pygame.display.flip()
#     pygame.display.update()
#     clock.tick(2000)


# pygame.quit()


import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("D:\Lectures\My_lect_Python\Game\+\player.png").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
#копіює картинку на екран
    screen.blit(player_image, [x, y])
 
#обновляємо екран
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()