#Exercicio 2609 Beecrowd

import sqlite3 

conexao = sqlite3.connect('beecrowd2609.db')

cursor = conexao.cursor()

#Criar Tabelas products e categories

cursor.execute(
        """CREATE TABLE IF NOT EXISTS products (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  amount INT NOT NULL,
  price INT NOT NULL,
  id_categories INT NOT NULL, 
    CONSTRAINT products_fk FOREIGN KEY (id_categories) REFERENCES categories(id)
);"""

)

cursor.execute(

        """CREATE TABLE IF NOT EXISTS categories (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
  
);"""
)

#Popular as tabelas com os valores, conforme enunciado

cursor.execute(

       """INSERT INTO products (id, name, amount, price, id_categories) VALUES 
    (1, 'Two-doors wardrobe', 100, 800, 1),
    (2, 'Dining table', 1000, 560, 3),
    (3, 'Towel holder', 10000, 25.50, 4),
    (4, 'Computer desk', 350, 320.50, 2),
    (5, 'Chair', 3000, 210.64, 4),
    (6, 'Single bed', 750, 460, 1)
  ;"""

)

cursor.execute(

       """INSERT INTO categories (id, name) VALUES 
    (1, 'wood'),
    (2, 'luxury'),
    (3, 'vintage'),
    (4, 'modern'),
    (5, 'super luxury')
    
  ;"""

)

#Select utilizando uma terceira tabela auxiliar, usando artificio do alias AS, para realizar o join e sum e gerar o resultado esperado no problema.

sql="""
        SELECT categories.name, SUM(products.amount) AS sum
        FROM products
        INNER JOIN categories ON products.id_categories = categories.id
        GROUP BY categories.name;
  """

resultados = cursor.execute(sql)
for resultado in resultados:
    print(resultados)


conexao.commit()
conexao.close()