from PedSimulation.example.model.sfmodel import SFModel
from PedSimulation.example.listener import *
from PedSimulation.example.strategy import NearestGoalStrategy
from PedSimulation.scene import Scene
from PedSimulation.gui.panel import *
from PedSimulation.gui.ui.mainwindow_main import *
from PyQt5 import QtWidgets
import sys
import qdarkstyle

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    m = MainWindow("MainWindow")
    m.show()
    app.installEventFilter(m)
    sys.exit(app.exec_())
