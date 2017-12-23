"fui.qss"
from  Mentry1 import *
import sys
import Mentry1
if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    HelloPyQt = QtGui.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(HelloPyQt)

    file = QtCore.QFile('fui.qss')
    file.open(QtCore.QFile.ReadOnly)
    styleSheet = file.readAll()
    styleSheet = unicode(styleSheet, encoding='utf8')
    HelloPyQt.setStyleSheet(styleSheet)

    HelloPyQt.show()

    sys.exit(app.exec_())
