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
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QT_VERSION_STR, Qt, QUrl

from app_guis import Ui_ExamAppCreator, Ui_AboutWindow
import methods

PY_VER = sys.version[:3]

#app class goes here
class App(QtWidgets.QMainWindow):
	"""docstring for App"""
	def __init__(self, parent=None):
		super(App, self).__init__(parent)
		self.screen_size = QtWidgets.QDesktopWidget().availableGeometry()
		self.enabled = False
		self.file_name = ('','')
		self.file_modified = False #change this value when anything is modified

		methods.dark_theme(app)
		#self.load_data()
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
		self.examcreator_gui.actionAbout.triggered.connect(self.open_about_window)
		#set the text etc

		self.examcreator_gui.closeEvent.connect(self.closeEvent1)

		#Show window
		self.examcreator_gui.show()

	def closeEvent1(self, event):
	    print ("Closing again")
	    #self.destory()

	def new_file(self):
		#Check to see if a file is open and has been changed
		if self.file_name[0] != '' and self.file_modified:
			#msg box do you want to save your changes
			print('open msg box ask if you want to save your changes')
			self.save_file()
		elif self.file_name[0] == '' and self.file_modified:
			# save a new file
			self.save_as_file()
		else:
			#enable the main screen to work with
			self.file_modified = True
			print('new file open')

	def open_file(self):
		#Open file browser window and choose a csv file
		self.file_name = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption="Select CSV File", directory="./resources", filter="CSV Files (*.csv)")
		#populate any lists/vairables by reading the csv file
		try:
			if self.file_name[0] != '':
				with open(self.file_name[0], "r") as open_file:
					csv_reader = csv.DictReader(open_file)
					for line in csv_reader:
						pass
		except Exception as e:
			#Open Message box with error message
			print(e)

	def save_file(self):
		#Check to see if already saved if not open file window same as save as
		try:
			if self.file_name[0] != '':
				with open(self.file_name[0], "w") as new_file:
					csv_writer = csv.writer(new_file, delimiter = ',')
					csv_writer.writerow("First write")
			elif self.file_modified:
				self.save_as_file()
		except Exception as e:
			#Open Message box with error message
			print(e)

	def save_as_file(self):
		#open save dialog window to save file
		self.file_name = QtWidgets.QFileDialog.getSaveFileName(parent=self, caption="Save As", directory="./resources", filter="CSV Files (*.csv)")
		try:
			if self.file_name[0] != '':
				with open(self.file_name[0], "w") as new_file:
					csv_writer = csv.writer(new_file, delimiter = ',')
					csv_writer.writerow("First write")
		except Exception as e:
			#Open Message box with error message
			print(e)

	def exit_app(self):
		#Check to see if the open file has been saved
		#If file is not saved:
			#Open a message box
		sys.exit(app.exec_())

	def create_class_list(self):
		pass

	def create_exam_list(self):
		pass

	def create_student_list(self):
		pass

	def open_help(self):
		pass
		#os.startfile('About.txt')

	def open_about_window(self):
		self.about_window = Ui_AboutWindow()
		self.about_window.setWindowTitle("About Exam Creator (Version: {})".format(__version__))
		methods.screen_location(wn=self.about_window, win_type=False, avail_geom=self.screen_size)

		self.about_window.VersionLabel.setText("version {}".format(__version__))

		self.about_window.show()

print(sys.executable)

if __name__ == '__main__':
	print("Qt version:", QT_VERSION_STR)
	print("Author:", __author__)
	print("App version:",__version__)

	app = QApplication(sys.argv)
	main_app = App()

	sys.exit(app.exec_())