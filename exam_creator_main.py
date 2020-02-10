#! python 3
'''
EXAM CREATOR LAUNCHER developed by Mr Steven J walden
    Feb. 2020
    SAMROIYOD, PRACHUAP KIRI KHAN, THAILAND
[See License.txt file]
'''

__author__ = 'Mr Steven J Walden'
__version__ = '1.0.0'

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QT_VERSION_STR, Qt, QUrl


PY_VER = sys.version[:3]

#app class goes here



print(sys.executable)

if __name__ == '__main__':
    print("Qt version:", QT_VERSION_STR)
    print("Author:", __author__)
    print("App version:",__version__)

    app = QtWidgets.QApplication(sys.argv)
    #main_app = App()

sys.exit(app.exec_())