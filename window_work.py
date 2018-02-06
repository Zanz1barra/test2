# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_work.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 90, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(110, 120, 104, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Hello World", None))
        self.pushButton.setText(_translate("Form", "print", None))
        self.pushButton.clicked.connect(world)




class dio(QtGui.QDialog):
    def __init__(self, parent=None):
        buttonbox = QtGui.QDialogButtonBox()
        button = buttonbox.addButton("hello",  QtGui.QDialogButtonBox.ActionRole)
       # button.clicked.connect(self.world)
        self.line = QtGui.QLineEdit()
        self.line.setReadOnly(True)


def world(self):
    #self.line.setText("Hello")
    print("h")

        #QtGui.QMessageBox.information(self, "kapec!")

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = Ui_Form()
    mainWin.show()
    sys.exit(app.exec_())