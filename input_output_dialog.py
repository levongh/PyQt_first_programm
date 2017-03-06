from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSql

class InputOutputTable(QtGui.QDialog):
    def __init__(self, parent=None):
        super(InputOutputTable, self).__init__(parent)
        horizontalGroupBox = QtGui.QGroupBox("Input details");
        informationLayout = QtGui.QHBoxLayout()
        
        #the description of the input/output
        descriptionLabel = QtGui.QLabel("Description");
        descriptionEdit = QtGui.QLineEdit()
        informationLayout.addWidget(descriptionLabel)
        informationLayout.addWidget(descriptionEdit)

        #Sum part of input/output dialog
        sumLayout = QtGui.QLabel("Sum")
        sumEdit = QtGui.QLineEdit()
        informationLayout.addWidget(sumLayout)
        informationLayout.addWidget(sumEdit)

        #OK and Cencel buttons
        okButton = QtGui.QPushButton("Ok")
        okButton.setDefault(True)
        cencelButton = QtGui.QPushButton("Cencel")
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        buttonBox.addButton(okButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(cencelButton, QtGui.QDialogButtonBox.RejectRole)

        #the types of action
        typesComboBox = QtGui.QComboBox()
        typesComboBox.addItem("Input", "Input")
        typesComboBox.addItem("Output", "Output")
        informationLayout.addWidget(typesComboBox)

        #the categories
        categoryComboBox = QtGui.QComboBox()
        categoryComboBox.addItem("Salary", "Salary")
        categoryComboBox.addItem("Transport", "Transport")
        categoryComboBox.addItem("Insurance", "Insurance")
        categoryComboBox.addItem("Clothing", "Clothing")
        categoryComboBox.addItem("Banking", "Banking")
        categoryComboBox.addItem("Health", "Health")
        categoryComboBox.addItem("Bonus", "Bonus")
        categoryComboBox.addItem("Other", "Other")
        informationLayout.addWidget(categoryComboBox)
               
        #Slots
        def pars(self):
            if (descriptionEdit.text() == "") or (sumEdit.text() == ""):
                QtGui.QMessageBox.critical(None, "Information Missing",
                                           QtGui.qApp.tr("You can not do this action becouse some argument is \n"
                                                         "missing. Please fill all areas."),
                                           QtGui.QMessageBox.Ok)
            else:
                descriptionString = descriptionEdit.text()
                descriptionEdit.clear()
                sumSize = sumEdit.text()
                sumEdit.clear()
                ioType = typesComboBox.currentText()
                ioCategory = categoryComboBox.currentText()
                query = QtSql.QSqlQuery()
                query.exec_("insert into input_output values('" + descriptionString + "', " + sumSize + ", '" + ioType + "', '" + ioCategory + "')")
                parent.update_total_information()
                parent.model.select()
                   
        #connections
        okButton.clicked.connect(pars)
        okButton.clicked.connect(self.close)
        cencelButton.clicked.connect(self.close)
        buttonsLayout = QtGui.QHBoxLayout()
        space = QtGui.QSpacerItem(30, 10)
        buttonsLayout.addItem(QtGui.QSpacerItem(350, 10));
        buttonsLayout.addWidget(okButton)
        buttonsLayout.addWidget(cencelButton)
        
        #layout correcting
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(informationLayout)
        mainLayout.addLayout(buttonsLayout)
        self.setLayout(mainLayout)


