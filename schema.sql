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
    adresse TEXT NOT NULL,
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

--CREATE TABLE livres (
  --  id INTEGER PRIMARY KEY AUTOINCREMENT,
    --titre TEXT NOT NULL,
    --auteur TEXT NOT NULL,
    --genre TEXT,
    --annee_publication INTEGER,
    --nombre_exemplaires INTEGER NOT NULL CHECK (nombre_exemplaires >= 0),
    --disponible INTEGER NOT NULL DEFAULT 1 CHECK (disponible IN (0, 1))
--);

-- Table Emprunts (relation entre clients et livres)
/*CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    id_livre INTEGER NOT NULL,
    date_emprunt TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_retour TIMESTAMP,
    CONSTRAINT fk_client FOREIGN KEY (id_client) REFERENCES clients(id),
    CONSTRAINT fk_livre FOREIGN KEY (id_livre) REFERENCES livres(id),
    CONSTRAINT unique_emprunt UNIQUE (id_client, id_livre, date_retour)
);*/
