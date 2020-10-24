
import pygame
from math import sqrt



class Body(object):
    def __init__( self, xi, yi, vxi, vyi, radius, mass ):
        self.x = xi
        self.y = yi
        self.x_l = xi
        self.y_l = yi
        self.vx = vxi
        self.vy = vyi
        self.r = radius
        self.m = mass
        return
        
    def evolve( self, body_list ):
        force_sum = [0,0]
        for body in body_list:
            # mag of seperation vector
            mag_r = sqrt( (body.x_l - self.x_l)**2 + (body.y_l - self.y_l)**2)
            
            force_sum[0] -= 10e-11*body.m*(self.x_l - body.x_l)/mag_r**3
            force_sum[1] -= 10e-11*body.m*(self.y_l - body.y_l)/mag_r**3


        self.x += dt*self.vx
        self.y += dt*self.vy

        self.vx += dt*force_sum[0]
        self.vy += dt*force_sum[1]
        return
        
    def draw( self, game_window, WIDTH, HEIGHT ):
        # one earth to sun distance is 100 units
        pygame.draw.circle(game_window,(255,255,255), ( int( WIDTH/2 + (self.x - WIDTH/2)/1.4881e9 ), int(HEIGHT/2 + (self.y - HEIGHT/2)/1.4881e9) ), self.r)
        return

def time_evolve( body_list, dt ):
    for i in range(len(body_list)):
        body_list[i].evolve( body_list[:i] + body_list[i+1:] )

    for body in body_list:
        body.x_l = body.x
        body.y_l = body.y

    return

def draw_screen( body_list, WIDHT, HEIGHT ):
    # draw windows
    game_window.fill( (  0,  0,  0) )

    for body in body_list:
        body.draw(game_window, WIDTH, HEIGHT)

    
    pygame.display.update()
    return

pygame.init()
WIDTH = 800
HEIGHT = 500

body_list = []
body_list.append( Body( WIDTH/2,             HEIGHT/2, 0,-29785*5.972e24/2.09847e30,     10, 2.09847e30  ) )
body_list.append( Body( WIDTH/2 + 1.4881e11, HEIGHT/2, 0,29785, 1,  5.972e24    ) )
body_list.append( Body( WIDTH/2 + 2.1456e11, HEIGHT/2, 0,24785, 1,  6.39e23     ) )
body_list.append( Body( WIDTH/2 + 4.3456e10, HEIGHT/2, 0,47360, 1,  6.39e23     ) )
body_list.append( Body( WIDTH/2 + 1.0856e11, HEIGHT/2, 0,35025, 1,  4.867e24    ) )



dt = 3600

count = 0
game_window = pygame.display.set_mode((WIDTH,HEIGHT))

# gime window
exit_flag= False
play_flag = True
while not exit_flag:

    # restart animation if stopped
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        play_flag = True

    # close animation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_flag = True
    
    while play_flag:
        # stop game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            play_flag = False
            
        # close animation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True
                play_flag = False

        draw_screen( body_list, WIDTH, HEIGHT )
        count += 1
        time_evolve( body_list, dt )

pygame.quit()



            
