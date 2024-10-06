import pygame, sys, random, math
from pygame.locals import *
#bắt đầu pygame
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
# độ dài cửa sổ
chieu_dai_x = 500
chieu_cao_y = 500
# hệ mầu
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
# thiết lập cửa sổ
DISPLAYSURF = pygame.display.set_mode((chieu_dai_x, chieu_cao_y))
pygame.display.set_caption('cai gi do')
# tạo hình tròn
circle_speed = 5
circle_height = 50 # chiều cao circle
circle_width = 50 # chiều rộng circle
circle_x = 255
circle_y = 255
surface_1 = pygame.Surface((50, 50), SRCALPHA)
pygame.draw.circle(surface_1, RED, (25, 20), 10)

# tạo vật tấn công hình vuông
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(*self.random_start_position(), 30, 30)
        self.lifetime = random.randint(100, 300)
        self.speed = 2

    def random_start_position(self):
        """Sinh vị trí ngẫu nhiên cho kẻ địch ở ngoài màn hình""" 
        side = random.choice(['top', 'bottom', 'left', 'right'])
        if side == 'top':
            return random.randint(0, chieu_dai_x - 30), 0
        elif side == 'bottom':
            return random.randint(0, chieu_dai_x - 30), chieu_cao_y - 30
        elif side == 'left':
            return 0,  random.randint(0, chieu_cao_y - 30)
        else:
            return chieu_dai_x - 30, random.randint(0, chieu_cao_y - 30)
        
    def move_towards_player(self, player_x, player_y):
        """Di chuyển kẻ địch về phía người chơi"""
        dx = player_x - self.rect.centerx
        dy = player_y - self.rect.centery
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def update(self):
        """Cập nhật trạng thái kẻ địch (giảm thời gian sống)"""
        self.lifetime -= 1

    def is_alive(self):
        """Kiểm tra nếu kẻ địch vẫn còn sống (còn thời gian sống)"""
        return self.lifetime > 0


# Danh sách kẻ địch
enemies = [Enemy() for _ in range(3)]  # Tạo ra n kẻ địch ban đầu

# di chuyển hình tròn
up = down = left = right = False
def move_circle():
    global circle_x, circle_y, up, down, left, right  # Sử dụng biến toàn cục cho tọa độ và điều khiển
    # Kiểm tra để đảm bảo cirle không vượt quá lề trái hoặc phải
    if up and circle_y > 0:
        circle_y -= circle_speed
    if down and circle_y < chieu_cao_y - circle_height:
        circle_y += circle_speed
    if left and circle_x > 0:
        circle_x -= circle_speed
    if right and circle_x < chieu_dai_x - circle_width:
        circle_x += circle_speed

running = True
while running:

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(surface_1, (circle_x, circle_y))

    # Vẽ và di chuyển kẻ địch
    for enemy in enemies:
        if enemy.is_alive():  # Chỉ vẽ kẻ địch khi nó còn sống
            enemy.move_towards_player(circle_x, circle_y)
            pygame.draw.rect(DISPLAYSURF, BLACK, enemy.rect)
        enemy.update()  # Giảm thời gian sống của kẻ địch

        # kiểm tra va chạm của kẻ địch
        if math.hypot(circle_x - enemy.rect.centerx, circle_y - enemy.rect.centery) < 35:
            print('GAME OVER')
            running = False
    
    # Xử lý kẻ địch sau khi biến mất
    for i, enemy in enumerate(enemies):
        if not enemy.is_alive():  # Nếu kẻ địch hết thời gian sống
            enemies[i] = Enemy()  # Tạo lại kẻ địch mới

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
    
    move_circle()

    # Cập nhật màn hình
    pygame.display.update()
    # tóc độ khung hình
    fpsClock.tick(FPS)


