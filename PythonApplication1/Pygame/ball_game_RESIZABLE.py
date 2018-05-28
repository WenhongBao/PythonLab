import pygame,sys

pygame.init()
size = width,height = 600,400
speed = [1,1]
BLACK = 0,0,0
#change the screen resizeable
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("Pygame Ball")
ball = pygame.image.load("PYG02-ball.gif")
ballrect = ball.get_rect()
fps=300
fclock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed[0]=speed[0] if speed[0]==0 else(speed[0]-1)*int(speed[0]/abs(speed[0]))
            elif event.key==pygame.K_RIGHT:
                speed[0]=speed[0]+1 if speed[0]>0 else speed[0]-1
            elif event.key==pygame.K_UP:
                speed[1]=speed[1]+1 if speed[1]>0 else speed[1]-1
            elif event.key==pygame.K_DOWN:
                speed[1]=speed[1] if speed[1]==0 else(speed[1]-1)*int(speed[1]/abs(speed[1]))
        #set a key
        elif event.type==pygame.VIDEORESIZE:
            #rebuilt the size
            size=width,height=event.size[0],event.size[1]
            screen=pygame.display.set_mode(size,pygame.RESIZABLE)
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)
