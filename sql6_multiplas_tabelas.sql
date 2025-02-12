-- Use o banco de dados restaurante e crie os joins ou subconsultas
USE restaurante;

-- Selecionar:
-- produtos: id, nome e descrição
-- info_produtos:  ingredientes
SELECT p.id_produto, p.nome, p.descricao, ip.ingredientes
FROM produtos p
JOIN info_produtos ip ON p.id_produto = ip.id_produto;


-- Selecionar:
-- pedidos:  id, quantidade e data
-- clientes: nome e email
SELECT p.id_pedido, p.quantidade, p.data_pedido, c.nome, c.email
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente;


-- Selecionar:
-- pedidos:  id, quantidade e data
-- clientes: nome e email
-- funcionarios: nome
SELECT p.id_pedido, p.quantidade, p.data_pedido, c.nome, c.email, f.nome AS funcionario
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
JOIN funcionarios f ON p.id_funcionario = f.id_funcionario;


-- Selecionar:
-- pedidos:  id, quantidade e data
-- clientes: nome e email
-- funcionarios: nome
-- produtos: nome, preco
SELECT pe.id_pedido, pe.quantidade, pe.data_pedido, c.nome, c.email, f.nome AS funcionario, pr.nome AS produto, pr.preco
FROM pedidos pe
JOIN clientes c ON pe.id_cliente = c.id_cliente
JOIN funcionarios f ON pe.id_funcionario = f.id_funcionario
JOIN produtos pr ON pe.id_produto = pr.id_produto
ORDER BY pe.id_pedido;

-- Selecionar o nome dos clientes com os pedidos com status ‘Pendente’ e exibir por ordem descendente de acordo com o id do pedido
SELECT c.nome
FROM clientes c
JOIN pedidos p ON p.id_cliente = c.id_cliente
WHERE p.status_pedido = 'Pendente'
ORDER BY p.id_pedido DESC;


-- Selecionar clientes sem pedidos
SELECT c.*
FROM clientes c
LEFT JOIN pedidos p ON p.id_cliente = c.id_cliente
WHERE p.id_pedido IS NULL;


-- Selecionar o nome do cliente e o total de pedidos cada cliente
SELECT clientes.nome,
	(SELECT COUNT(*) FROM pedidos WHERE pedidos.id_cliente = clientes.id_cliente) AS qtd_pedidos
FROM clientes ORDER BY qtd_pedidos DESC;


-- Selecionar o preço total (quantidade*preco) de cada pedido
SELECT SUM(pe.quantidade * pr.preco) AS preco_total
FROM pedidos pe
JOIN produtos pr ON pe.id_produto = pr.id_produto
GROUP BY pe.id_pedido
ORDER BY preco_total DESC;

-- Como submeter sua entrega: Salve o script como “multiplas_tabelas.sql” e envie o arquivo para os tutores no campo de entrega.