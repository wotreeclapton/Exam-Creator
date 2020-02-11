#! python 3
'''
EXAM CREATOR LAUNCHER developed by Mr Steven J walden
    Feb. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

__author__ = 'Mr Steven J Walden'
__version__ = '1.0.0'

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QT_VERSION_STR, Qt, QUrl

from app_guis import Ui_ExamAppCreator
import methods

PY_VER = sys.version[:3]

#app class goes here
class App(QtWidgets.QMainWindow):
	"""docstring for App"""
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.screen_size = QtWidgets.QDesktopWidget().availableGeometry()
		self.enabled = False

		methods.dark_theme(app)
		self.load_data()
		self.open_main_window()


	def load_data(self):
		pass

	def open_main_window(self):
		self.examcreator_gui = Ui_ExamAppCreator(self.screen_size, enabled=self.enabled)
		methods.screen_location(wn=self.examcreator_gui, win_type=True, avail_geom=self.screen_size)
		self.examcreator_gui.setWindowTitle("Exam Creator V{}".format(__version__))

		#Connect the methods
		self.examcreator_gui.actionNew.triggered.connect(self.new_file)
		self.examcreator_gui.actionOpen.triggered.connect(self.open_file)
		self.examcreator_gui.actionSave.triggered.connect(self.save_file)
		self.examcreator_gui.actionSave_As.triggered.connect(self.save_as_file)
		self.examcreator_gui.actionExit.triggered.connect(self.exit_app)
		self.examcreator_gui.actionCreate_Classlist.triggered.connect(self.create_class_list)
		self.examcreator_gui.actionCreate_Examlist.triggered.connect(self.create_exam_list)
		self.examcreator_gui.actionCreate_Studentlist.triggered.connect(self.create_student_list)
		self.examcreator_gui.actionView_Help.triggered.connect(self.open_help)
		self.examcreator_gui.actionAbout.triggered.connect(self.show_readme_file)
		#set the text etc

		#Show window
		self.examcreator_gui.show()

	def new_file(self):
		pass

	def open_file(self):
		pass

	def save_file(self):
		pass

	def save_as_file(self):
		pass

	def exit_app(self):
		pass

	def create_class_list(self):
		pass

	def create_exam_list(self):
		pass

	def create_student_list(self):
		pass

	def open_help(self):
		pass

	def show_readme_file(self):
		os.startfile('About.txt')


print(sys.executable)

if __name__ == '__main__':
    print("Qt version:", QT_VERSION_STR)
    print("Author:", __author__)
    print("App version:",__version__)

    app = QtWidgets.QApplication(sys.argv)
    main_app = App()

sys.exit(app.exec_())