from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.someFunction()

    def someFunction(self):
#        buttons = [None] * 8
        for i in range(8):
            button = QPushButton("Button {}".format("jaclet"), self)
            print(button)
            button.clicked.connect(lambda ch,i=i+1: self.function(i))      # < ---
            self.layout.addWidget(button)

    def function(self, i):
        print("butotn",i)

if __name__ == '__main__':
    app = QApplication([])
    mainapp = MainWindow()
    mainapp.show()
    app.exec_()