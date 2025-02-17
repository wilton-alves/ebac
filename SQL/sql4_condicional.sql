
-- 1. Use o banco de dados restaurante
USE restaurante;

-- 2. Selecione todos os pedidos que do id funcionário igual a 4 e status é igual a ‘Pendente’
SELECT * FROM pedidos WHERE id_funcionario = 4 AND status_pedido = 'Pendente';

-- 3. Selecione todos os pedidos que o status não é igual a ‘Concluído’
SELECT * FROM pedidos WHERE status_pedido <> 'Concluído';

-- 4. Selecione os pedidos que contenham os id produtos: 1, 3, 5, 7 ou 8
SELECT * FROM pedidos WHERE id_produto IN(1, 3, 5, 7, 8);

-- 5. Selecione os clientes que começam com a letra c
SELECT * FROM clientes WHERE nome LIKE 'C%';

-- 6. Selecione as informações de produtos que contenham nos ingredientes ‘carne’ ou ‘frango’
SELECT * FROM info_produtos WHERE ingredientes LIKE '%carne%' OR ingredientes LIKE '%frango%';

-- 7. Selecione os produtos com o preço entre 20 a 30
SELECT * FROM produtos WHERE preco BETWEEN 20 AND 30;

-- 8. Atualizar id pedido 6 da tabela pedidos para status = NULL
UPDATE pedidos SET status_pedido = NULL WHERE id_pedido = 6;

-- 9. Selecione os pedidos com status nulos
SELECT * FROM pedidos WHERE status_pedido IS NULL;

-- 10. Selecionar o id pedido e o status da tabela pedidos, porém para todos os status nulos, mostrar 'Cancelado'
SELECT id_pedido, IFNULL(status_pedido, 'Cancelado') AS status_pedido FROM pedidos;

-- 11. Selecione o nome, cargo, salário dos funcionários e adicione um campo chamado media_salario, que irá mostrar ‘Acima da média’, para o salário > 3000, senão 'Abaixo da média'
SELECT nome, cargo, salario,
	IF(salario > 3000, 'Acima da média', 'Abaixo da média')
    AS media_salario
FROM funcionarios;