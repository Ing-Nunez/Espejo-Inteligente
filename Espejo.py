import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer, QTime
from PyQt5.uic import loadUi
import time

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('Interfaz1.ui', self)

        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1000)

    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString('hh:mm:ss')
        self.reloj(displayText)
        self.lcdnumber.display(displayText)

app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())