from OpenGL.GL import *
from Textures import *


class Rectangle:
    index = -1

    def __init__(self, left, right, bottom, top):
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom
        Rectangle.index += 1
        self.idx = Rectangle.index
        # print(self.idx)


    def draw_texture(self):
            drawHelper(self.idx, self.left, self.right, self.top, self.bottom)


    def drawRectangle(self, color=(1, 1, 1)):
        glColor3f(color[0], color[1], color[2])
        glBegin(GL_QUADS)
        glVertex2f(self.left, self.bottom)
        glVertex2f(self.right, self.bottom)
        glVertex2f(self.right, self.top)
        glVertex2f(self.left, self.top)
        glEnd()




