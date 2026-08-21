from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Circle center and radius
xc, yc = 250, 250
r = 100

# Draw a pixel
def drawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

# Plot the 8 symmetric points
def plotCirclePoints(xc, yc, x, y):
    drawPixel(xc + x, yc + y)
    drawPixel(xc - x, yc + y)
    drawPixel(xc + x, yc - y)
    drawPixel(xc - x, yc - y)

    drawPixel(xc + y, yc + x)
    drawPixel(xc - y, yc + x)
    drawPixel(xc + y, yc - x)
    drawPixel(xc - y, yc - x)

# Midpoint Circle Algorithm
def midpointCircle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        plotCirclePoints(xc, yc, x, y)

        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x - 2 * y + 1

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)   # Red Circle
    glPointSize(3)

    midpointCircle(xc, yc, r)

    glFlush()

# Initialize
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)

# Main
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Midpoint Circle Drawing Algorithm")

init()
glutDisplayFunc(display)

glutMainLoop()