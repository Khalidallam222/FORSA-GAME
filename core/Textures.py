from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame

# from Rectangles import *


""" STEPS
    1. glEnable(GL_TEXTURE_2D)
    2. Load images
    3. to_string
    4. glGenTextures
    5. glBindTexture
    6. glTexParameterf
    7. glTexImage2D
    8. glBindTexture
    9. glTexCoord 
"""

"""textures:world , main car , 12 cars"""
texture_number = 24
global texture

def setupHelper(image_raw_data, texture_index, width, height):
    global texture
    glEnable(GL_BLEND)  # FOR BLENDING
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # FOR BLENDING
    glBindTexture(GL_TEXTURE_2D, texture[texture_index])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)  # GL_NEAREST)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # GL_CLAMP)
    gluBuild2DMipmaps(GL_TEXTURE_2D, 4, width, height, GL_RGBA, GL_UNSIGNED_BYTE, image_raw_data)


def loadHelper(path, texture_index):
    global texture
    image = pygame.image.load(path)

    image_raw_data = pygame.image.tostring(image, "RGBA", True)
    setupHelper(
        image_raw_data, texture_index, image.get_width(), image.get_height())


def load_setup_textures():
    global texture
    # we'll use it to load all needed textures for one time
    glEnable(GL_TEXTURE_2D)
    texture = glGenTextures(texture_number)
    loadHelper("World Assets/LOWER_ROAD.png", 0)
    loadHelper("World Assets/MIDDLE_ROAD.png", 1)
    loadHelper("World Assets/UPPER_ROAD.png", 2)
    loadHelper("World Assets/UPPER_LEFT_ROAD.png", 3)
    loadHelper("World Assets/UPPER_RIGHT_ROAD.png", 4)
    loadHelper("World Assets/rect_L1_1.png", 5)
    loadHelper("World Assets/rect_L2_1.png", 6)
    loadHelper("World Assets/rect_L2_2.png", 7)
    loadHelper("World Assets/rect_L3_1.png", 8)
    loadHelper("World Assets/rect_L3_2.png", 9)
    loadHelper("World Assets/rect_L3_3.png", 10)

    loadHelper("World Assets/car-yellow.png", 11)
    loadHelper("World Assets/car-red.png", 12)
    loadHelper("World Assets/car-purple.png", 13)
    loadHelper("World Assets/car-purple-2.png", 14)
    loadHelper("World Assets/car-pink.png", 15)
    loadHelper("World Assets/car-orange.png", 16)
    loadHelper("World Assets/car-green.png", 17)
    loadHelper("World Assets/car-blue.png", 18)
    loadHelper("World Assets/car-red.png", 19)
    loadHelper("World Assets/car-purple-2.png", 20)
    loadHelper("World Assets/car-pink.png", 21)
    loadHelper("World Assets/car-orange.png", 22)

    loadHelper("World Assets/porche_911.png", 23)


def drawHelper(textureIndex, left, right, top, bottom):
    global texture
    glBindTexture(GL_TEXTURE_2D, texture[textureIndex])
    glBegin(GL_QUADS)
    glTexCoord(0, 0)
    glVertex2f(left, bottom)
    glTexCoord(1, 0)
    glVertex2f(right, bottom)
    glTexCoord(1, 1)
    glVertex2f(right, top)
    glTexCoord(0, 1)
    glVertex2f(left, top)
    glEnd()
    # glBindTexture(GL_TEXTURE_2D, -1)
