import sqlite3

connection = sqlite3.connect('app.db') # Connect to the SQLite database (or create it if it doesn't exist)
cursor = connection.cursor()  # Create a cursor object to execute SQL commands

cursor.execute('''
CREATE TABLE IF NOT EXISTS stock (
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS stock_price (
     id INTEGER PRIMARY KEY,
     stock_id INTEGER,
     date NOT NULL,
     open NOT NULL,
     high NOT NULL,
     low NOT NULL,
     close NOT NULL,
     adjusted_close NOT NULL,
     volume NOT NULL,
     FOREIGN KEY (stock_id) REFERENCES stock (id)
)
''')

connection.commit() 