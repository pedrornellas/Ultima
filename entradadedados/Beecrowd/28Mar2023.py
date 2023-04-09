#Exercicio 2605

"""SELECT p.name AS product_name, pr.name AS provider_name
FROM products p
INNER JOIN categories c ON p.id_categories = c.id
INNER JOIN providers pr ON p.id_providers = pr.id
WHERE c.id = 6;"""

#Exercicio 2606

"""SELECT p.id, p.name 
FROM products p 
JOIN categories c ON p.id_categories = c.id 
WHERE c.name LIKE 'super%';"""

