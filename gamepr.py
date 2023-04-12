import pygame
from pygame.locals import *

# Эта функция упрощает загрузку изображений
def img(filename):
    return pygame.image.load(f'images/{filename}')

clock = pygame.time.Clock()  # Это часы на будущее, чтобы регулировать смену кадров движения привидения

pygame.init()
screen = pygame.display.set_mode((1099, 669))
pygame.display.set_caption("proga")
icon = img('Ghost-64.webp')
pygame.display.set_icon(icon)

# АНИМАЦИЯ И ДВИЖЕНИЕ ГГ

walk_right = [
    img('player_right/player_right1.png'),
    img('player_right/player_right2.png')
]  # список из подключенных картинок привидения, идущего направо
walk_left = [
    img('player_left/player_left1.png'),
    img('player_left/player_left2.png')
]  # список из подключенных картинок привидения, идущего налево

player_anim_count = 0  # счетчик-индекс для изображений в списке анимаций игрока
player_speed = 10  # это будем отнимать и прибавлять к координатам по х, тем самым регулируя скорость игрок1
player_x = 150  # координаты игрока по х
player_y = 540  # координаты игрока по y. Чем больше координаты, тем НИЖЕ ИГРОК. Чем меньше координаты, тем игрок ВЫШЕ.

is_jump = False  # переменная для отслеживания прыжка
jump_count = 10  # количество позиций, на которое мы будем поднимать игрока при прыжке (высота прыжка)

player_lives = 5  # количество жизней игрока. Если игрок все жизни игра заканчивается

# АНИМАЦИЯ И ДВИЖЕНИЕ ВРАГОВ

enemy_land_left = [
    img('enemy_land_left/enemy_land_left1.png'),
    img('enemy_land_left/enemy_land_left2.png')
]

animation_speed = 10
animation_stage = 0

enemy_land_anim_count = 0
enemy_land_x = 600
enemy_land_y = 500

enemy_sky_left = [
    img('enemy_sky_left/enemy_sky_left1.png'),
    img('enemy_sky_left/enemy_sky_left2.png'),
    img('enemy_sky_left/enemy_sky_left3.png'),
    img('enemy_sky_left/enemy_sky_left4.png'),
    img('enemy_sky_left/enemy_sky_left5.png'),
    img('enemy_sky_left/enemy_sky_left4.png'),
    img('enemy_sky_left/enemy_sky_left3.png'),
    img('enemy_sky_left/enemy_sky_left2.png')
]

enemy_sky_anim_speed = 3
enemy_sky_anim_stage = 0

enemy_sky_anim_count = 0
enemy_sky_x = 800
enemy_sky_y = 400

# БЭКГРАУНД
bg = img('pixel_bg.png')

bg_x = 0

# ВНЕДРЕНИЕ ВСЕГО В ИГРУ

