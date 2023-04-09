import sqlite3 

conexao = sqlite3.connect('maonamassa.db')

cursor = conexao.cursor()
cursor.execute(

    '''CREATE TABLE IF NOT EXISTS Fornecedor (
    id INT NOT NULL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    produto VARCHAR(255) NOT NULL
    );'''
)

cursor.execute(
    
     """INSERT INTO Fornecedor (id, nome, endereco, produto) VALUES 
  (1, 'Empresa de Leite Parmaleite', 'Rua dos Leites, 23', 'Leite'),
  (2, 'Peixaria Abril', 'Rua dos Leites, 26', 'Peixe'),
  (3, 'Açougue Legal', 'Rua das Carnes, 30', 'Carnes'),
  (4, 'Açougue Novo', 'Rua das Carnes, 50', 'Carnes'),
  (5, 'Padaria do Pão', 'Rua dos Pães, 20', 'Pão'),
  (6, 'Marcenaria Martelo', 'Rua dos Quitutes, 30', 'Diversos')
  ;"""
)

cursor.execute(
    
    """UPDATE Fornecedor
    SET endereco = "Rua dos Peixes, 26"
    WHERE id = 2;
    
    """
)

cursor.execute(
    
    """SELECT * FROM Fornecedor
    
    """
)

cursor.execute(
    
    """SELECT * FROM Fornecedor
    
    """
)

cursor.execute(
    
    """SELECT * FROM Fornecedor WHERE produto = "Carnes"
    
    """
)

cursor.execute(
    
    """DELETE FROM Fornecedor WHERE id = 1
    
    """
)

conexao.commit()
conexao.close()