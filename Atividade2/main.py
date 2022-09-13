import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def triangulo():
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)

    glEnd()

def main():
    pygame.init()
    display = (800, 700)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(80,
                   (display[0]/display[1]),
                   1,
                   20
    )
    glTranslatef(
        2, #X
        2, #Y
    )
    glRotatef(80,  # aqui esta o angulo de retação
              2,   #X
              0
              )

    glColor3f(255,255,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        triangulo()
        pygame.display.flip()
        #pygame.time.wait(10)


main()