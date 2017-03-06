import sys
from PyQt4 import QtGui, QtSql, QtCore

def createConnection():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('Personal_Budget.db')
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\n"
                              "Click Cancel to exit."),
                QtGui.QMessageBox.Cancel)
        return False
    
    query = QtSql.QSqlQuery()
    query.exec_("create table input_output(Description varchar(20), sum int, type VARCHAR(10), category VARCHAR(15))")
    query.exec_("insert into input_output values('Salari', 1000, 'Input', 'Salary')")
    query.exec_("insert into input_output values('Bonus', 500, 'Input', 'Banking')")
    query.exec_("insert into input_output values('Debth', 2000, 'Output', 'Other')")

    return True

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)

