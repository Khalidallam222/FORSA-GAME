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
textureIdentifiers = [i for i in range(16)]


def setupHelper(texture, textureIdentifier, width, height):
    glEnable(GL_BLEND)  # FOR BLENDING
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # FOR BLENDING
    glBindTexture(GL_TEXTURE_2D, textureIdentifier)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, width, height, GL_RGBA, GL_UNSIGNED_BYTE,
                      texture)


def loadHelper(path, index):
    image = pygame.image.load(path)

    binaryImage = pygame.image.tostring(image, "RGBA", True)
    setupHelper(
        binaryImage, textureIdentifiers[index], image.get_width(), image.get_height())


def load_setup_textures():
    glEnable(GL_TEXTURE_2D)
    glGenTextures(len(textureIdentifiers), textureIdentifiers)

    loadHelper("World Assets/world.png", 0)
    loadHelper("World Assets/porche_911.png", 1)

    loadHelper("World Assets/car-yellow.png", 2)
    loadHelper("World Assets/car-red.png", 3)
    loadHelper("World Assets/car-purple.png", 4)

    loadHelper("World Assets/car-purple-2.png", 5)
    loadHelper("World Assets/car-pink.png", 6)
    loadHelper("World Assets/car-orange.png", 7)

    loadHelper("World Assets/car-green.png", 8)
    loadHelper("World Assets/car-blue.png", 9)
    loadHelper("World Assets/car-red.png", 10)

    loadHelper("World Assets/car-purple-2.png", 11)
    loadHelper("World Assets/car-pink.png", 12)
    loadHelper("World Assets/car-orange.png", 13)
    loadHelper("World Assets/start.png", 14)
    loadHelper("World Assets/start-button.png", 15)

def drawHelper(textureIndex, left, right, top, bottom):
    glBindTexture(GL_TEXTURE_2D, textureIdentifiers[textureIndex])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex(left, bottom, 0)
    glTexCoord2f(1, 0.0)
    glVertex(right, bottom, 0)
    glTexCoord2f(1, 1)
    glVertex(right, top, 0)
    glTexCoord2f(0.0, 1)
    glVertex(left, top, 0)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, -1)
def drawTextures(quad):
    # TODO: Draw all textures here [ WORLD , MAIN CAR , OTHER CARS(12)]
    drawHelper(quad.idx, quad.left, quad.right, quad.top, quad.bottom)
