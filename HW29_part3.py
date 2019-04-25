from PyQt5 import QtCore, QtGui, QtWidgets

from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led=LED(14)

led_pin=24 
GPIO.setup(led_pin, GPIO.OUT)
pwm=GPIO.PWM(led_pin,100)
pwm.start(100)


def ledToggle():
        if led.is_lit:
            led.off()
        else:
            led.on()
        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 310)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 190, 281, 131))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        
        self.verticalSlider.setGeometry(QtCore.QRect(180, 149, 41, 181))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "Toggle LED"))
        self.lineEdit.setText(_translate("MainWindow", "LED Brightness"))
        
        self.pushButton.clicked.connect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)
        
    def sliderMov(self):
        value=self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
        

import sys
app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())