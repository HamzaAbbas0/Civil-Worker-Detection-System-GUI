from PyQt5.QtWidgets \
import QMainWindow,QApplication, QWidget, QPushButton,QLineEdit,QTableWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic, QtWidgets,QtGui
import sys

class Ui(QMainWindow):
    def __init__(self):
        global table
        super(Ui,self).__init__()
        uic.loadUi("qt-design.ui",self)
        self.somefunction()
        self.btnstate()
        # string value
        self.setWindowIcon(QtGui.QIcon('hackerspacelogo.png'))
        title = "Saftey-Detection-System"
        self.setFixedSize(550,620)
        # set the title
        self.setWindowTitle(title)


    def somefunction(self):
        global button_array, data, Multiple_selection
        button_array = []
        Multiple_selection = 0
        data = ["helmet", "gloves", "jacket", "googles", "mask", "faceshield","coverall"]
        # define some widgets of Buttons
        #for i in range(6):
        self.button = self.findChild(QtWidgets.QPushButton,  'pushButton')
        self.button1= self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.button2 = self.findChild(QtWidgets.QPushButton, 'pushButton_3')
        self.button3 = self.findChild(QtWidgets.QPushButton, 'pushButton_4')
        self.button4= self.findChild(QtWidgets.QPushButton, 'pushButton_5')
        self.button5 = self.findChild(QtWidgets.QPushButton, 'pushButton_6')
        self.button6 = self.findChild(QtWidgets.QPushButton, 'pushButton_7')

        #Multiple Selection button
        self.button7 = self.findChild(QtWidgets.QPushButton, 'pushButton_8')
        self.button7.setCheckable(True)

        #clear button
        self.button8 = self.findChild(QtWidgets.QPushButton, 'pushButton_9')


        choose_the_option = [self.button , self.button1,self.button2,self.button3,self.button4,self.button5,self.button6]
        self.button.clicked.connect(lambda x:self.function(1))
        self.button1.clicked.connect(lambda x: self.function(2))
        self.button2.clicked.connect(lambda x: self.function(3))
        self.button3.clicked.connect(lambda x:self.function(4))
        self.button4.clicked.connect(lambda x: self.function(5))
        self.button5.clicked.connect(lambda x: self.function(6))
        self.button6.clicked.connect(lambda x: self.function(7))
        #demo work button
        self.button7.clicked.connect(self.append)
        self.button7.clicked.connect(self.btnstate)
        self.button8.clicked.connect(self.destroy)


        #print(choose_the_option)

    def btnstate(self):
        if self.button7.isChecked():
            print("button pressed")
            self.button7.setStyleSheet("background-color:green;border-radius :20px;color :white")

        else:
            print("button released")
            self.button7.setStyleSheet("background-color:red;;border-radius :20px;color :white")




    def function(self,i):
        global button_array,data, Multiple_selection,final_selection
        print(i)

        if Multiple_selection == 1:
            print('code ise here')
            button_array.append(data[i-1])
            print(button_array)
            final_selection = button_array
        else:
            print(data[i - 1])
            final_selection = data[i-1]
        print('options selected =',final_selection)

    def append(self):
        global Multiple_selection
        if Multiple_selection ==0:
            Multiple_selection = 1
        elif Multiple_selection ==1:
            Multiple_selection =0

    def destroy(self):
        global Multiple_selection,final_selection, button_array
        #self.button2.clear()

        button_array=[]
        # final_selection=" "
        # print(final_selection)
        print("empty all")











if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window1 = QMainWindow()
    ui = Ui()
    ui.show()
    sys.exit(app.exec_())