import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('L\'Étranger', 'Albert Camus', 'Roman', 10, 10))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Fiction', 15, 15))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('Les Misérables', 'Victor Hugo', 'Drame', 5, 5))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('1984', 'George Orwell', 'Science-fiction', 12, 12))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 'Fantaisie', 20, 20))

connection.commit()
connection.close()
