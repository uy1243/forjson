# -*- coding: utf-8 -*-
"""
Main Game class for PyQt QML Game Of Life.

Hosted at https://github.com/pkobrien/qml-game-of-life
"""

from PyQt5.QtCore import (pyqtProperty, pyqtSignal, pyqtSlot, QObject, 
                          QTimer, QVariant)

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from token import STRING
from User import User


import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

class Game(QObject):
    
    login = pyqtSignal(QVariant, arguments=['te1'])


    def __init__(self):
        super(Game, self).__init__()

    #===========================================================================
    # @pyqtProperty(int, notify=login)
    # def height(self):
    #     return 1
    #===========================================================================
    @pyqtSlot(QVariant,QVariant)
    def flogin(self,name,passw):
        print name,passw
        if (name=='u') & (passw=='1'):
            self.login.emit(1)


    @pyqtSlot()
    def fcancel(self):
        """Update grid with the next generation of living cells."""
        print 'cc'


if __name__ == '__main__':
    #===========================================================================
    # import os
    # import sys
    # app = QGuiApplication(sys.argv)
    # engine = QQmlApplicationEngine()
    # context = engine.rootContext()
    # game = Game()
    # context.setContextProperty('loginCh', game)
    # qml_filename = os.path.join('qml/main.qml')
    # engine.load(qml_filename)
    # sys.exit(app.exec_())
    #===========================================================================
    
    
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    appLabel = QQuickView()
    game = Game()
    user=User()
    appLabel.rootContext().setContextProperty('loginCh', game)
    appLabel.rootContext().setContextProperty('user', user)
    appLabel.setSource(QUrl('qml/Loginw.qml'))

    # Show the Label
    appLabel.show()

    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
