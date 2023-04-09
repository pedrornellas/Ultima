import sqlite3 

conexao = sqlite3.connect('db.sqlite3')

cursor = conexao.cursor()
cursor.execute(
        'CREATE TABLE categoria (id INT NOT NULL,nome VARCHAR(100), PRIMARY KEY (id));'

)
cursor. execute(
        'CREATE TABLE produto (id INT NOT NULL, nome VARCHAR(100), categoria_id INT NOT NULL, PRIMARY KEY (id), FOREIGN KEY (categoria_id) REFERENCES categoria(id));'
)

conexao.commit()
conexao.close()