-- Suppression des tables existantes si elles existent déjà
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS livre;
DROP TABLE IF EXISTS emprunts;

-- Table Clients (utilisateurs)
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    adresse TEXT NOT NULL
);

-- Table Livres (gestion des livres)
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    genre TEXT,
    stock_total INTEGER NOT NULL,
    stock_disponible INTEGER NOT NULL
);

-- Table Emprunts (gestion des emprunts)
CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    livre_id INTEGER NOT NULL,
    date_emprunt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_retour TIMESTAMP,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (livre_id) REFERENCES livres(id)
);
