import os
import sys
import random
import pygame
from global_varibals import STEPS, MAXENERGY, check_ellipse, deadlines,\
    text_message, check_message, image_message, fun_lever, select_lever, check_pc


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
            elif level[y][x] == '^':
                # Tile('empty', x, y)
                Lever(x, y)
            elif level[y][x] == '+':
                Lava(x, y)
            elif level[y][x] == '!':
                Pc(x, y)
            elif level[y][x] == '?':
                Pc2(x, y)
            elif level[y][x] == '$':
                Button(x, y)
            elif level[y][x] == 'A':
                Door(x, y)
                Tile('door2', x, y)
            elif level[y][x] == 'B':
                Tile('door1', x, y)

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
                Message(x, y)
                Tile('wallP2', x, y)
            elif level[y][x] == '&':
                Tile('wallP1', x, y)
            elif level[y][x] == '~':
                MessageEnd(x, y)
                Tile('wallP2', x, y)

            elif level[y][x] == '@':
                Tile('empty', x, y)
                fx, fy = x, y
    return x, y, fx, fy #


def print_energy():
    screen.blit(string_rendered_energy, intro_rect_energy)
    pygame.draw.rect(screen, (0, 0, 255), (115, 15, speed_energy, 30))
    pygame.draw.rect(screen, (255, 255, 255), (115, 15, 100, 30), 2)


