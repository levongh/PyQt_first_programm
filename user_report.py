from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSql
import sys
import random
from check_open_db import *

class ReportTable(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ReportTable, self).__init__(parent)
        self.scene = QtGui.QGraphicsScene()
        self.categories = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.colours = []
        set_angle = 0
        count1 = 0
        total = len(self.categories)
        self.setWindowTitle("Report Results")
        
        #ellipse.setStartAngle(set_angle)
        #ellipse.setPos(0, 0)
        
        for count in range(len(self.categories)):  
            number = []
            for count in range(5):
                number.append(random.randrange(0, 255))
            self.colours.append(QtGui.QColor(number[0], number[1], number[2], number[4]))
            
        #self.total_result = QtSql.QSqlQuery("select sum(sum)from input_output")
        for c in self.categories:
            #ellipse.setStartAngle(set_angle)
            angle = round(c/total*16*360)
            ellipse = QtGui.QGraphicsEllipseItem(0, 0, 400, 400)
            ellipse.setPos(0, 0)
            ellipse.setStartAngle(set_angle)
            ellipse.setSpanAngle(angle)
            ellipse.setBrush(self.colours[c])
            set_angle = angle + set_angle
            #count1 +=1
            self.scene.addItem(ellipse)
        view = QtGui.QGraphicsView(self.scene)
            

        values_list = QtGui.QVBoxLayout()
        category_list = ['Salary', 'Transport', 'Insurance', 'Clothing', 'Banking', 'Health', 'Bonus', 'Other']
        for c in category_list:
            tmp = c + '_label'
            c_query = QtSql.QSqlQuery("select sum(sum) from input_output where category == '" + c + "'")
            zero_value = 0;
            while (c_query.next()):
                if c_query.isNull(0):
                    zero_value = 0
                else:
                    zero_value = c_query.value(0)                    
            tmp = QtGui.QLabel(c + ":   " + str(zero_value))
            values_list.addWidget(tmp)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(view)
        mainLayout.addLayout(values_list)
        self.setLayout(mainLayout)
        view.show()