running = True
while running:

    # НАСТРОЙКА БЭКГРАУНДА

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1099, 0))

    bg_x -= 1  # настраиваем скорость движения бэкграунда
    if bg_x == -1099:
        bg_x = 0

    # ВНЕДРЕНИЕ ВРАГОВ И НАСТРОЙКА ЕГО АНИМАЦИИ

    # Наземный
    screen.blit(enemy_land_left[enemy_land_anim_count], (enemy_land_x, enemy_land_y))
    # Воздушный
    screen.blit(enemy_sky_left[enemy_sky_anim_count], (enemy_sky_x, enemy_sky_y))

    # строчки ниже - настройка индексов анимаций игрока
    if animation_stage == animation_speed:
        animation_stage = 0
        if enemy_land_anim_count == 1:  # Обнуляем индекс, когда доходим до последнего элемента списка (чтобы не выйти за него)
            enemy_land_anim_count = 0
        else:
            enemy_land_anim_count += 1  # каждый раз, заходя в цикл, будем увеличивать индекс, выводя поочередно все элементы
    else:
        animation_stage += 1

    # строчки ниже - настройка индексов анимаций игрока
    if enemy_sky_anim_stage == enemy_sky_anim_speed:
        enemy_sky_anim_stage = 0
        if enemy_sky_anim_count == 7:  # Обнуляем индекс, когда доходим до последнего элемента списка (чтобы не выйти за него)
            enemy_sky_anim_count = 0
        else:
            enemy_sky_anim_count += 1  # каждый раз, заходя в цикл, будем увеличивать индекс, выводя поочередно все элементы
    else:
        enemy_sky_anim_stage += 1

    # ВНЕДРЕНИЕ ИГРОКА И НАСТРОЙКА ЕГО АНИМАЦИИ

    player = img('player_right/player_right1.png')  # базовая картинка игрока
    keys = pygame.key.get_pressed()  # Кнопка, на которую сейчас нажимает пользователь
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    # Выводим на экран игрока с указанием его координат,
    # при этом выводя все элементы списка по индексу указанной в кв скобках переменной. Это для эффекта движения влево
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
        # это то же самое, но для эффекта движения вправо
    else:
        screen.blit(player, (player_x, player_y))  # делаем такую картинку когда игрок стоит
    # строчки ниже - настройка индексов анимаций игрока
    if animation_stage == animation_speed:
        animation_stage = 0
        if player_anim_count == 1:  # Обнуляем индекс, когда доходим до последнего элемента списка (чтобы не выйти за него)
            player_anim_count = 0
        else:
            player_anim_count += 1  # каждый раз, заходя в цикл, будем увеличивать индекс, выводя поочередно все элементы
    else:
        animation_stage += 1

    # НАСТРОЙКА ДВИЖЕНИЯ И ПРЫЖКА ИГРОКА

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 20:
        # Если эта кнопка равна стрелке влево или букве A, да и коорд игр больше 50 (невидимая граница слева), то:
        player_x -= player_speed  # движемся влево, вычитая показатели из координат игрока
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < 1039:
        # Если эта кнопка равна стрелке вправо или букве D, да и коорд игр меньше 649 (невидимая граница справа), то:
        player_x += player_speed  # движемся вправо, прибавляя показатели к координатам игрока

    if not is_jump:  # Если наш герой в данный момент не прыгает, то:
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:  # при наж на пробел / W / стрелку вверх:
            is_jump = True  # значение прыжка активируется и герой должен прыгнуть
    else:  # если значение прыжка активируется, то:
        if jump_count >= -10:  # покуда всё больше -10, процесс прыжка идёт
            if jump_count >= 0:  # для поднятия
                player_y -= (jump_count ** 2) / 2  # Возводим в квадрат для БОЛЬШЕЙ МОЩИ! Делим на 2 для плавного эффек.
                # поднимаем игрока, постепенны отнимая числа от его координат
            else:  # для опускания
                player_y += (jump_count ** 2) / 2  # опускаем игрока
            jump_count -= 1  # постепенно отнимаем 1 для плавного перемещения игрока вверх и обратно.
        else:  # если дошли до -10, то прыжок уже сделан, можно вернуть все параметры к старым значениям.
            is_jump = False
            jump_count = 10

    player_hitbox = Rect(player_x, player_y, 26, 34)

    # ВЫЯВЛЕНИЕ КОЛЛИЗИЙ ВРАГОВ И ИГРОКА

    enemy_land_hitbox = Rect(enemy_land_x, enemy_land_y, 104, 88)
    enemy_sky_hitbox = Rect(enemy_sky_x, enemy_sky_y + 49, 98, 44)

    collision = Rect.colliderect(player_hitbox, enemy_land_hitbox)
    collision = collision or Rect.colliderect(player_hitbox, enemy_sky_hitbox)

    if collision:
        player_lives -= 1
        player_x = 150
        player_y = 540
        is_jump = False
        jump_count = 10 

    if player_lives == 0: running = False

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(20)  # указываем количество фреймов за 1 сек, т.е. количество раз, которое проиграется цикл за 1 сек
    # иначе говоря, скорость смены изображений-анимаций игрока.
