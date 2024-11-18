import mysql.connector

# Connect to server
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mike",
    password="s3cre3t!")

# Get a cursor
mycursor = mydb.cursor()

# Execute a query
mycursor.execute("SELECT CURDATE()")

# Fetch one result
recordsList = mycursor.fetchall()

print("Current date is: {0}".format(recordsList[0]))

# Close connection
mydb.close()
