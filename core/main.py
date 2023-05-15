# TODO: 1- make all the objects of the class rectangle
# TODO: 2- make the collision detection system with the rectangle point relation

import os
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, numpy as np
from Rectangles import *
from Textures import *
from Collision import *

# WINDOW PROPERTIES
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000

# CAR PROPERTIES
CAR_WIDTH = 70
CAR_HIEGHT = 30
CAR_SPEED = 0.1
CAR_ROTATION_SPEED = 1
time_interval = 1
keys_pressed = set()
car_pos = [WINDOW_WIDTH / 10, 3 * WINDOW_HEIGHT / 10]
car_angle = [90.0]
car_vel = [0.0, 0.0]
obstacle_speed = 1  # Changes on linux


# * =================================== Init PROJECTION ===================================== * #


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, -1, 1)
    glMatrixMode(GL_MODELVIEW)


# * ========================= Rectangle ( left, right ,  top , bottom ) ========================= * #
# Roads
LOWER_ROAD = Rectangle(0, WINDOW_WIDTH, WINDOW_HEIGHT / 5 - 10, 2 * WINDOW_HEIGHT / 5 + 10)
MIDDLE_ROAD = Rectangle(WINDOW_WIDTH / 2 - 20, 3 * WINDOW_WIDTH / 4 + 10, 2 * WINDOW_HEIGHT / 5, 3 * WINDOW_HEIGHT / 5)

UPPER_ROAD = Rectangle(0, WINDOW_WIDTH, 3 * WINDOW_HEIGHT / 5 - 10, 4 * WINDOW_HEIGHT / 5 + 10)
UPPER_LEFT_ROAD = Rectangle(WINDOW_WIDTH / 10 - 10, 3 * WINDOW_WIDTH / 10 + 10, 4 * WINDOW_HEIGHT / 5, WINDOW_HEIGHT)
UPPER_RIGHT_ROAD = Rectangle(7 * WINDOW_WIDTH / 10 - 10, 9 * WINDOW_WIDTH / 10 + 10, 4 * WINDOW_HEIGHT / 5,
                             WINDOW_HEIGHT)
# ! LAYER 01
rect_L1_1 = Rectangle(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT / 5)
# # ! LAYER 02
rect_L2_1 = Rectangle(-10, WINDOW_WIDTH / 2, 2 * WINDOW_HEIGHT / 5, 3 * WINDOW_HEIGHT / 5)
rect_L2_2 = Rectangle(3 * WINDOW_WIDTH / 4, WINDOW_WIDTH, 2 * WINDOW_HEIGHT / 5, 3 * WINDOW_HEIGHT / 5)
# # ! LAYER 03
rect_L3_1 = Rectangle(0, WINDOW_WIDTH / 10, 4 * WINDOW_HEIGHT / 5, WINDOW_HEIGHT)
rect_L3_2 = Rectangle(3 * WINDOW_WIDTH / 10, 7 * WINDOW_WIDTH / 10, 4 * WINDOW_HEIGHT / 5, WINDOW_HEIGHT)
rect_L3_3 = Rectangle(9 * WINDOW_WIDTH / 10, 10 * WINDOW_WIDTH / 10, 4 * WINDOW_HEIGHT / 5, WINDOW_HEIGHT)

# # * ========================= car models ( left, right ,  top , bottom ) ========================= * #
# road 1
car_Obj_1_0 = Rectangle(0, CAR_WIDTH, WINDOW_HEIGHT / 5, WINDOW_HEIGHT / 5 + CAR_HIEGHT)
car_Obj_1_1 = Rectangle(WINDOW_WIDTH / 3, WINDOW_WIDTH / 3 + CAR_WIDTH, WINDOW_HEIGHT / 5,
                        WINDOW_HEIGHT / 5 + CAR_HIEGHT)
car_Obj_1_2 = Rectangle(2 * WINDOW_WIDTH / 3, 2 * WINDOW_WIDTH / 3 + CAR_WIDTH, WINDOW_HEIGHT / 5,
                        WINDOW_HEIGHT / 5 + CAR_HIEGHT)
