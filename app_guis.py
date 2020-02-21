'''Exam Creator Guis developed by Mr Steven J Walden
    Dec. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See license at end of file]
'''

import sys
from PyQt5 import QtWidgets, QtGui, QtCore, QtMultimediaWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer


class Ui_ExamAppCreator(QtWidgets.QMainWindow):
	"""docstrbing for MyApp"""
	def __init__(self, screen_size, modified, parent=None):
		super(Ui_ExamAppCreator, self).__init__(parent)
		self.screen_height = screen_size.height()
		self.screen_width = round((self.screen_height - 32) * 1.3)
		self.modified = modified
		#print("Ori W=1200 New W={} Ori H=924 New W={}".format(self.screen_width,self.screen_height))
		self.initUI()

	def initUI(self):
		self.resize(self.screen_width, self.screen_height - 32)
		self.setMinimumSize(800, 600) # orig size was 1200x924
		self.setMaximumSize(1200, self.screen_height - 32)
		self.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.setWindowTitle("Exam Creator")

		self.add_widgets()
		self.add_layouts()
		self.add_menus()
		self.add_labels()
		self.add_buttons()
		self.tool_status_tips()
		self.tab_order()
		self.kb_shortcuts()

	def closeEvent(self, event):
		if self.modified:
			self.msgbox = QMessageBox()
			self.msgbox.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
			self.msgbox.setIcon(QMessageBox.Warning)
			self.msgbox.setWindowTitle("Exam Creator")
			self.msgbox.setDefaultButton(QMessageBox.Save)
			self.msgbox.setStandardButtons(QMessageBox.Save|QMessageBox.Discard|QMessageBox.Cancel)
			self.msgbox.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
			self.msgbox.setText("Do you want to save changes to untitled?")

			event.ignore()

			if self.msgbox.exec() == QMessageBox.Discard:
				event.accept()
			elif self.msgbox.exec() == QMessageBox.Save:
				print('Save it')
			else:
				event.ignore()
			# 	event.ignore()
			# if self.msgbox.exec() == QMessageBox.Cancel:
			# 	event.ignore()

		event.accept()

	def add_widgets(self):
		self.centralwidget = QtWidgets.QWidget(self)

		self.menubar = QtWidgets.QMenuBar(self)
		#self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		#self.menubar.setObjectName("menubar")

		self.MainVerticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

		self.TopWidget = QtWidgets.QFrame(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		self.TopWidget.setSizePolicy(sizePolicy)
		self.TopWidget.setMinimumWidth(600)
		self.TopWidget.setMinimumHeight(103)
		self.TopWidget.setMaximumHeight(103)

		self.TopWidget1 = QtWidgets.QFrame(self.centralwidget)
		self.TopWidget1.setSizePolicy(sizePolicy)
		self.TopWidget1.setMinimumWidth(1)
		self.TopWidget1.setMinimumHeight(103)
		self.TopWidget1.setMaximumHeight(103)

		self.TopWidget2 = QtWidgets.QFrame(self.centralwidget)
		self.TopWidget2.setSizePolicy(sizePolicy)
		self.TopWidget2.setMinimumWidth(290)
		self.TopWidget2.setMinimumHeight(103)
		self.TopWidget2.setMaximumHeight(103)

		self.videoWidget = QtMultimediaWidgets.QVideoWidget(self.centralwidget)

		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		font = QtGui.QFont()
		font.setPointSize(15)
		font.setBold(True)
		font.setItalic(True)
		font.setWeight(75)
		self.tabWidget.setFont(font)
		self.tabWidget.setEnabled(False)

		self.AnswerATab = QtWidgets.QWidget()
		self.TabTextLayoutA = QtWidgets.QHBoxLayout(self.AnswerATab)
		self.TabTextLayoutA.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerATab, "Answer-A")

		self.AnswerBTab = QtWidgets.QWidget()
		self.TabTextLayoutB = QtWidgets.QHBoxLayout(self.AnswerBTab)
		self.TabTextLayoutB.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerBTab, "Answer-B")

		self.AnswerCTab = QtWidgets.QWidget()
		self.TabTextLayoutC = QtWidgets.QHBoxLayout(self.AnswerCTab)
		self.TabTextLayoutC.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerCTab, "Answer-C")

		self.AnswerDTab = QtWidgets.QWidget()
		self.TabTextLayoutD = QtWidgets.QHBoxLayout(self.AnswerDTab)
		self.TabTextLayoutD.setContentsMargins(330, -1, -1, -1)
		self.tabWidget.addTab(self.AnswerDTab, "Answer-D")

		self.CheckboxFrame = QtWidgets.QFrame(self.centralwidget)
		self.CheckboxFrame.setSizePolicy(sizePolicy)
		self.CheckboxFrame.setMinimumWidth(600)
		self.CheckboxFrame.setMinimumHeight(46)
		self.CheckboxFrame.setMaximumHeight(46)

		self.CheckboxFrame1 = QtWidgets.QFrame(self.centralwidget)
		self.CheckboxFrame1.setSizePolicy(sizePolicy)
		self.CheckboxFrame1.setMinimumWidth(1)
		self.CheckboxFrame1.setMinimumHeight(46)
		self.CheckboxFrame1.setMaximumHeight(46)

		self.CheckboxFrame2 = QtWidgets.QFrame(self.centralwidget)
		self.CheckboxFrame2.setSizePolicy(sizePolicy)
		self.CheckboxFrame2.setMinimumWidth(278)
		self.CheckboxFrame2.setMinimumHeight(46)
		self.CheckboxFrame2.setMaximumHeight(46)


		self.BottomFrame = QtWidgets.QFrame(self.centralwidget)
		self.BottomFrame.setSizePolicy(sizePolicy)
		self.BottomFrame.setMinimumWidth(390)
		self.BottomFrame.setMaximumWidth(390)
		self.BottomFrame.setMinimumHeight(38)
		self.BottomFrame.setMaximumHeight(38)

		self.BottomFrame2 = QtWidgets.QFrame(self.centralwidget)
		self.BottomFrame2.setSizePolicy(sizePolicy)
		self.BottomFrame2.setMinimumWidth(240)
		self.BottomFrame2.setMaximumWidth(240)
		self.BottomFrame2.setMinimumHeight(38)
		self.BottomFrame2.setMaximumHeight(38)

		self.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(self)

	def add_layouts(self):
		self.setMenuBar(self.menubar)
		self.TopLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.TopLayout)
		self.TopLayout.addWidget(self.TopWidget)
		self.TopLayout.addWidget(self.TopWidget1)
		self.TopLayout.addWidget(self.TopWidget2)
		# self.MainVerticalLayout.addWidget(self.TopWidget)
		self.QuestionsAndVideoLayoutLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.QuestionsAndVideoLayoutLayout)

		self.MainVerticalLayout.addWidget(self.tabWidget)


		#add a layout to the checkbox frame
		self.CheckBoxLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.CheckBoxLayout)

		self.CheckBoxLayout.addWidget(self.CheckboxFrame)
		self.CheckBoxLayout.addWidget(self.CheckboxFrame1)
		self.CheckBoxLayout.addWidget(self.CheckboxFrame2)

		self.BottomLayout = QtWidgets.QHBoxLayout()
		self.MainVerticalLayout.addLayout(self.BottomLayout)
		self.BottomLayout.addWidget(self.BottomFrame)

		self.BottomLayout.addWidget(self.BottomFrame2)

		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
		self.mediaPlayer.setVideoOutput(self.videoWidget)

		self.setStatusBar(self.statusbar)

	def add_menus(self):
		font = QtGui.QFont()
		font.setPointSize(10)
		self.menubar.setFont(font)
		self.menuFile = QtWidgets.QMenu(self.menubar)
		# self.menuFile.setObjectName("menuFile")
		self.menuCreate = QtWidgets.QMenu(self.menubar)
		# self.menuCreate.setObjectName("menuCreate")
		self.menuHelp = QtWidgets.QMenu(self.menubar)

		self.actionNew = QtWidgets.QAction(self)
		self.actionOpen = QtWidgets.QAction(self)
		self.actionSave = QtWidgets.QAction(self)
		self.actionSave_As = QtWidgets.QAction(self)
		self.actionExit = QtWidgets.QAction(self)
		self.actionCreate_Classlist = QtWidgets.QAction(self)
		self.actionCreate_Examlist = QtWidgets.QAction(self)
		self.actionCreate_Studentlist = QtWidgets.QAction(self)
		self.actionView_Help = QtWidgets.QAction(self)
		self.actionAbout = QtWidgets.QAction(self)

		self.menuFile.addAction(self.actionNew)
		self.menuFile.addAction(self.actionOpen)
		self.menuFile.addAction(self.actionSave)
		self.menuFile.addAction(self.actionSave_As)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionExit)

		self.menuCreate.addAction(self.actionCreate_Classlist)
		self.menuCreate.addAction(self.actionCreate_Examlist)
		self.menuCreate.addAction(self.actionCreate_Studentlist)

		self.menuHelp.addAction(self.actionView_Help)
		self.menuHelp.addSeparator()
		self.menuHelp.addAction(self.actionAbout)

		self.menuFile.setTitle("File")
		self.menuCreate.setTitle("Create")
		self.menuHelp.setTitle("Help")

		self.actionNew.setText("New")
		self.actionOpen.setText("Open...")
		self.actionSave.setText("Save")
		self.actionSave_As.setText("Save As...")
		self.actionExit.setText("Exit")

		self.actionCreate_Classlist.setText("Class List")
		self.actionCreate_Examlist.setText("Exam List")
		self.actionCreate_Studentlist.setText("Student List")

		self.actionView_Help.setText("View Help")
		self.actionAbout.setText("About Exam Creator")

		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuCreate.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

	def add_labels(self):
		self.SchoolLabel = QtWidgets.QLabel(self.TopWidget)
		self.SchoolLabel.setMinimumSize(QtCore.QSize(75, 97))
		self.SchoolLabel.setGeometry(4, 4, 75, 97)
		self.SchoolLabel.setPixmap(QtGui.QPixmap("img/School logo75x97_grad.png"))

		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		self.ExamTitle = QtWidgets.QLabel(self.TopWidget)
		self.ExamTitle.setGeometry(95, 10, 201, 51)
		self.ExamTitle.setText("Exam Title")
		self.ExamTitle.setFont(font)
		self.ExamTitle.setAlignment(QtCore.Qt.AlignTop)
		# self.ExamTitle.setEnabled(False)

		self.ExamTime = QtWidgets.QLabel(self.TopWidget)
		self.ExamTime.setGeometry(95, 61, 201, 51)
		self.ExamTime.setText("?: Mins")
		self.ExamTime.setFont(font)
		self.ExamTime.setAlignment(QtCore.Qt.AlignTop)

		font.setItalic(True)
		font.setPointSize(14)
		self.QuestionNumberLabel = QtWidgets.QLabel(self.TopWidget2)
		self.QuestionNumberLabel.setGeometry(10, 10, 186, 30)
		self.QuestionNumberLabel.setFont(font)
		self.QuestionNumberLabel.setText("Question Number:")

		self.QuestionNumber = QtWidgets.QLabel(self.TopWidget2)
		self.QuestionNumber.setGeometry(196, 10, 30, 30)
		self.QuestionNumber.setFont(font)
		self.QuestionNumber.setText("?")

		self.OutOfQuestionLabel = QtWidgets.QLabel(self.TopWidget2)
		self.OutOfQuestionLabel.setGeometry(226, 10, 42, 30)
		self.OutOfQuestionLabel.setFont(font)
		self.OutOfQuestionLabel.setText("/?")

		font.setPointSize(20)
		self.Questions = QtWidgets.QLabel(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHeightForWidth(self.Questions.sizePolicy().hasHeightForWidth())
		self.Questions.setSizePolicy(sizePolicy)
		self.Questions.setFont(font)
		self.Questions.setFrameShape(QtWidgets.QFrame.Panel)
		self.Questions.setFrameShadow(QtWidgets.QFrame.Raised)
		self.Questions.setAlignment(QtCore.Qt.AlignTop)
		self.Questions.setWordWrap(True)
		self.Questions.setText("Questions")
		self.QuestionsAndVideoLayoutLayout.addWidget(self.Questions)

		self.QuestionsAndVideoLayoutLayout.addWidget(self.videoWidget)

		self.AnswerTextA = QtWidgets.QLabel(self.AnswerATab)
		self.AnswerTextA.setFont(font)
		self.AnswerTextA.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextA.setWordWrap(True)
		self.AnswerTextA.setText("TextLabel")
		self.TabTextLayoutA.addWidget(self.AnswerTextA)

		self.AnswerTextB = QtWidgets.QLabel(self.AnswerBTab)
		self.AnswerTextB.setFont(font)
		self.AnswerTextB.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextB.setWordWrap(True)
		self.AnswerTextB.setText("TextLabel")
		self.TabTextLayoutB.addWidget(self.AnswerTextB)

		self.AnswerTextC = QtWidgets.QLabel(self.AnswerCTab)
		self.AnswerTextC.setFont(font)
		self.AnswerTextC.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextC.setWordWrap(True)
		self.AnswerTextC.setText("TextLabel")
		self.TabTextLayoutC.addWidget(self.AnswerTextC)

		self.AnswerTextD = QtWidgets.QLabel(self.AnswerDTab)
		self.AnswerTextD.setFont(font)
		self.AnswerTextD.setAlignment(QtCore.Qt.AlignTop)
		self.AnswerTextD.setWordWrap(True)
		self.AnswerTextD.setText("TextLabel")
		self.TabTextLayoutD.addWidget(self.AnswerTextD)

	def add_buttons(self):
		bfont = QtGui.QFont()
		bfont.setPointSize(12)
		bfont.setBold(True)
		bfont.setItalic(True)
		self.BackButton = QtWidgets.QPushButton(self.CheckboxFrame2)
		self.BackButton.setGeometry(10, 6, 130, 32)
		self.BackButton.setFont(bfont)
		self.BackButton.setText("       Back")
		self.BackButton.setIcon(QtGui.QIcon("img/back_button.png"))
		self.BackButton.setIconSize(QtCore.QSize(32,32))
		self.BackButton.setEnabled(False)

		self.ForwardButton = QtWidgets.QPushButton(self.CheckboxFrame2)
		self.ForwardButton.setGeometry(142, 6, 130, 32)
		self.ForwardButton.setFont(bfont)
		self.ForwardButton.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.ForwardButton.setText("         Next")
		self.ForwardButton.setIcon(QtGui.QIcon("img/forward_button.png"))
		self.ForwardButton.setIconSize(QtCore.QSize(32,32))
		self.ForwardButton.setEnabled(False)

	def tool_status_tips(self):
		self.tabWidget.setStatusTip("Click to view possible answers.")
		self.ForwardButton.setStatusTip("Click to go to the next question.")

	def tab_order(self):
		self.tabWidget.setCurrentIndex(0)
		self.setTabOrder(self.tabWidget, self.ForwardButton)
		self.setTabOrder(self.ForwardButton, self.BackButton)

	def kb_shortcuts(self):
		self.actionNew.setShortcut("Ctrl+N")
		self.actionOpen.setShortcut("Ctrl+O")
		self.actionSave.setShortcut("Ctrl+S")
		self.actionSave_As.setShortcut("Ctrl+Shift+S")

		self.actionCreate_Classlist.setShortcut("Alt+C")
		self.actionCreate_Examlist.setShortcut("Alt+E")
		self.actionCreate_Studentlist.setShortcut("Alt+S")

		self.BackButton.setShortcut("Left")
		self.ForwardButton.setShortcut("Return")

class Ui_AboutWindow(QtWidgets.QWidget):
	"""docstring for Ui_AboutWindow"""
	def __init__(self, parent=None):
		super(Ui_AboutWindow, self).__init__(parent)
		self.resize(320, 360)
		self.setMinimumSize(320, 360)
		self.setMaximumSize(320, 360)
		self.setWindowIcon(QtGui.QIcon("img/ep_program_logo_user_acc_zrP_icon.ico"))
		self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

		self.add_labels()

	def add_labels(self):
		self.AppLogo = QtWidgets.QLabel(self)
		self.AppLogo.setMinimumSize(QtCore.QSize(160, 160))
		self.AppLogo.setGeometry(self.geometry().width()/2 - self.AppLogo.width() / 2, 16, 160, 160)
		self.AppLogo.setPixmap(QtGui.QPixmap("img/Ep logo160x160.png"))
		self.AppLogo.setAlignment(QtCore.Qt.AlignCenter)

		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		self.AppName = QtWidgets.QLabel(self)
		self.AppName.setMinimumSize(QtCore.QSize(160, 50))
		self.AppName.setGeometry(self.geometry().width()/2 - self.AppName.width() / 2, 184, 160, 50)
		self.AppName.setText("Exam Creator")
		self.AppName.setFont(font)
		self.AppName.setAlignment(QtCore.Qt.AlignCenter)

		font.setPointSize(10)
		font.setBold(False)
		self.VersionLabel = QtWidgets.QLabel(self)
		self.VersionLabel.setMinimumSize(QtCore.QSize(120, 50))
		self.VersionLabel.setGeometry(self.geometry().width()/2 - self.VersionLabel.width() / 2, 214, 120, 50)
		self.VersionLabel.setText("")
		self.VersionLabel.setFont(font)
		self.VersionLabel.setAlignment(QtCore.Qt.AlignCenter)

		font.setPointSize(11)
		self.CopyrightLabel = QtWidgets.QLabel(self)
		self.CopyrightLabel.setMinimumSize(QtCore.QSize(280, 50))
		self.CopyrightLabel.setGeometry(self.geometry().width()/2 - self.CopyrightLabel.width() / 2, 260, 280, 50)
		self.CopyrightLabel.setText("Copyright 2020 Mr Steven J Walden.")
		self.CopyrightLabel.setFont(font)
		self.CopyrightLabel.setAlignment(QtCore.Qt.AlignCenter)

		font.setPointSize(10)
		self.RightsLabel = QtWidgets.QLabel(self)
		self.RightsLabel.setMinimumSize(QtCore.QSize(120, 50))
		self.RightsLabel.setGeometry(self.geometry().width()/2 - self.RightsLabel.width() / 2, 290, 120, 50)
		self.RightsLabel.setText("All rights reserved.")
		self.RightsLabel.setFont(font)
		self.RightsLabel.setAlignment(QtCore.Qt.AlignCenter)

class Ui_CreateCSVWindow(object):
    def setupUi(self, CreateCSVWindow):
        CreateCSVWindow.setObjectName("CreateCSVWindow")
        CreateCSVWindow.resize(430, 221)
        CreateCSVWindow.setMinimumSize(QtCore.QSize(430, 221))
        CreateCSVWindow.setMaximumSize(QtCore.QSize(430, 221))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ep_program_logo_user_acc_zrP_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreateCSVWindow.setWindowIcon(icon)
        self.label_3 = QtWidgets.QLabel(CreateCSVWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.Logo_label = QtWidgets.QLabel(CreateCSVWindow)
        self.Logo_label.setEnabled(True)
        self.Logo_label.setGeometry(QtCore.QRect(354, 9, 64, 64))
        self.Logo_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Logo_label.setToolTipDuration(-5)
        self.Logo_label.setText("")
        self.Logo_label.setPixmap(QtGui.QPixmap("img/Ep logo60x60.png"))
        self.Logo_label.setScaledContents(False)
        self.Logo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo_label.setObjectName("Logo_label")
        self.frame = QtWidgets.QFrame(CreateCSVWindow)
        self.frame.setGeometry(QtCore.QRect(10, 80, 411, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(240, 90, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.TabBoxLabel = QtWidgets.QLabel(self.frame)
        self.TabBoxLabel.setGeometry(QtCore.QRect(10, 38, 150, 13))
        self.TabBoxLabel.setObjectName("TabBoxLabel")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(356, 10, 42, 20))
        self.toolButton.setObjectName("toolButton")
        self.FileBox = QtWidgets.QLineEdit(self.frame)
        self.FileBox.setGeometry(QtCore.QRect(10, 10, 340, 20))
        self.FileBox.setObjectName("FileBox")
        self.SheetcomboBox = QtWidgets.QComboBox(self.frame)
        self.SheetcomboBox.setGeometry(QtCore.QRect(10, 58, 190, 22))
        self.SheetcomboBox.setObjectName("SheetcomboBox")
        self.StartRowLabel = QtWidgets.QLabel(self.frame)
        self.StartRowLabel.setGeometry(QtCore.QRect(48, 84, 47, 13))
        self.StartRowLabel.setObjectName("StartRowLabel")
        self.StartColBox = QtWidgets.QLineEdit(self.frame)
        self.StartColBox.setGeometry(QtCore.QRect(10, 102, 26, 20))
        self.StartColBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StartColBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StartColBox.setObjectName("StartColBox")
        self.StartCollabel = QtWidgets.QLabel(self.frame)
        self.StartCollabel.setGeometry(QtCore.QRect(12, 84, 47, 13))
        self.StartCollabel.setObjectName("StartCollabel")
        self.StartRowBox = QtWidgets.QLineEdit(self.frame)
        self.StartRowBox.setGeometry(QtCore.QRect(46, 102, 26, 20))
        self.StartRowBox.setText("")
        self.StartRowBox.setObjectName("StartRowBox")
        self.EndRowLabel = QtWidgets.QLabel(self.frame)
        self.EndRowLabel.setGeometry(QtCore.QRect(140, 84, 47, 13))
        self.EndRowLabel.setObjectName("EndRowLabel")
        self.EndColBox = QtWidgets.QLineEdit(self.frame)
        self.EndColBox.setGeometry(QtCore.QRect(102, 102, 26, 20))
        self.EndColBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EndColBox.setObjectName("EndColBox")
        self.EndRowBox = QtWidgets.QLineEdit(self.frame)
        self.EndRowBox.setGeometry(QtCore.QRect(138, 102, 26, 20))
        self.EndRowBox.setObjectName("EndRowBox")
        self.EndColLabel = QtWidgets.QLabel(self.frame)
        self.EndColLabel.setGeometry(QtCore.QRect(104, 84, 47, 13))
        self.EndColLabel.setObjectName("EndColLabel")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(31, 102, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(123, 102, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CreateCSVWindow)
        self.toolButton.clicked.connect(CreateCSVWindow.browse_for_workbook)
        self.buttonBox.accepted.connect(CreateCSVWindow.ok_button_clicked)
        self.buttonBox.rejected.connect(CreateCSVWindow.cancel_button_clicked)
        self.FileBox.textChanged['QString'].connect(CreateCSVWindow.populate_sheet_cmb)
        QtCore.QMetaObject.connectSlotsByName(CreateCSVWindow)
        CreateCSVWindow.setTabOrder(self.FileBox, self.toolButton)
        CreateCSVWindow.setTabOrder(self.toolButton, self.SheetcomboBox)

    def retranslateUi(self, CreateCSVWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateCSVWindow.setWindowTitle(_translate("CreateCSVWindow", "Create CSV File"))
        self.label_3.setText(_translate("CreateCSVWindow", "Please browse for workbook"))
        self.TabBoxLabel.setText(_translate("CreateCSVWindow", "Choose Sheet name "))
        self.toolButton.setText(_translate("CreateCSVWindow", "..."))
        self.FileBox.setText(_translate("CreateCSVWindow", "Enter file location"))
        self.StartRowLabel.setText(_translate("CreateCSVWindow", "Row"))
        self.StartColBox.setInputMask(_translate("CreateCSVWindow", ">Aa"))
        self.StartCollabel.setText(_translate("CreateCSVWindow", "Col"))
        self.StartRowBox.setInputMask(_translate("CreateCSVWindow", "900"))
        self.EndRowLabel.setText(_translate("CreateCSVWindow", "Row"))
        self.EndColBox.setInputMask(_translate("CreateCSVWindow", ">Aa"))
        self.EndRowBox.setInputMask(_translate("CreateCSVWindow", "900"))
        self.EndColLabel.setText(_translate("CreateCSVWindow", "Col"))
        self.label.setText(_translate("CreateCSVWindow", ":"))
        self.label_2.setText(_translate("CreateCSVWindow", ":"))

# if __name__ == '__main__':
# 	app = QtWidgets.QApplication(sys.argv)
# 	screen_size = QtWidgets.QDesktopWidget().availableGeometry()
# # 	#main_app = Ui_ExamLogin()
# # 	main_app = Ui_ExamQuestions()
# 	main_app = Ui_ExamAppCreator(screen_size)
# 	main_app.show()

# sys.exit(app.exec_())

# Copyright (c) 2020 Steven Walden
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.