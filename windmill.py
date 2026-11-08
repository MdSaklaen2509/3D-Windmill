from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

width = 900
height = 650
blade_angle = 0
cam_angle = 0

def Ground():
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.65, 0.25)
    glVertex3f(-250, 0, -250)
    glVertex3f(250, 0, -250)
    glVertex3f(250, 0, 250)
    glVertex3f(-250, 0, 250)
    glEnd()

def Box(w, h, d, r, g, b):
    glBegin(GL_QUADS)
    glColor3f(r, g, b)
    glVertex3f(-w, 0, d)
    glVertex3f(w, 0, d)
    glVertex3f(w, h, d)
    glVertex3f(-w, h, d)
    glColor3f(r * 0.8, g * 0.8, b * 0.8)
    glVertex3f(-w, 0, -d)
    glVertex3f(w, 0, -d)
    glVertex3f(w, h, -d)
    glVertex3f(-w, h, -d)
    glColor3f(r * 0.7, g * 0.7, b * 0.7)
    glVertex3f(-w, 0, -d)
    glVertex3f(-w, 0, d)
    glVertex3f(-w, h, d)
    glVertex3f(-w, h, -d)
    glColor3f(r * 0.9, g * 0.9, b * 0.9)
    glVertex3f(w, 0, -d)
    glVertex3f(w, 0, d)
    glVertex3f(w, h, d)
    glVertex3f(w, h, -d)
    glColor3f(r * 0.95, g * 0.95, b * 0.95)
    glVertex3f(-w, h, d)
    glVertex3f(w, h, d)
    glVertex3f(w, h, -d)
    glVertex3f(-w, h, -d)
    glEnd()

def PyramidRoof(w, h, d, r, g, b):
    glBegin(GL_TRIANGLES)
    glColor3f(r, g, b)
    glVertex3f(-w, 0, d)
    glVertex3f(w, 0, d)
    glVertex3f(0, h, 0)
    glColor3f(r * 0.85, g * 0.85, b * 0.85)
    glVertex3f(w, 0, d)
    glVertex3f(w, 0, -d)
    glVertex3f(0, h, 0)
    glColor3f(r * 0.75, g * 0.75, b * 0.75)
    glVertex3f(w, 0, -d)
    glVertex3f(-w, 0, -d)
    glVertex3f(0, h, 0)
    glColor3f(r * 0.9, g * 0.9, b * 0.9)
    glVertex3f(-w, 0, -d)
    glVertex3f(-w, 0, d)
    glVertex3f(0, h, 0)
    glEnd()

def PlacePowerHouse(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    Box(55, 75, 45, 0.95, 0.8, 0.5)
    glTranslatef(0, 75, 0)
    PyramidRoof(65, 50, 55, 0.8, 0.2, 0.15)
    glPopMatrix()

def PlaceTree(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    Box(8, 50, 8, 0.45, 0.25, 0.1)
    glTranslatef(0, 50, 0)
    PyramidRoof(32, 70, 32, 0.1, 0.5, 0.15)
    glPopMatrix()

def Blade():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.9, 0.2)
    glVertex3f(0, 0, 0)
    glVertex3f(12, 85, 0)
    glVertex3f(-12, 85, 0)
    glEnd()

def PlaceWindmill(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    Box(18, 150, 18, 0.75, 0.75, 0.8)
    glTranslatef(0, 140, 20)
    for i in range(4):
        glPushMatrix()
        glRotatef(blade_angle + i * 90, 0, 0, 1)
        Blade()
        glPopMatrix()
    glPopMatrix()

def update(value):
    global blade_angle, cam_angle
    blade_angle = blade_angle + 3.0
    cam_angle = cam_angle + 0.01
    glutPostRedisplay()
    glutTimerFunc(15, update, 0)

def main():
    Ground()
    PlacePowerHouse(-90, 0, 0)
    PlaceTree(-170, 0, 80)
    PlaceTree(160, 0, 70)
    PlaceWindmill(70, 0, 0)

def showScreen():
    glClearColor(0.53, 0.81, 0.98, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, width / height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    eye_x = 380 * math.sin(cam_angle)
    eye_z = 380 * math.cos(cam_angle)
    gluLookAt(eye_x, 170, eye_z, 0, 60, 0, 0, 1, 0)
    main()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(width, height)
glutInitWindowPosition(100, 50)
glutCreateWindow(b"3D Windmill Energy Park - OpenGL GLU")
glutDisplayFunc(showScreen)
glutTimerFunc(0, update, 0)
glutMainLoop()