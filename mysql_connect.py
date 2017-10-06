#pip install MySQL-python
#or conda MySQL-python
#or conda install -c anaconda mysql-connector-python 




import mysql.connector

cnx = mysql.connector.connect(user='liaowenhao', password='kcr01260',host='127.0.0.1',database='elanhome')
print(cnx.is_connected())

cursor = cnx.cursor()
query = ("SELECT * from elanhome.data")

cursor.execute()
# Commit the changes
#cnx.commit()
cnx.close()

