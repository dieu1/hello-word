import pygame, sys
from pygame.locals import *
#khởi tạo pygame
pygame.init()

WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 300 # Chiều cao cửa sổ

#tạo màn hình hiển thị
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('game')
# Tạo sẵn các màu sắc
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

car_x = 0 # Hoành độ của xe
car_y = 0# Tung độ của xe
car_width = 50  # Chiều rộng xe
car_height = 50  # Chiều cao xe
car_speed = 5 # tóc độ của xe
carSurface = pygame.Surface((100, 50), SRCALPHA)
pygame.draw.polygon(carSurface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
pygame.draw.circle(carSurface, GREEN, (15, 40), 10)
pygame.draw.circle(carSurface, GREEN, (85, 40), 10)
#thêm hình ảnh cho game
img = pygame.image.load('minimal spotify cover.jpg')
img = pygame.transform.scale(img, (50, 70))
img_rect = img.get_rect(center = (0, 100))

up = right = left = down = False
   
   
#vòng lặp game
while True:
    #đặt màu nền trắng
    DISPLAYSURF.fill(WHITE)
    # thêm hình ảnh
    DISPLAYSURF.blit(img, (car_x, car_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # sự kiện ấn phím
    if event.type == KEYDOWN:
        if event.key == K_UP:
            up = True
        if event.key == K_DOWN:
            down = True
        if event.key == K_LEFT:
            left = True
        if event.key == K_RIGHT:
            right = True
    # sự kiện thả phím
    if event.type == KEYUP:
        if event.key == K_UP:
            up = False
        if event.key == K_DOWN:
            down = False
        if event.key == K_LEFT:
            left = False
        if event.key == K_RIGHT:
            right = False
    # di chuyển xe lên, xuống, trái, phải
    if up and car_y > 0:
        car_y -= car_speed
    if down and car_y < WINDOWHEIGHT - car_height:
        car_y += car_speed
    if left and car_x > 0:
        car_x -= car_speed
    if right and car_x < WINDOWWIDTH - car_width:
        car_x += car_speed


    pygame.display.update()
    fpsClock.tick(FPS)
