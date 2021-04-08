#not needed for lib
import sys

#Import Qt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

#time
import time

#Lib to make screenshot
import pyscreenshot

#Box
class Box(QWidget):
	def __init__(self, colour, opacity):
		super().__init__()

		#transparency
		self.setWindowOpacity(opacity)

		#always on top and hite title bar
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

		# setting up the border and colour
		self.setStyleSheet(f"border :3px solid {colour}; background-color: {colour};")

		#set Geometry
		self.setGeometry(0, 0, 0, 0)

	#resize self that 2 of it diagonals are on end and begin
	def Resize(self, begin, end):
		Sub = end - begin
		self.setGeometry((Sub.x() < 0)*end.x() + (Sub.x() >= 0)*begin.x(), (Sub.y() < 0)*end.y() + (Sub.y() >= 0)*begin.y(), abs(Sub.x()), abs(Sub.y()))
#screen shooter class
class SS(QWidget):
	def __init__(self, colour, opacity):
		#Call parent class init
		super().__init__()

		#set Vars
		self.colour = colour
		self.opacity = opacity

		#always on top and hite title bar
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

		#transparency
		self.setWindowOpacity(0)

		#opening window in maximized size
		self.showFullScreen()

		#Set cursor
		self.setCursor(Qt.CrossCursor)

		#grab mouse
		self.grabMouse()

		#Get screenshot Flag
		#self.img = False

		#Position
		self.begin = QtCore.QPoint()
		self.end = QtCore.QPoint()

		#show all widgets
		self.show()

	#Make screenshot
	def ScreenShoot(self):
		#Get smaler and greater
		x = self.end.x()*(self.end.x() < self.begin.x()) + self.begin.x()*(self.end.x() >= self.begin.x())
		y = self.end.y()*(self.end.y() < self.begin.y()) + self.begin.y()*(self.end.y() >= self.begin.y())

		return pyscreenshot.grab(bbox=(x, y, self.end.x() + self.begin.x() - x, self.end.y() + self.begin.y() - y))
	
	#handle mouses
	def mousePressEvent(self, event):
		self.begin = event.pos()
		self.end = event.pos()

		self.Box = Box(self.colour, self.opacity)
		self.Box.show()

	def mouseMoveEvent(self, event):
		self.end = event.pos()
		self.Box.Resize(self.begin, self.end)

	def mouseReleaseEvent(self, event):
		self.Box.close()	

		#take screenshoot
		#self.img = self.ScreenShoot()

		self.close()

#I wonder what it does? Time is "adjusted" for 30fps
def MakeScreenShoot(colour, opacity):
	app = QApplication(sys.argv)
	ex = SS(colour, opacity)

	app.exec()
	return ex.ScreenShoot()
