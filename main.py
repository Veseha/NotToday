import os
import sys
import random
import pygame
from global_varibals import STEPS, MAXENERGY, check_ellipse, deadlines


def init_display(WIDTH, HEIGHT):  # NOT EDIT, WORKS 100%
    global screen, background
    SIZE = WIDTH, HEIGHT
    if WIDTH <= 1280:
        screen = pygame.display.set_mode(SIZE)
    if WIDTH > 1280:
        screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    background = screen.copy()
    background.fill((0, 0, 0, 0))
    screen.blit(background, (0, 0))


def ellipse_on_screen():
    if check_ellipse:
        pygame.draw.circle(screen, (0, 0, 0), (640, 360), 800, 650)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    # print(fullname)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ['']

    fon = pygame.transform.scale(load_image('menu.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        print('Start window')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key != pygame.K_F11:
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:  # Q - quit
                    print('We are leaving ...')
                    exit(0)
                if event.key == pygame.K_F11:  # F - full screen
                    if screen.get_width() > 1280:
                        init_display(1280, 720)
                        break
                    if screen.get_width() == 1280:
                        init_display(1281, 721)
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        text_coord = 0
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        clock.tick(30)


def preview():
    fon = pygame.transform.scale(load_image('background.png'), (width, height))
    screen.blit(fon, (0, 0))

    pygame.display.flip()
    clock.tick(1)


def rules():
    fon = pygame.transform.scale(load_image('rules.png'), (width, height))
    screen.blit(fon, (0, 0))

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP:
                if event.key != pygame.K_F11:
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:  # Q - quit
                    print('We are leaving ...')
                    exit(0)
                if event.key == pygame.K_F11:  # F - full screen
                    if screen.get_width() > 1280:
                        init_display(1280, 720)
                        break
                    if screen.get_width() == 1280:
                        init_display(1281, 721)
        pygame.display.flip()
        screen.blit(fon, (0, 0))
        clock.tick(30)


def load_level(filename):
    filename = 'data/' + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    fx, fy = 0, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)

            elif level[y][x] == 'a':   # Верхний Левый угол
                Tile('wall41', x, y)
            elif level[y][x] == 'b':
                Tile('wall42', x, y)
            elif level[y][x] == 'c':
                Tile('wall43', x, y)
            elif level[y][x] == 'd':
                Tile('wall44', x, y)

            elif level[y][x] == 'e':  # Верхний правый угол
                Tile('wall31', x, y)
            elif level[y][x] == 'f':
                Tile('wall32', x, y)
            elif level[y][x] == 'g':
                Tile('wall33', x, y)
            elif level[y][x] == 'h':
                Tile('wall34', x, y)

            elif level[y][x] == '1':   # Стороны
                Tile('wall11', x, y)
            elif level[y][x] == '2':
                Tile('wall12', x, y)
            elif level[y][x] == '3':
                Tile('wall21', x, y)
            elif level[y][x] == '4':
                Tile('wall22', x, y)
            elif level[y][x] == '5':
                Tile('walll1', x, y)
            elif level[y][x] == '6':
                Tile('walll2', x, y)
            elif level[y][x] == '7':
                Tile('wallr1', x, y)
            elif level[y][x] == '8':
                Tile('wallr2', x, y)
            elif level[y][x] == '9':
                Tile('walld1', x, y)
            elif level[y][x] == '0':
                Tile('walld2', x, y)

            elif level[y][x] == 'i':   # Угол нижний закрывающий левый
                Tile('wallll1', x, y)
            elif level[y][x] == 'j':
                Tile('wallll2', x, y)
            elif level[y][x] == 'k':
                Tile('wallll3', x, y)
            elif level[y][x] == 'l':
                Tile('wallll4', x, y)

            elif level[y][x] == 'm':   # Угол нижний закрывающий правый
                Tile('wallrr1', x, y)
            elif level[y][x] == 'n':
                Tile('wallrr2', x, y)
            elif level[y][x] == 'o':
                Tile('wallrr3', x, y)
            elif level[y][x] == 'p':
                Tile('wallrr4', x, y)

            elif level[y][x] == 'u':   # Полноразмерные доп. углы, видные
                Tile('wallul1', x, y)
            elif level[y][x] == 'v':
                Tile('wallul2', x, y)
            elif level[y][x] == 'w':
                Tile('wallur1', x, y)
            elif level[y][x] == 'x':
                Tile('wallur2', x, y)

            elif level[y][x] == 'y':  # Неполные доп. углы, уходят в бездну
                Tile('wallrl', x, y)
            elif level[y][x] == 'z':
                Tile('walllr', x, y)

            elif level[y][x] == '>':
                Tile('wallP1', x, y)
            elif level[y][x] == '<':
                Tile('wallP2', x, y)

            elif level[y][x] == '@':
                Tile('empty', x, y)
                fx, fy = x, y
    # new_player = Player(fx, fy)
    # return new_player, x, y, fx, fy
    return x, y, fx, fy

#
# class Mouse(pygame.sprite.Sprite):
#     def __init__(self, group):
#         super().__init__(group)
#         self.image = load_image('arrow.png', -1)
#         self.rect = self.image.get_rect()
#         self.rect.x = 0
#         self.rect.y = 0
#
#     def update(self, *args):
#         if bool(pygame.mouse.get_focused()):
#             self.rect.x, self.rect.y = mousepos
#         else:
#             self.rect.x, self.rect.y = (-100, -100)
#
#     def get_event(self, *args):
#         pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type == 'wallll3' or tile_type == 'wallrr1':
            None
        elif tile_type[:4] == 'wall' and (tile_type != 'wallll3' or tile_type != 'wallrr1'):
            self.add(not_passable_group)
        if tile_type == 'empty':
            self.image = load_image('plank' + random.choice(['1', '1', '2', '2', '3', '4', '5', '1', '6']) +
                                    '1.png')
        else:
            self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.kost = Kostyl(x, y)
        sx, sy = 70, 70
        self.moving_left = [
            pygame.transform.scale(load_image(r'player\walking_left\walk ' + str(i) + '.png', -1), (sx, sy)) for i in
            range(0, 6)]
        self.moving_right = [
            pygame.transform.scale(load_image(r'player\walking_right\walk ' + str(i) + '.png', -1), (sx, sy)) for i in
            range(0, 6)]
        self.walking_up = [
            pygame.transform.scale(load_image(r'player\walking_up\walk ' + str(i) + '.png', -1), (sx, sy)) for
            i in range(0, 6)]
        self.walking_down = [
            pygame.transform.scale(load_image(r'player\walking_down\walk ' + str(i) + '.png', -1), (sx, sy)) for
            i in range(0, 6)]

        self.image = self.walking_down[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * 50 - 18, y * 50 - 46

    def update(self, *args):
        global cfm
        k = 0.5
        if vy_actual < 0:
            if cfm % 1 == 0:
                self.image = self.walking_up[int(cfm)]
            cfm -= k

            if cfm == -STEPS:
                cfm = 0

        if vy_actual > 0:
            if cfm % 1 == 0:
                self.image = self.walking_down[int(cfm)]
            cfm += k
            if cfm == STEPS:
                cfm = 0

        if vx_actual < 0:
            if cfm % 1 == 0:
                self.image = self.moving_left[int(cfm)]
            cfm -= k
            if cfm == -STEPS:
                cfm = 0

        if vx_actual > 0:
            if cfm % 1 == 0:
                self.image = self.moving_right[int(cfm)]
            cfm += k
            if cfm == STEPS:
                cfm = 0
        self.rect.x = self.kost.rect.x - 18
        self.rect.y = self.kost.rect.y - 46

        collide = False
        for i in not_passable_group:
            if pygame.sprite.collide_mask(i, self):
                collide = True
        if collide:
            self.rect.x = self.kost.rect.x - 18
            self.rect.y = self.kost.rect.y - 46


class Kostyl(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        sx, sy = 35, 24
        self.moving_left = pygame.transform.scale(load_image(r'player\walking_left\kvadrat.png', -1), (sx, sy))
        self.image = self.moving_left
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * 50, y * 50

    def update(self, *args):
        global cfm
        xx, yy = 0, 0
        k = 1
        self.image = self.moving_left
        if vx_actual > 0:
            self.rect.x += velocity_direction_x * speed_player
            xx = 1
        elif vy_actual > 0:
            self.rect.y += velocity_direction_y * speed_player
            yy = 1
        elif vx_actual < 0:
            self.rect.x += velocity_direction_x * speed_player
            xx = -1
        elif vy_actual < 0:
            self.rect.y += velocity_direction_y * speed_player
            yy = -1

        if pygame.sprite.spritecollideany(self, not_passable_group):
            self.rect.x -= xx * speed_player
            self.rect.y -= yy * speed_player


class Deadline(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(deadline_group, all_sprites)
        sx, sy = 50, 5
        self.image = load_image('deadline.png')
        self.rect = self.image.get_rect().move(sx * x, 50 * y)

    def update(self, *args):
        if 580 < self.rect.x < 650 and 359 < self.rect.y < 397:
            global running
            running = False
            fon = pygame.transform.scale(load_image('youdied' + random.choice(['1',
                                                                               '2', '3', '4', '5',
                                                                               '6',
                                                                               '1', '2', '3', '4',
                                                                               '5']) + '.png'),
                                         (width, height))
            screen.blit(fon, (0, 0))

            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        exit(0)
                pygame.display.flip()
                screen.blit(fon, (0, 0))
                clock.tick(15)


    # if 580 < tiles_group.sprites()[0].rect[0] < 650 and 319 < \
    #   tiles_group.sprites()[0].rect[1] < 397:


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)
        # print(self.dx, self.dy)


def print_energy():
    screen.blit(string_rendered_energy, intro_rect_energy)
    pygame.draw.rect(screen, (0, 0, 255), (115, 15, speed_energy, 30))
    pygame.draw.rect(screen, (255, 255, 255), (115, 15, 100, 30), 2)


screen = None


try:
    cur_lvl = load_level(r'levels/' + (str(sys.argv[1]) if len(sys.argv) > 1 or False else 'level1.lvl'))
except Exception as e:
    print('level not detected.')
    cur_lvl = load_level(r'levels/level1.lvl')


pygame.init()
running = True

font_energy = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 30)
string_rendered_energy = font_energy.render('Energy', 1, pygame.Color('white'))
intro_rect_energy = string_rendered_energy.get_rect()
intro_rect_energy.top = 10
intro_rect_energy.x = 10

init_display(1280, 720)
cfm = 0
speed_player = 4
speed_energy = MAXENERGY
size = width, height = screen.get_size()
clock = pygame.time.Clock()
# isinfocus = bool(pygame.mouse.get_focused())
#mousepos = (-50, -50)
# playerpos = (0, 0)
velocity_direction_x = 0
velocity_direction_y = 0

tile_images = {'wall': load_image('box.png'), 'wall11': load_image('wall11.png'),
               'wall12': load_image('wall12.png'), 'wall21': load_image('wall21.png'),
               'wall22': load_image('wall22.png'), 'wall31': load_image('wall31.png'),
               'wall32': load_image('wall32.png'), 'wall33': load_image('wall33.png'),
               'wall34': load_image('wall34.png'), 'wall41': load_image('wall41.png'),
               'wall42': load_image('wall42.png'), 'wall43': load_image('wall43.png'),
               'wall44': load_image('wall44.png'), 'walll1': load_image('walll1.png'),
               'walll2': load_image('walll2.png'), 'wallr1': load_image('wallr1.png'),
               'wallr2': load_image('wallr2.png'), 'walld1': load_image('walld1.png'),
               'walld2': load_image('walld2.png'), 'wallll1': load_image('wallll1.png'),
               'wallll2': load_image('wallll2.png'), 'wallll3': load_image('wallll3.png'),
               'wallll4': load_image('wallll4.png'), 'wallrr1': load_image('wallrr1.png'),
               'wallrr2': load_image('wallrr2.png'), 'wallrr3': load_image('wallrr3.png'),
               'wallrr4': load_image('wallrr4.png'), 'wallul1': load_image('wallul1.png'),
               'wallul2': load_image('wallul2.png'), 'wallur1': load_image('wallur1.png'),
               'wallur2': load_image('wallur2.png'), 'wallrl': load_image('wallrl.png'),
               'walllr': load_image('walllr.png'), 'wallP1': load_image('wallP1.png'),
               'wallP2': load_image('wallP2.png'),
}



tile_width = tile_height = 50
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
deadline_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
not_passable_group = pygame.sprite.Group()

image_player_global = None
screen.fill((0, 0, 0))
vx_actual, vy_actual = 0, 0
move_ticker = 0
check_for_change_image = [0]
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
# player, level_x, level_y = generate_level(cur_lvl)
level_x, level_y, fx, fy = generate_level(cur_lvl)
Deadline(4, 29)
player = Player(fx, fy)
# mousePoint, cam = Mouse(all_sprites), Camera()
cam = Camera()


preview()
start_screen()
rules()
print(all_sprites)
print(all_sprites.sprites())
# for i in range(1):
#     print(all_sprites.remove(i))
print(all_sprites)


pygame.display.flip()
try:
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mousepos = event.pos
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:  # Q - quit
                    print('We are leaving ...')
                    exit(0)
                if event.key == pygame.K_F11:  # F - full screen
                    if screen.get_width() > 1280:
                        init_display(1280, 720)
                        break
                    if screen.get_width() == 1280:
                        init_display(1281, 721)

        if check_for_change_image[0] and cfm != 0:
            velocity_direction_y = check_for_change_image[3]
            velocity_direction_x = check_for_change_image[2]
            select_button = check_for_change_image[1]
        elif check_for_change_image[0] and cfm == 0:
            check_for_change_image[0] = 0
            select_button = 0
            velocity_direction_x = 0
            velocity_direction_y = 0

        try:
            #isinfocus = bool(pygame.mouse.get_focused())
            screen.fill((0, 0, 0))
            keys = pygame.key.get_pressed()
            if keys:
                if keys[pygame.K_w]:
                    velocity_direction_x = 0
                    velocity_direction_y = -1
                elif keys[pygame.K_s]:
                    velocity_direction_x = 0
                    velocity_direction_y = 1
                elif keys[pygame.K_d]:
                    velocity_direction_x = 1
                    velocity_direction_y = 0
                elif keys[pygame.K_a]:
                    velocity_direction_x = -1
                    velocity_direction_y = 0
                else:
                    velocity_direction_x = 0
                    velocity_direction_y = 0
                if keys[pygame.K_LCTRL]:
                    if speed_energy > 0:
                        speed_player = 8
                        speed_energy -= 0.5
                    else:
                        speed_energy = 0
                        speed_player = 5
                elif speed_energy != MAXENERGY:
                    speed_player = 5
                    if speed_energy != MAXENERGY:
                        speed_energy += 0.25

            if velocity_direction_x != 0 or vx_actual != 0:
                vy_actual = 0
                if vx_actual in [STEPS, -STEPS]:
                    vx_actual = 0
                if velocity_direction_x > 0 or vx_actual > 0:
                    if vx_actual < 0:
                        vx_actual = 0
                    vx_actual += 1
                    vy_actual = 0
                    velocity_direction_y = 0
                if velocity_direction_x < 0 or vx_actual < 0:
                    if vx_actual > 0:
                        vx_actual = 0
                    vx_actual -= 1
                    vy_actual = 0
                    velocity_direction_y = 0
            elif velocity_direction_y != 0 or vy_actual != 0:
                vx_actual = 0
                if vy_actual in [STEPS, -STEPS]:
                    vy_actual = 0
                if velocity_direction_y > 0 or vy_actual > 0:
                    if vy_actual < 0:
                        vy_actual = 0
                    vy_actual += 1
                    vx_actual = 0
                    velocity_direction_x = 0
                if velocity_direction_y < 0 or vy_actual < 0:
                    if vy_actual > 0:
                        vy_actual = 0

                    vy_actual -= 1
                    vx_actual = 0
                    velocity_direction_x = 0

            all_sprites.draw(screen)
            all_sprites.update()
            # print(all_sprites)
            #if 580 < tiles_group.sprites()[0].rect[0] < 650 and 319 < \
             #   tiles_group.sprites()[0].rect[1] < 397:
              #  print('iam here!')
            # print(tiles_group.sprites()[0].rect)


            cam.update(player)
            for sprite in all_sprites:
                cam.apply(sprite)
            ellipse_on_screen()
            print_energy()
            # print(player_group.sprites())
            pygame.display.flip()
            clock.tick(60)
        except Exception as a:
            print(a)
except Exception as aa:
    print(aa)
pygame.quit()
