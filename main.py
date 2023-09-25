import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsScene, QFileDialog, QMessageBox, QFrame
from ui_form2 import Ui_Form
from chart import Figure_Canvas, Figure_Bar
from PySide2.QtCore import *
import pandas as pd
import numpy as np
from collections import Counter

F = ""
Dataset = []
values = []
label = []
explode = []
X = []
Y = []

class PyMain(QWidget):
    def __init__(self):
        super(PyMain, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def __openByIODevice(self, fileName):  ## open the file
        fileDevice = QFile(fileName)
        if not fileDevice.exists():
            return False

        if not fileDevice.open(QIODevice.ReadOnly | QIODevice.Text):
            return False

        try:
            self.ui.textEdit.clear()
        finally:
            fileDevice.close()
        return True

    def on_actQFile_Open_triggered(self):
        curPath = QDir.currentPath()
        title = "open a .csvFile"
        filt = "CSVfile(*.csv)"
        fileName, flt = QFileDialog.getOpenFileName(self, title, curPath, filt)
        if (fileName == ""):
            return

        if self.__openByIODevice(fileName):
            self.ui.textEdit.insertPlainText(fileName)
            print(fileName)
            global F
            F = fileName
            self.getData()
        else:
            QMessageBox.critical(self, "error", "failed to open the file")

    def getData(self):
        data = pd.read_csv(F)
        data = np.array(data)
        global Dataset,X,Y,values
        Dataset = data[:, 0]
        for each in Dataset:
            if each not in label:
                # print(each)
                label.append(each)
                explode.append(0.01)
        # print(Counter(Dataset))
        Value = Counter(Dataset)
        for v in Value.values():
            values.append(v)
            # print(v)

        X = data[:, 1]
        Y = data[:, 2]

    def signalExit(self):
        QApplication.exit()

    def signalPlot(self):
        width = self.ui.graphicsView.width()
        height = self.ui.graphicsView.height()
        self.myImage = Figure_Bar(width / 100, height / 100, X, Y)
        self.myGraphyScene = QGraphicsScene()
        self.ui.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene.addWidget(self.myImage)
        self.ui.graphicsView.setScene(self.myGraphyScene)
        self.myImage.ShowPlot()

    def signalScatter(self):
        width = self.ui.graphicsView.width()
        height = self.ui.graphicsView.height()
        self.myImage = Figure_Bar(width / 100, height / 100, X, Y)
        self.myGraphyScene = QGraphicsScene()

        self.ui.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.myQGraphicsProxyWidget = self.myGraphyScene.addWidget(self.myImage)
        self.ui.graphicsView.setScene(self.myGraphyScene)

        self.myImage.ShowScatter()

    def signalPie(self):
        width = self.ui.graphicsView.width()
        height = self.ui.graphicsView.height()
        self.myImage = Figure_Bar(width / 100, height / 100, X, Y)
        self.myGraphyScene = QGraphicsScene()
        self.ui.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene.addWidget(self.myImage)
        self.ui.graphicsView.setScene(self.myGraphyScene)
        self.myImage.ShowPie(values, explode, label)

    def signalClear(self):
        width = self.ui.graphicsView.width()
        height = self.ui.graphicsView.height()
        self.myImage = Figure_Bar(width / 100, height / 100, X, Y)
        self.myGraphyScene = QGraphicsScene()

        self.ui.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.myQGraphicsProxyWidget = self.myGraphyScene.addWidget(self.myImage)
        self.ui.graphicsView.setScene(self.myGraphyScene)
        self.myImage.Clear()

    def slotExit(self):
        self.ui.pushButton_4.clicked.connect(self.signalExit)

    def slotPlot(self):
        self.ui.pushButton.clicked.connect(self.signalPlot)

    def slotScatter(self):
        self.ui.pushButton_2.clicked.connect(self.signalScatter)

    def slotPie(self):
        self.ui.pushButton_3.clicked.connect(self.signalPie)

    def slotClear(self):
        self.ui.pushButton_5.clicked.connect(self.signalClear)

    def openSlot(self):
        self.ui.toolButton.clicked.connect(self.on_actQFile_Open_triggered)


if __name__ == "__main__":
    if QApplication.instance():
        QApplication.instance().exit()
    app = QApplication([])
    widget = PyMain()
    widget.slotExit()
    widget.slotScatter()
    widget.slotClear()
    widget.slotPlot()
    widget.slotPie()
    widget.openSlot()
    widget.show()
    sys.exit(app.exec_())

