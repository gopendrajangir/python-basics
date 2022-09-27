import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = ""
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

databases = []

for x in mycursor:
    databases.append(x[0])

mycursor.execute("USE mydatabase")

print(databases)

if "mydatabase" not in databases:
    mycursor.execute("CREATE DATABASE mydatabase")

tables = []

mycursor.execute("SHOW TABLES")

for x in mycursor:
    tables.append(x[0])

if 'customers' not in tables:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)