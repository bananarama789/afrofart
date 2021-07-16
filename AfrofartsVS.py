import pygame
pygame.init

xsize = 683
ysize = 384

window = pygame.display.set_mode((xsize, ysize))
pygame.display.set_caption("afrofart")

m = 1
g = 0
w = 30
h = 80
v = 10
x = 0
y = 500 - h

jump = False
jumpCount = 10
crouch = False
hold = True
back = False

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
Y = (255,255,0)
C = (0,255,255)
V = (255,0,255)
W = (255,255,255)
b = (0,0,0)
run = True

fpms = 20

while True:
    yborder = ysize - h
    pygame.time.delay(fpms)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x -= v

    if keys[pygame.K_RIGHT] and x < xsize - w:
        x += v

    if keys[pygame.K_UP] and y > 0:
        jump = True

    if keys[pygame.K_DOWN]:
       crouch = True
    else:
        crouch = False

    if keys[pygame.K_SPACE]:
        jump = True
        
    if y <= ysize - h and jump == True:
        if crouch == True:
            g = 0.1
        else:
            g = 0.3
        y -= (jumpCount * abs(jumpCount)) * g
        jumpCount -= 1.2
        
    else:
        y -= y - yborder
        jump = False
        jumpCount = 10
    
    if crouch == True:
        back = True
        h = 50
        v = 5
        if hold == True:
            y += 40
            hold = False
        
    else:
        h = 80
        v = 10
        hold = True
        if back == True:
            y -= 40
            back = False

    window.fill(b)
    
    pygame.draw.rect(window, C, (x, y, w, h))
    pygame.draw.rect(window, (220,181,80), (x, y, w, w))


    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    window.fill(b)
    
    pygame.draw.rect(window, C, (x, y, w, h))
    pygame.draw.rect(window, (220,181,80), (x, y, w, w))

    pygame.display.update()