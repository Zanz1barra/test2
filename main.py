import sys
# Импортируем наш интерфейс из файла
from window_work import *
from PyQt4 import QtCore, QtGui

class MyWin(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui =
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    def MyFunction(self):
        pass

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())