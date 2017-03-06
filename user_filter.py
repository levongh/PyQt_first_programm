from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSql
from check_open_db import *

class FilterTable(QtGui.QDialog):
    def __init__(self, parent=None):
        super(FilterTable, self).__init__(parent)
        horizontalGroupBox = QtGui.QGroupBox("Filter Categories");
        categoryLayout = QtGui.QHBoxLayout()
        self.setWindowTitle("Filter Window")
        #the description of the input/output
        categoryLabel = QtGui.QLabel("Filter by");
        categoryEdit = QtGui.QLineEdit()
        categoryLayout.addWidget(categoryLabel)
        categoryLayout.addWidget(categoryEdit)



        #OK and Cencel buttons
        okButton = QtGui.QPushButton("Ok")
        okButton.setDefault(True)
        cencelButton = QtGui.QPushButton("Cencel")
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(okButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(cencelButton, QtGui.QDialogButtonBox.RejectRole)
               
        #Slots
        def run_filter_table(self):
            if (categoryEdit.text() == ""):
                QtGui.QMessageBox.critical(None, "Information Missing",
                                           QtGui.qApp.tr("You can not do this action becouse You don't enter\n"
                                                         "the category of filtering datas"),
                                           QtGui.QMessageBox.Ok)
            else:
                category = categoryEdit.text()
                categoryEdit.clear()
                query = QtSql.QSqlQuery("Select * from input_output where category == '" + category + "'")
                parent.model.setQuery(query)
                                
        #connections
        okButton.clicked.connect(run_filter_table)
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
        mainLayout.addLayout(categoryLayout)
        mainLayout.addLayout(buttonsLayout)
        self.setLayout(mainLayout)