def print_time(sec):
    string_rendered_time = font_energy.render('Time left: ' + str(sec // 60) +
                                              ':' + str(sec % 60), 3, pygame.Color('white'))
    screen.blit(string_rendered_time, (10, 60, 17, 35))


def died():
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


class Mouse(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = load_image('arrow.png', -1)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if bool(pygame.mouse.get_focused()):
            self.rect.x, self.rect.y = mousepos
        else:
            self.rect.x, self.rect.y = (-100, -100)

    def get_event(self, *args):
        pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type == 'wallll3' or tile_type == 'wallrr1':
            None
        # elif tile_type == 'door1':
         #   self.image = load_image('door1')
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
    def __init__(self, type, x, y, num):
        super().__init__(deadline_group, all_sprites)
        self.type = type
        self.num = (x, y)
        if type == 'x':
            self.image = load_image('deadline.png')
            self.rect = self.image.get_rect().move(50 * x, 50 * y)
        if type == 'y':
            self.image = load_image('deadline1.png')
            self.rect = self.image.get_rect().move(50 * x + 25, 50 * y)

    def update(self, *args):
        if (580 < self.rect.x < 650 and 359 < self.rect.y < 397 and self.type == 'x') or \
                (637 < self.rect.x < 643 and 343 < self.rect.y < 372 and self.type == 'y'):
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

    def suicide(self):
        self.kill()

    # if 580 < tiles_group.sprites()[0].rect[0] < 650 and 319 < \
    #   tiles_group.sprites()[0].rect[1] < 397:


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(lava_group, all_sprites)
        self.image = load_image('lava.png')
        self.rect = self.image.get_rect().move(50 * x, 50 * y)

    def update(self, *args):
        if 577 < self.rect.x < 653 and 324 < self.rect.y < 397:
            global running
            running = False
            fon = pygame.transform.scale(load_image('deadlava.png'), (width, height))
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


class Message(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(message_group, all_sprites)
        self.type = (x, y)
        self.image = load_image('box.png', -1)
        self.rect = self.image.get_rect().move(50 * x + 50, 50 * y)
        # print(self.type)

    def update(self, *args):
        global check_message
        if check_message:
            if 590 < self.rect.x < 740 and 283 < self.rect.y < 433 and check_message:
                fon = pygame.transform.scale(load_image(image_message[self.type]), (width, height))
                check = True
                while check:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_F11:  # F - full screen
                                if screen.get_width() > 1280:
                                    init_display(1280, 720)
                                    break
                                if screen.get_width() == 1280:
                                    init_display(1281, 721)
                            else:
                                check = False
                    pygame.display.flip()
                    screen.blit(fon, (0, 0))
                    clock.tick(15)
            else:
                check_message = False


class Lever(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(lever_group, all_sprites)
        self.image = load_image('lever11.png', -1)
        self.rect = self.image.get_rect().move(50 * x, 50 * y)

    def update(self, *args):
        global check_message, deadlines, select_lever

        if check_message:
            if 590 < self.rect.x < 740 and 283 < self.rect.y < 433:
                if select_lever == [('x', 12, 13)]:
                    select_lever = [('y', 29, 27)]
                self.image = load_image('lever22.png', -1)
                for j in select_lever:
                    # chk = 0
                    for i in range(len(deadline_group.sprites()) - 1):
                        if deadline_group.sprites()[i].num == (j[1], j[2]):
                            deadline_group.sprites()[i].suicide()
            else:
                check_message = False


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image('button.png')
        self.rect = self.image.get_rect().move(50 * x, 50 * y)
        self.cheker = True

    def update(self, *args):
        global check_message, select_lever
        if self.cheker:
            if 590 < self.rect.x < 740 and 283 < self.rect.y < 433:
                self.image = load_image('button1.png')
                for j in fun_lever[2]:
                    for i in range(len(deadline_group.sprites())):
                        if deadline_group.sprites()[i].num == (j[1], j[2]):
                            deadline_group.sprites()[i].suicide()
                self.cheker = False


class Pc(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pc_group, all_sprites)
        self.image = load_image('pc0.png', -1)
        self.rect = self.image.get_rect().move(50 * x, 50 * y)
        self.add(not_passable_group)
        self.pov = 0
        self.num = 0

    def update(self, *args):
        global check_pc, running

        if 590 < self.rect.x < 740 and 283 < self.rect.y < 433 and check_pc:
            check = True
            self.num += 1
            if self.pov == 0 and self.num <= 3:
                fon = pygame.transform.scale(load_image('pccast1.png'), (width, height))
            elif self.pov == 2 and self.num <= 3:
                fon = pygame.transform.scale(load_image('pccast3.png'), (width, height))
            elif self.num > 3:
                fon = pygame.transform.scale(load_image('pccastE.png'), (width, height))
                self.image = load_image('pc3.png', -1)
                chkr = True
                while chkr:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                        elif event.type == pygame.KEYDOWN:
                                if self.pov == 2:
                                    fon = pygame.transform.scale(load_image('fatalerror.png'), (width, height))
                                    self.pov = 3
                                elif self.pov == 3:
                                    running = False
                                    terminate()
                                    return
                    pygame.display.flip()
                    screen.blit(fon, (0, 0))
                    clock.tick(15)

            while check:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:  # F - full screen
                            if screen.get_width() > 1280:
                                init_display(1280, 720)
                                break
                            if screen.get_width() == 1280:
                                init_display(1281, 721)
                        else:
                            if self.pov == 0:
                                fon = pygame.transform.scale(load_image('pccast2.png'), (width, height))
                                self.pov = 1
                            elif self.pov == 1:
                                fon = pygame.transform.scale(load_image('pccast3.png'), (width, height))
                                self.pov = 2
                            elif self.pov == 2:
                                check = False
                                check_pc = False
                                self.image = load_image('pc1.png', -1)

                pygame.display.flip()
                screen.blit(fon, (0, 0))
                clock.tick(15)
        else:
            check_pc = False


class Pc2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(pc_group, all_sprites)
        self.image = load_image('pc0.png', -1)
        self.rect = self.image.get_rect().move(50 * x, 50 * y)
        self.add(not_passable_group)
        self.aaa = True

    def update(self, *args):
        global check_pc
        if 590 < self.rect.x < 740 and 283 < self.rect.y < 433 and check_pc and self.aaa:
            check = True
            red = False
            ans = []
            fon = pygame.transform.scale(load_image('pcin.png'), (width, height))

            while check:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if red:
                            fon = pygame.transform.scale(load_image('pcin.png'), (width, height))
                            red = False
                        if event.key == pygame.K_F11:  # F - full screen
                            if screen.get_width() > 1280:
                                init_display(1280, 720)
                                break
                            if screen.get_width() == 1280:
                                init_display(1281, 721)
                        elif event.key == pygame.K_SPACE:
                            return
                        elif event.key == pygame.K_1:
                            ans.append(1)
                        elif event.key == pygame.K_2:
                            ans.append(2)
                        elif event.key == pygame.K_7:
                            ans.append(7)
                        elif event.key == pygame.K_8:
                            ans.append(8)
                        else:
                            ans.append(0)
                if len(ans) >= 4:
                    if ans == [1, 7, 2, 8]:
                        fon = pygame.transform.scale(load_image('pcG.png'), (width, height))
                        pygame.display.flip()
                        screen.blit(fon, (0, 0))
                        w = True
                        self.aaa = False
                        self.image = load_image('pc3.png', -1)
                        for j in fun_lever[1]:
                            for i in range(len(deadline_group.sprites())):
                                if deadline_group.sprites()[i].num == (j[1], j[2]):
                                    deadline_group.sprites()[i].suicide()
                        while w:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    terminate()
                                elif event.type == pygame.KEYDOWN:
                                    w = False
                                    check = False
                            clock.tick(15)
                    else:
                        fon = pygame.transform.scale(load_image('pcR.png'), (width, height))
                        red = True
                pygame.display.flip()
                screen.blit(fon, (0, 0))
                clock.tick(15)
        else:
            check_pc = False


class MessageEnd(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(message_group, all_sprites)
        self.type = (x, y)
        # print(self.type)
        self.image = load_image('box.png', -1)
        self.rect = self.image.get_rect().move(50 * x + 50, 50 * y)

    def update(self, *args):
        global check_message
        global check_orc

        aaa = False
        if check_message:
            if 590 < self.rect.x < 740 and 283 < self.rect.y < 433 and check_message:
                fon = pygame.transform.scale(load_image(image_message[self.type]), (width, height))
                check = True
                while check:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            terminate()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_F11:  # F - full screen
                                if screen.get_width() > 1280:
                                    init_display(1280, 720)
                                    break
                                if screen.get_width() == 1280:
                                    init_display(1281, 721)
                            else:
                                for j in fun_lever[3]:
                                    for i in range(len(deadline_group.sprites()) - 1):
                                        if deadline_group.sprites()[i].num == (j[1], j[2]):
                                            deadline_group.sprites()[i].suicide()
                                for j in fun_lever[4]:
                                    for i in range(len(deadline_group.sprites()) - 1):
                                        if deadline_group.sprites()[i].num == (j[1], j[2]):
                                            deadline_group.sprites()[i].suicide()
                                corr = [all_sprites.sprites()[0].rect[0], all_sprites.sprites()[0].rect[1]]
                                corrx = (950 - corr[0]) / 50
                                corry = (0 - corr[1]) / 50
                                for i in [['y', 11, 15], ['y', 13, 11], ['y', 13, 18], ['x', 12, 6], ['x', 14, 23]]:
                                    Deadline(i[0], i[1] - corrx, i[2] - corry, 0)
                                # Orc(34, 4)
                                aaa = True
                                print(deadline_group.sprites()[-1].rect)
                                check = False

                    pygame.display.flip()
                    screen.blit(fon, (0, 0))
                    clock.tick(15)
            else:
                check_message = False
        if aaa:
            check_orc = True


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(message_group, all_sprites)
        self.image = load_image('door2.png')
        self.rect = self.image.get_rect().move(50 * x + 50, 50 * y)
        # print(self.type)

    def update(self, *args):
        if 590 < self.rect.x < 740 and 283 < self.rect.y < 433 and check_message:
            fon = pygame.transform.scale(load_image('win.png'), (width, height))
            check = True
            while check:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F11:  # F - full screen
                            if screen.get_width() > 1280:
                                init_display(1280, 720)
                                break
                            if screen.get_width() == 1280:
                                init_display(1281, 721)
                        else:
                            check = False
                pygame.display.flip()
                screen.blit(fon, (0, 0))
                clock.tick(15)


class Orc(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(orc_group, all_sprites)
        sx, sy = 70, 70
        self.moving_left = pygame.transform.scale(load_image(r'player\walking_left\orc.png', -1), (sx, sy))
        self.moving_right = pygame.transform.scale(load_image(r'player\walking_right\orc.png', -1), (sx, sy))
        self.walking_up = pygame.transform.scale(load_image(r'player\walking_up\orc.png', -1), (sx, sy))
        self.walking_down = pygame.transform.scale(load_image(r'player\walking_down\orc.png', -1), (sx, sy))
        self.image = self.walking_down
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x * 50 - 18, y * 50 - 46

    def update(self, *args):
        self.image = self.walking_down
        if self.rect.x < 601:
            self.rect.x += 2
        else:
            self.rect.x -= 2
        if self.rect.y < 344:
            self.rect.y += 2
        else:
            self.rect.y -= 2
        if 590 < self.rect.x < 740 and 283 < self.rect.y < 433:
            global running
            running = False
            fon = pygame.transform.scale(load_image('scrimer.png'),(width, height))
            screen.blit(fon, (0, 0))
            checing = True

            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if checing:
                            fon = pygame.transform.scale(load_image('youdied' + random.choice(['1',
                                                                                               '2', '3', '4', '5',
                                                                                               '6',
                                                                                               '1', '2', '3', '4',
                                                                                               '5']) + '.png'),
                                                         (width, height))
                            checing = False
                        else:
                            terminate()
                pygame.display.flip()
                screen.blit(fon, (0, 0))
                clock.tick(15)


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
               'wallP2': load_image('wallP2.png'), 'door1': load_image('door1.png'),
                'door2': load_image('door2.png')
}



tile_width = tile_height = 50
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
deadline_group = pygame.sprite.Group()
message_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
lever_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
pc_group = pygame.sprite.Group()
not_passable_group = pygame.sprite.Group()
orc_group = pygame.sprite.Group()

image_player_global = None
screen.fill((0, 0, 0))
vx_actual, vy_actual = 0, 0
move_ticker = 0
check_orc = False
check_orc_1 = False
check_for_change_image = [0]
pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
level_x, level_y, fx, fy = generate_level(cur_lvl)
for j in range(len(deadlines)):
    i = deadlines[j]
    Deadline(i[0], i[1], i[2], j)
player = Player(fx, fy)
# print(all_sprites.sprites()[0].rect)
cam = Camera()
preview()
start_screen()
rules()
start_ticks = pygame.time.get_ticks()
# print(all_sprites.sprites()[0].rect)


pygame.display.flip()
try:
    while running:
        if check_orc:
            pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds >= 300:
            died()
        if check_orc_1:
            print('here')
            orc_group.update()
        for event in pygame.event.get():
            if check_orc:
                print()
                check_orc = False
                check_orc_1 = True
                Orc(-39, 10)
                orc_group.update()
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
                if event.key == pygame.K_e:
                    for i in range(len(message_group.sprites())):
                        # image_message = text_message[i]
                        check_message = True
                        message_group.sprites()[i].update()
                    for i in range(len(lever_group.sprites())):
                        select_lever = fun_lever[i]
                        check_message = True
                        lever_group.sprites()[i].update()
                    for i in range(len(pc_group.sprites())):
                        check_pc = True
                        pc_group.sprites()[i].update()

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
            # if 580 < tiles_group.sprites()[0].rect[0] < 650 and 319 < \
            #   tiles_group.sprites()[0].rect[1] < 397:
            #  print('iam here!')
            # print(tiles_group.sprites()[0].rect)

            cam.update(player)
            for sprite in all_sprites:
                cam.apply(sprite)

            ellipse_on_screen()
            print_energy()
            print_time(300 - seconds)

            pygame.display.flip()
            clock.tick(60)
        except Exception as a:
            print(a)
except Exception as aa:
    print(aa)
pygame.quit()
