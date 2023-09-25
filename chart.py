from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
pyplot.rcParams['font.sans-serif'] = 'SimHei'#设置中文显示


class Figure_Canvas(FigureCanvas):  # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    def __init__(self, parent=None):
        fig = Figure(dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)
        self.axes = pyplot.axes()  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法


class FigureCanvasQTAgg(FigureCanvas):

    def print_figure(self, *args, **kwargs):
        super().print_figure(*args, **kwargs)
        self.draw()


class Figure_Bar(FigureCanvasQTAgg):

    def __init__(self, width, height, x, y,  parent=None):
        self.fig = pyplot.figure(figsize=(width, height), facecolor='#666666', dpi=100, edgecolor='#0000FF')
        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)
        self.myAxes = self.fig.add_subplot(111)
        self.x = x
        self.y = y

    def ShowScatter(self):
        # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图，最后刷新显示。
        self.myAxes.clear()
        self.myAxes.scatter(self.x, self.y)
        # 刷新画布，否则不刷新显示
        self.fig.canvas.draw()

    def ShowPlot(self):
        self.myAxes.clear()
        self.myAxes.plot(self.x, color='blue')
        self.myAxes.plot(self.y, color='red')
        # pyplot.show()
        self.fig.canvas.draw()

    def ShowPie(self, values, explode, label):
        self.myAxes.clear()
        self.myAxes.pie(values, explode=explode, labels=label, autopct='%1.1f%%')
        # pyplot.show()
        self.fig.canvas.draw()

    def Clear(self):
        self.myAxes.clear()