# road 2
car_Obj_2_0 = Rectangle(0, CAR_WIDTH, 2 * WINDOW_HEIGHT / 5 - CAR_HIEGHT, 2 * WINDOW_HEIGHT / 5)
car_Obj_2_1 = Rectangle(WINDOW_WIDTH / 3, WINDOW_WIDTH / 3 + CAR_WIDTH, 2 * WINDOW_HEIGHT / 5 - CAR_HIEGHT,
                        2 * WINDOW_HEIGHT / 5)
car_Obj_2_2 = Rectangle(2 * WINDOW_WIDTH / 3, 2 * WINDOW_WIDTH / 3 + CAR_WIDTH, 2 * WINDOW_HEIGHT / 5 - CAR_HIEGHT,
                        2 * WINDOW_HEIGHT / 5)
# road 3
car_Obj_3_0 = Rectangle(0, CAR_WIDTH, 3 * WINDOW_HEIGHT / 5, 3 * WINDOW_HEIGHT / 5 + CAR_HIEGHT)
car_Obj_3_1 = Rectangle(WINDOW_WIDTH / 3, WINDOW_WIDTH / 3 + CAR_WIDTH, 3 * WINDOW_HEIGHT / 5,
                        3 * WINDOW_HEIGHT / 5 + CAR_HIEGHT)
car_Obj_3_2 = Rectangle(2 * WINDOW_WIDTH / 3, 2 * WINDOW_WIDTH / 3 + CAR_WIDTH, 3 * WINDOW_HEIGHT / 5,
                        3 * WINDOW_HEIGHT / 5 + CAR_HIEGHT)
# road 4
car_Obj_4_0 = Rectangle(0, CAR_WIDTH, 4 * WINDOW_HEIGHT / 5 - CAR_HIEGHT, 4 * WINDOW_HEIGHT / 5)
car_Obj_4_1 = Rectangle(WINDOW_WIDTH / 3, WINDOW_WIDTH / 3 + CAR_WIDTH, 4 * WINDOW_HEIGHT / 5 - CAR_HIEGHT,
                        4 * WINDOW_HEIGHT / 5)
car_Obj_4_2 = Rectangle(2 * WINDOW_WIDTH / 3, 2 * WINDOW_WIDTH / 3 + CAR_WIDTH, 4 * WINDOW_HEIGHT / 5 - CAR_HIEGHT,
                        4 * WINDOW_HEIGHT / 5)
# # * ============================================ The main Car  ============================================ * #
car = Rectangle(0, CAR_WIDTH, 0, CAR_HIEGHT)


def collision_action():
    global car_pos, car_angle, car_vel
    car_pos = [WINDOW_WIDTH / 10, 3 * WINDOW_HEIGHT / 10]
    car_angle[0] = 0
    car_vel = [0.0, 0.0]
def drawState(carObj):
    global obstacle_speed
    glColor(1, 1, 1)  # White color
    carObj.draw_texture()

    carObj.left = carObj.left + obstacle_speed
    carObj.right = carObj.right + obstacle_speed

    if carObj.left >= WINDOW_WIDTH:
        carObj.left = -CAR_WIDTH
        carObj.right = 0


def main_car_movement():
    car.left = car_pos[0]
    car.right = car_pos[0] + CAR_WIDTH
    car.top = car_pos[1] + CAR_HIEGHT
    car.bottom = car_pos[1]
    glPushMatrix()
    glTranslatef(car_pos[0], car_pos[1], 0)
    glRotatef(car_angle[0], 0, 0, 1)
    glTranslatef(-car_pos[0], -car_pos[1], 0)
    car.draw_texture()
    # print(car_angle[0])
    glPopMatrix()

# * ===============================================  DRAW FUNCTION ========================================== * #

