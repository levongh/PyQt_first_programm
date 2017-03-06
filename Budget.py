from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSql
from input_output_dialog import InputOutputTable
from check_open_db import *
from user_sort import *
from user_filter import *
from user_report import *

class TableEditor(QtGui.QDialog):
    def __init__(self, tableName, parent=None):
        super(TableEditor, self).__init__(parent)
        openDB('Personal_Budget.db')
        self.setMinimumSize(QtCore.QSize(520, 550))
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable(tableName)
        self.model.select()

        view = QtGui.QTableView()
        view.setModel(self.model)

        submitButton = QtGui.QPushButton("Input/Output")
        submitButton.setDefault(True)
        quitButton = QtGui.QPushButton("Quit")
        
        #buttons for user querying actions
        sortButton = QtGui.QPushButton("Sort")
        filterButton = QtGui.QPushButton("Filter")
        reportButton = QtGui.QPushButton("Report")

        #buttons collecting
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
        buttonBox.addButton(submitButton, QtGui.QDialogButtonBox.AcceptRole)

        #user buttons
        buttonBox.addButton(sortButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(filterButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(reportButton, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(quitButton, QtGui.QDialogButtonBox.RejectRole)

        #total informations
        total_layout = QtGui.QVBoxLayout()
        total_input_info  = QtGui.QLabel("Total input")
        self.total_input = QtGui.QLabel()
        total_output_info = QtGui.QLabel("Total output")
        self.total_output = QtGui.QLabel()
        total_layout.addWidget(total_input_info)
        total_layout.addWidget(self.total_input)
        total_layout.addWidget(total_output_info)
        total_layout.addWidget(self.total_output)
        
        #connections
        submitButton.clicked.connect(self.submit)
        submitButton.clicked.connect(self.model.select)
        sortButton.clicked.connect(self.run_sort)
        filterButton.clicked.connect(self.run_filter)
        reportButton.clicked.connect(self.show_report)
        quitButton.clicked.connect(self.closeDB)
        quitButton.clicked.connect(self.close)

        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(view)
        left_layout = QtGui.QVBoxLayout()
        left_layout.addWidget(buttonBox)
        left_layout.addLayout(total_layout)
        mainLayout.addLayout(left_layout)
        
        self.setLayout(mainLayout)

        self.setWindowTitle("personal Budget")
        view.show()

        self.tmp_input = InputOutputTable(self)
        self.userSort = SortingTable(self)
        self.userFilter = FilterTable(self)
        self.userReport = ReportTable(self)

        self.update_total_information()

    def closeDB(self):
        close_database('Personal_Budget.db')
        
    def update_total_information(self):
        total_query_i =QtSql.QSqlQuery("select sum(sum) from input_output where type == 'Input'")
        total_query_i.exec_()
        while ( total_query_i.next()):
            self.total_input.setText(str(total_query_i.value(0)))
            total_query_o = QtSql.QSqlQuery("select sum(sum) from input_output where type == 'Output'")
            total_query_o.exec_()
        while ( total_query_o.next()):
            self.total_output.setText(str(total_query_o.value(0)))
                
    
    def submit(self):
        self.tmp_input.show()
        
    def run_sort(self):
        self.userSort.show()

    def run_filter(self):
        self.userFilter.show()

    def show_report(self):
        self.userReport.show()
        
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    editor = TableEditor("input_output")
    editor.show()
    sys.exit(editor.exec_())
