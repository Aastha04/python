import pygame
x=pygame.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
#print(x)
#Creating Window
screen_width=1000
screen_height=300
screen_caption="My First Snake GAme"
gameWindow=pygame.display.set_mode((1000,600))
pygame.display.set_caption(screen_caption)
exit_game=False
game_over=False
snake_X= 40
snake_Y=20
snake_size=10
# Game specific Variable
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            exit_game=True
        gameWindow.fill(white)
        pygame.display.update()
        gameWindow.fill(red)
        pygame.display.update()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              snake_X=snake_X+10
          if event.key == pygame.K_LEFT:
              print("you pressed left arrow key")
          if event.key == pygame.K_DOWN:
              print("you pressed down arrow key")
          if event.key == pygame.K_UP:
              print("you pressed up arrow key")
          pygame.quit()
quit()
