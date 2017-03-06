from PyQt4 import QtSql

def openDB(dbName):
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(dbName)
    if not db.open():
        QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
                QtGui.qApp.tr("Unable to establish a database connection.\n"
                              "This example needs SQLite support. Please read "
                              "the Qt SQL driver documentation for information "
                              "how to build it.\n\n"
                              "Click Cancel to exit."),
                                QtGui.QMessageBox.Cancel)
        return False
    return True
    
def close_database(dbName):
    db = QtSql.QSqlDatabase.database('Personal_Budget.db')
    db.close()
    QtSql.QSqlDatabase.removeDatabase('Personal_Budget.db')
