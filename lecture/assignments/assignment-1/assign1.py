from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

"""
Assignment-1: Draw a Rectangle
"""


def draw_rectangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)                     

    glBegin(GL_LINE_LOOP)               

    # Bottom-left
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(-5, -5)

    # Top-left 
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(-5, 5)

    # Top-right 
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(5, 5)

    # Bottom-right 
    glColor3f(1.0, 1.0, 0.0)
    glVertex2i(5, -5)

    glEnd()
    glFlush()



glutInit()
glutInitWindowSize(600, 400)
glutCreateWindow(b"Rectangle")
glutDisplayFunc(draw_rectangle)       
gluOrtho2D(-10, 10, -10, 10)          
glutMainLoop()