import sys

import pypyodbc
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("dialog.ui")

driver = 'DRIVER={SQL Server}'
server = 'SERVER=LAPTOP-TB8OGQS4'
db = 'DATABASE=book_store'
conn_str = ';'.join([driver, server, db])

conn = pypyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute('select * from clients')
# row = cursor.fetchone()
rest_of_rows = cursor.fetchall()

# print(row)
print(rest_of_rows)

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
