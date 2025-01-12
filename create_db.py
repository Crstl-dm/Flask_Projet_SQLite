import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des clients existants
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)", ('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))

# Insertion des livres existants
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('L\'Étranger', 'Albert Camus', 'Roman', 10, 10))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Fiction', 15, 15))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('Les Misérables', 'Victor Hugo', 'Drame', 5, 5))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('1984', 'George Orwell', 'Science-fiction', 12, 12))
cur.execute("INSERT INTO livres (titre, auteur, genre, stock_total, stock_disponible) VALUES (?, ?, ?, ?, ?)", ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 'Fantaisie', 20, 20))

# Insertion des emprunts de test
cur.execute("INSERT INTO emprunts (client_id, livre_id, date_emprunt, date_retour) VALUES (?, ?, ?, ?)", (1, 1, '2023-01-15', '2023-01-22'))
cur.execute("INSERT INTO emprunts (client_id, livre_id, date_emprunt, date_retour) VALUES (?, ?, ?, ?)", (2, 2, '2023-01-20', '2023-01-27'))
cur.execute("INSERT INTO emprunts (client_id, livre_id, date_emprunt, date_retour) VALUES (?, ?, ?, ?)", (3, 3, '2023-02-01', '2023-02-08'))


connection.commit()
connection.close()
