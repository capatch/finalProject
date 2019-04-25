# Task 2
#import pyqtgraph as pg
#from pyqtgraph.Qt import QtCore, QtGui
#from pyqtgraph import PlotWidget
#import numpy as np
#
#x=np.array([1,2,3])
#y=np.array([1,2,3])
#pg.setConfigOption('background','w')
#penn=pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine)
#p1=pg.plot(x,y,pen=penn, title='The first pyqtgraph plot', symbol='t', symbolSize=20)
#p1.setXRange(0,4)
#p1.setYRange(0,4)
#p1.setLabel('left','Voltage','V')
#p1.setLabel('bottom','Time','s')
#
#QtGui.QApplication.exec_()

from PyQt5 import QtGui, QtCore
import pyqtgraph as pg

# Initialize Qt
app = QtGui.QApplication([])
# Define top-level widget
w = QtGui.QWidget()
# Create some widgets to be placed inside
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')
listw=QtGui.QListWidget()
pg.setConfigOption('background','w')
plt=pg.PlotWidget() 
penn=pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine)
plt.plot([1,2,3],[1,2,3], pen=penn, title='The first pyqtgraph plot', symbol='t', symbolSize=20)

labelStyle={'color':'#000', 'font-size':'30px'}
plt.setLabel('bottom','Time','s',**labelStyle)
plt.setLabel('left','Voltage','V',**labelStyle)
plt.setYRange(0,5)
plt.setXRange(0,5)

layout = QtGui.QGridLayout()
w.setLayout(layout)
 
layout.addWidget(btn, 0,0)
layout.addWidget(text, 1,0)
layout.addWidget(listw,2,0)
layout.addWidget(plt,0,1,3,1)

w.show()
app.exec_()
