from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSql
from check_open_db import *

class SortingTable(QtGui.QDialog):
    def __init__(self, parent=None):
        super(SortingTable, self).__init__(parent)
        horizontalGroupBox = QtGui.QGroupBox("Sorting Parameters");
        parameterLayout = QtGui.QHBoxLayout()
        self.setWindowTitle("Sortiing Window")
        #the description of the input/output
        parameterLabel = QtGui.QLabel("Sorting Parameter");
        parameterEdit = QtGui.QLineEdit()
        parameterLayout.addWidget(parameterLabel)
        parameterLayout.addWidget(parameterEdit)



        #OK and Cencel buttons
        okButton = QtGui.QPushButton("Ok")
        okButton.setDefault(True)
        cencelButton = QtGui.QPushButton("Cencel")
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(okButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(cencelButton, QtGui.QDialogButtonBox.RejectRole)
               
        #Slots
        def run_sort_in_table(self):
            if (parameterEdit.text() == ""):
                QtGui.QMessageBox.critical(None, "Information Missing",
                                           QtGui.qApp.tr("You can not do this action becouse You don't enter\n"
                                                         "the sorting parameter for sorting"),
                                           QtGui.QMessageBox.Ok)
            else:
                parameter = parameterEdit.text()
                parameterEdit.clear()
                query = QtSql.QSqlQuery("select * from input_output order by " + parameter)
                parent.model.setQuery(query)
                   
        #connections
        okButton.clicked.connect(run_sort_in_table)
        okButton.clicked.connect(self.close)
        cencelButton.clicked.connect(self.close)

        #buttons layout
        buttonsLayout = QtGui.QHBoxLayout()
        space = QtGui.QSpacerItem(30, 10)
        buttonsLayout.addItem(QtGui.QSpacerItem(350, 10));
        buttonsLayout.addWidget(okButton)
        buttonsLayout.addWidget(cencelButton)
        
        #layout correcting
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(parameterLayout)
        mainLayout.addLayout(buttonsLayout)
        self.setLayout(mainLayout)


