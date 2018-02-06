import sys
from PyQt4 import QtGui, QtCore


class HelloQt(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.setWindowTitle("Hello Qt")

        # Vertical layout
        self.layout = QtGui.QVBoxLayout(self)

        # Create widgets
        self.label = QtGui.QLabel("What's your name?")
        self.name = QtGui.QLineEdit()
        self.output = QtGui.QLineEdit()
        self.output.setReadOnly(True)

        # Add widgets to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.output)

        # Connect self.name with self.sayHello(name) when text is changed
        self.connect(self.name, QtCore.SIGNAL("textChanged(const QString&)"), self.sayHello)

    def sayHello(self, name):
        # Set the output text
        self.output.setText("Hello " + name + "!")


if __name__ == "__main__":
    # Create QApplication
    app = QtGui.QApplication(sys.argv)

    # Create a HelloQt window and show it
    helloqt = HelloQt()
    helloqt.show()

    # Run the mainloop
    sys.exit(app.exec_())