def draw():
    global car_pos, car_angle, car_vel, keys_pressed, obstacle_speed
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0, 0, 0, 1)

    # draw the world
    # LOWER_ROAD.drawRectangle((1,0,0))
    LOWER_ROAD.draw_texture()

    # MIDDLE_ROAD.drawRectangle((1,0,0))
    MIDDLE_ROAD.draw_texture()

    # UPPER_ROAD.drawRectangle((1,0,0))
    UPPER_ROAD.draw_texture()

    # UPPER_LEFT_ROAD.drawRectangle((1,0,0))
    UPPER_LEFT_ROAD.draw_texture()

    # UPPER_RIGHT_ROAD.drawRectangle((1,0,0))
    UPPER_RIGHT_ROAD.draw_texture()

    # rect_L1_1.drawRectangle((1,1,0))
    rect_L1_1.draw_texture()
    if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, rect_L1_1):
        collision_action()
    # rect_L2_1.drawRectangle((1,1,0))
    rect_L2_1.draw_texture()
    if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, rect_L2_1):
        collision_action()
    # rect_L2_2.drawRectangle((1,1,0))
    rect_L2_2.draw_texture()
    if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, rect_L2_2):
        collision_action()
    # rect_L3_1.drawRectangle((1,1,0))
    rect_L3_1.draw_texture()
    if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, rect_L3_1):
        collision_action()
    # rect_L3_2.drawRectangle((1,1,0))
    rect_L3_2.draw_texture()
    if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, rect_L3_2):
        collision_action()
    # rect_L3_3.drawRectangle((1,1,0))
    rect_L3_3.draw_texture()
    if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, rect_L3_3):
        collision_action()

    # * ========================= Draw cars ========================= * #
    obs_list = [car_Obj_1_0, car_Obj_1_1, car_Obj_1_2,
                car_Obj_2_0, car_Obj_2_1, car_Obj_2_2,
                car_Obj_3_0, car_Obj_3_1, car_Obj_3_2,
                car_Obj_4_0, car_Obj_4_1, car_Obj_4_2]

    for i in obs_list:
        drawState(i)
        if collision(car_pos, car_angle, CAR_WIDTH, CAR_HIEGHT, i):
            collision_action()


    if 'left' in keys_pressed:
        car_angle[0] += CAR_ROTATION_SPEED
    if 'right' in keys_pressed:
        car_angle[0] -= CAR_ROTATION_SPEED
    if 'up' in keys_pressed:
        car_vel[0] += CAR_SPEED * math.cos(math.radians(car_angle[0]))
        car_vel[1] += CAR_SPEED * math.sin(math.radians(car_angle[0]))
    if 'down' in keys_pressed:
        car_vel[0] -= CAR_SPEED * math.cos(math.radians(car_angle[0]))
        car_vel[1] -= CAR_SPEED * math.sin(math.radians(car_angle[0]))
    car_pos[0] += car_vel[0]
    car_pos[1] += car_vel[1]
    car_vel[0] *= 0.965
    car_vel[1] *= 0.965

    main_car_movement()



    

    glutSwapBuffers()


def keyboard(key, x, y):
    global keys_pressed

    if key == b'a':
        keys_pressed.add('left')
        # print(keys_pressed)
    elif key == b'd':
        keys_pressed.add('right')
        # print(keys_pressed)
    elif key == b'w':
        keys_pressed.add('up')
        # print(keys_pressed)
    elif key == b's':
        keys_pressed.add('down')
        # print(keys_pressed)
    elif key == b'q':
        keys_pressed.add('base')
        print(keys_pressed)
    elif key == b'e':
        keys_pressed.add('notbase')
        print(keys_pressed)


def keyboard_up(key, x, y):
    global keys_pressed

    if key == b'a':
        keys_pressed.remove('left')
        # print(keys_pressed)

    elif key == b'd':
        keys_pressed.remove('right')
        # print(keys_pressed)

    elif key == b'w':
        keys_pressed.remove('up')
        # print(keys_pressed)

    elif key == b's':
        keys_pressed.remove('down')
        # print(keys_pressed)


def Timer(v):
    draw()
    glutTimerFunc(time_interval, Timer, 1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"FORSA GAME")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyboard_up)
    # glutMouseFunc(MouseMotion)
    glutTimerFunc(time_interval, Timer, 50)
    init()
    load_setup_textures()
    glutMainLoop()


current_dir = os.getcwd().strip('\/core')

if os.name == "posix" and not (current_dir.startswith('/')):  # if linux
    current_dir = "/" + current_dir

os.chdir(current_dir)
main()
