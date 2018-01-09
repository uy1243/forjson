'''
Created on Jan 6, 2018

@author: yu
'''
from PyQt5.QtCore import (pyqtProperty, pyqtSignal, pyqtSlot, QObject, 
                          QTimer, QVariant)

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from token import STRING


import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

class User(QObject):
    
    useupdate = pyqtSignal(QVariant, arguments=['te1'])


    def __init__(self):
        super(User, self).__init__()

    #===========================================================================
    # @pyqtProperty(int, notify=login)
    # def height(self):
    #     return 1
    #===========================================================================
    @pyqtSlot(QVariant,QVariant)
    def gettail(self,name,passw):
        print name,passw



    @pyqtSlot()
    def getId(self):
        """Update grid with the next generation of living cells."""
        print 'id'