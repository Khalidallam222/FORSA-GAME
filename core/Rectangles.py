from OpenGL.GL import *
from Textures import *


class Rectangle:
    index = -1

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.right = x + width
        self.left = x
        self.top = y + height
        self.bottom = y
        self.idx = Rectangle.index + 1
    def draw_texture(self, texture_index):
        drawHelper(texture_index, self.left,
                   self.right, self.top, self.bottom)

    def drawRectangle(self, color=(1, 1, 1)):
        glColor3f(color[0], color[1], color[2])
        glBegin(GL_QUADS)
        glVertex2f(self.left, self.bottom)
        glVertex2f(self.right, self.bottom)
        glVertex2f(self.right, self.top)
        glVertex2f(self.left, self.top)
        glEnd()


class MainCar:
    def __init__(self, CAR_WIDTH, CAR_LENGTH, trans_x, trans_y, theta):
        glPushMatrix()
        glTranslatef(trans_x, trans_y, 0)
        glRotatef(theta, 0, 0, 1)
        drawHelper(1, -CAR_WIDTH / 2, CAR_WIDTH / 2, CAR_LENGTH / 2, -CAR_LENGTH / 2)
        glPopMatrix()


class Car_Model:
    def __init__(self, left, bottom, right, top, car_Direction, obstacle_speed):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        self.car_Direction = car_Direction * obstacle_speed

    def draw_texture(self, texture_index):
        drawHelper(texture_index, self.left, self.right, self.top, self.bottom)

    def draw_car(self):
        glBegin(GL_POLYGON)
        glVertex(self.left, self.bottom, 0)
        glVertex(self.right, self.bottom, 0)
        glVertex(self.right, self.top, 0)
        glVertex(self.left, self.top, 0)
        glEnd()
