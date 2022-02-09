DROP TABLE IF EXISTS entradas;
CREATE TABLE entradas(
    id integer primary key autoincrement,
    titulo STRING NOT NULL,
    texto STRING NOT NULL
)
