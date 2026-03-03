from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

"""
Assignment-2: Draw a Rectangle
"""

team1 = [(0,0)] * 5   
team2 = [(0,0)] * 5

def randomize_positions():
    """Fill team lists with random positions in range [-50,50]."""
    global team1, team2
    team1 = [(random.uniform(-50, 50), random.uniform(-50, 50)) for _ in range(5)]
    team2 = [(random.uniform(-50, 50), random.uniform(-50, 50)) for _ in range(5)]

def display():
    glClear(GL_COLOR_BUFFER_BIT)          

    # White middle line (vertical)
    glColor3f(1, 1, 1)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(0, -50)
    glVertex2f(0, 50)
    glEnd()

    # Team 1 (red)
    glColor3f(1, 0, 0)
    glPointSize(12)
    glBegin(GL_POINTS)
    for x, y in team1:
        glVertex2f(x, y)
    glEnd()

    # Team 2 (blue)
    glColor3f(0, 0, 1)
    glBegin(GL_POINTS)
    for x, y in team2:
        glVertex2f(x, y)
    glEnd()

    glutSwapBuffers()

def timer(value):
    randomize_positions()
    glutPostRedisplay()
    glutTimerFunc(5000, timer, 0)   


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Two Teams")   


glClearColor(0, 0.5, 0, 1)          
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-50, 50, -50, 50)        
glMatrixMode(GL_MODELVIEW)

randomize_positions()                 

glutDisplayFunc(display)
glutTimerFunc(5000, timer, 0)
glutMainLoop()