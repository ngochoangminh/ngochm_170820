import csv
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
    user='my_user',
    passwd='Ngoc_3201',
    db='my_database')
cursor = mydb.cursor()
# Create table customer
# cursor.execute("CREATE TABLE customer( customerid VARCHAR(50) NOT NULL PRIMARY KEY, firstname VARCHAR(255) NOT NULL, lastname VARCHAR(255) NOT NULL, \
#     companyname VARCHAR(255) NOT NULL,billingaddress1 VARCHAR(255) NOT NULL,billingaddress2 VARCHAR(255), city VARCHAR(255) NOT NULL, \
#     state VARCHAR(50) NOT NULL, postalcode INT NOT NULL, country VARCHAR(50) NOT NULL,   phonenumber VARCHAR(50) NOT NULL,\
#     emailaddress VARCHAR(255) NOT NULL, createddate VARCHAR(255) NOT NULL);")

# Load data from .csv file
csv_path= r"/home/ngoc/Downloads/customer.csv"
with open(csv_path, mode='r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')
    csv_data_list = list(reader)
    for row in csv_data_list:
        print(row)
        cursor.execute("INSERT INTO customer(customerid, firstname, lastname, companyname, state,\
            postalcode, country, phonenumber, emailaddress, createddate \
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

#close the connection to the database.
mydb.commit()
cursor.close()
mydb.close()
print("Done")

'customerid', 'firstname', 'lastname', 'companyname', 'billingaddress1', 'billingaddress2', 'city', 'state', 'postalcode', 'country', 'phonenumber', 'emailaddress', 'createddate'